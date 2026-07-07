# frozen_string_literal: true

Jekyll::Hooks.register :documents, :pre_render do |document|
  next unless document.collection.label == "interviews"
  next if document.data["description"]
  next unless document.data["teaser"]

  document.data["description"] = document.data["teaser"]
end
