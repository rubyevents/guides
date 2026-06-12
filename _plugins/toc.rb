# frozen_string_literal: true

require "nokogiri"

# Vendored, simplified table-of-contents generator.
#
# Inspired by jekyll-toc (https://github.com/toshimaru/jekyll-toc), reduced to
# exactly what this site needs: turn the rendered guide HTML into the chapter
# list we show in the sidebar, the inline mobile block, and the sticky header.
#
# Usage: drop an HTML comment marker where the contents list should appear:
#
#   <nav class="toc toc--desktop" aria-label="Guide contents"><!--toc--></nav>
#
# After the page is rendered, every <!--toc--> is replaced with an <ol> built
# from the page's own <h2 id="..."> headings. It reads the ids kramdown already
# injects, so anchors always match the real headings — no id generation, and no
# manual `chapters:` front matter to keep in sync.
module Jekyll
  module Toc
    MARKER = "<!--toc-->"

    # Only chapters (h2) appear in the contents, matching the guide design.
    HEADING_SELECTOR = "h2[id]"

    module_function

    def build(html)
      headings = Nokogiri::HTML::DocumentFragment.parse(html).css(HEADING_SELECTOR)
      return "" if headings.empty?

      items = headings.map do |heading|
        id = heading["id"]
        text = CGI.escapeHTML(heading.text.strip)
        %(<li class="toc__item"><a class="toc__link" href="##{id}">#{text}</a></li>)
      end

      %(<ol class="toc__list">#{items.join}</ol>)
    end
  end
end

Jekyll::Hooks.register([:pages, :documents], :post_render) do |doc|
  output = doc.output
  next unless output&.include?(Jekyll::Toc::MARKER)

  list = Jekyll::Toc.build(output)
  doc.output = output.gsub(Jekyll::Toc::MARKER, list)
end
