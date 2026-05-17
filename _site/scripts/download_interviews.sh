#!/usr/bin/env bash
set -euo pipefail

BASE_URL="https://rubyconferenceproject.com"
INDEX_URL="$BASE_URL/interviews/"
OUT_DIR="${1:-interviewss}"

usage() {
  cat <<'USAGE'
Usage: scripts/download_interviews.sh [output-dir]

Downloads every interview listed at https://rubyconferenceproject.com/interviews/
and saves each article as Markdown. The default output directory is ./interviewss.
USAGE
}

die() {
  echo "Error: $1" >&2
  exit "${2:-1}"
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"
}

markdown_url() {
  local url="$1"
  curl -fsSL "https://markdown.new/$url"
}

extract_markdown_content() {
  awk '
    found { print }
    /^Markdown Content:$/ { found = 1; next }
  ' | sed '1{/^$/d;}'
}

add_source_url() {
  local source_url="$1"
  awk -v source_url="$source_url" '
    NR == 1 && $0 == "---" {
      print
      print "source_url: " source_url
      next
    }
    { print }
  '
}

interview_paths() {
  curl -fsSL "$INDEX_URL" |
    grep -oE 'href="/[0-9]{4}-[0-9]{2}-[0-9]{2}[^"]+/"' |
    sed -E 's/^href="//; s/"$//' |
    awk '!seen[$0]++'
}

download_interview() {
  local path="$1"
  local url="$BASE_URL$path"
  local slug="${path#/}"
  slug="${slug%/}"
  local destination="$OUT_DIR/$slug.md"
  local raw markdown

  echo "Downloading $url -> $destination"
  raw="$(markdown_url "$url")"

  if grep -q '"success":false' <<<"$raw"; then
    die "markdown.new failed for $url"
  fi

  markdown="$(printf '%s\n' "$raw" | extract_markdown_content)"
  [[ -n "$markdown" ]] || die "No Markdown content extracted for $url"

  printf '%s\n' "$markdown" | add_source_url "$url" > "$destination"
}

main() {
  if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    return 0
  fi

  require_command curl
  require_command grep
  require_command sed
  require_command awk

  mkdir -p "$OUT_DIR"

  local paths=()
  mapfile -t paths < <(interview_paths)
  ((${#paths[@]} > 0)) || die "No interview links found at $INDEX_URL"

  for path in "${paths[@]}"; do
    download_interview "$path"
  done

  echo "Downloaded ${#paths[@]} interviews to $OUT_DIR/"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main "$@"
fi
