#!/usr/bin/env python3
import re
import sys
from pathlib import Path

SPEAKER_ALIASES = {
    "cirdes": "Cirdes Henrique",
    "hharen": "Hana Harencarova",
}

TRANSCRIPT_HEADINGS = {"transcript", "transcript:"}


def normalize_speaker(name: str) -> str:
    return SPEAKER_ALIASES.get(name.strip(), name.strip())


def clean_text(text: str) -> str:
    text = text.replace("\u2026", "...")
    text = re.sub(r"\\(?=\.)", "", text)
    text = re.sub(r"\b1st\b", "first", text, flags=re.I)
    text = re.sub(r"\b2nd\b", "second", text, flags=re.I)
    text = re.sub(r"\b3rd\b", "third", text, flags=re.I)
    text = re.sub(r"\b(\d+)th\b", r"\1th", text, flags=re.I)

    # Remove only obvious standalone filler placeholders.
    text = re.sub(r"(?i)(^|[\s,;:—-])(?:um+|uh+|ah+|erm+|hmm+)(?=$|[\s,.;:!?—-])", r"\1", text)

    # Common transcript punctuation cleanup.
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"([.!?])\s*,", r"\1", text)
    text = re.sub(r",\s*,+", ",", text)
    text = re.sub(r"\s+-\s+", "—", text)
    text = re.sub(r"\.\.\.\s*\.\.\.", "...", text)
    text = re.sub(r"\s+\.\.\.", "...", text)

    # Obvious Ruby ecosystem casing/transcription artifacts.
    replacements = [
        (r"\bruby\b", "Ruby"),
        (r"\brails\b", "Rails"),
        (r"\brubyists\b", "Rubyists"),
        (r"\bRuby Central\b", "Ruby Central"),
        (r"\bRuby central\b", "Ruby Central"),
        (r"\bRails Conf\b", "RailsConf"),
        (r"\bRails\. Conf\b", "RailsConf"),
        (r"\bRuby Conf\b", "RubyConf"),
        (r"\bRubyconf\b", "RubyConf"),
        (r"\bRuby Kaigi\b", "RubyKaigi"),
        (r"\bRuby Kiki\b", "RubyKaigi"),
        (r"\bJavascript\b", "JavaScript"),
        (r"\bJS\b", "JS"),
        (r"\bAV\b", "AV"),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text, flags=re.I)

    # Clean duplicated adjacent words introduced by auto captions.
    text = re.sub(r"\b(to)\s+\1\b", r"\1", text, flags=re.I)
    text = re.sub(r"\b(the)\s+\1\b", r"\1", text, flags=re.I)
    text = re.sub(r"\b(and)\s+\1\b", r"\1", text, flags=re.I)
    text = re.sub(r"\b(can)\s+\1\b", r"\1", text, flags=re.I)
    text = re.sub(r"\b(I)\s+\1\b", r"\1", text)

    # Sentence-start capitalization for very common caption line breaks.
    text = re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), text)
    return text.strip()


def collect_speakers(lines):
    speakers = []
    for line in lines:
        m = re.match(r"^([A-Za-z][A-Za-z0-9 ._-]{1,40}):\s*", line)
        if not m:
            continue
        name = m.group(1).strip()
        if name in {"source_url", "title", "description", "image", "LinkedIn", "Rails Foundation", "SF Ruby", "Evil Martians", "Tropical on Rails", "Helvetic Ruby", "Helvetic Ruby LinkedIn"}:
            continue
        name = normalize_speaker(name)
        if name not in speakers:
            speakers.append(name)
    return speakers


def split_speaker_segments(line, speakers):
    aliases = set(speakers) | set(SPEAKER_ALIASES) | set(SPEAKER_ALIASES.values())
    if not aliases:
        return [(None, line)]
    pattern = re.compile(r"(?<!\*)\b(" + "|".join(re.escape(s) for s in sorted(aliases, key=len, reverse=True)) + r"):\s*")
    matches = list(pattern.finditer(line))
    if not matches:
        return [(None, line)]
    segments = []
    if matches[0].start() > 0:
        before = line[:matches[0].start()].strip()
        if before:
            segments.append((None, before))
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(line)
        speaker = normalize_speaker(match.group(1))
        content = line[start:end].strip()
        if content:
            segments.append((speaker, content))
    return segments


def find_transcript_start(lines):
    in_frontmatter = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter and stripped == "---":
            in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        heading_text = stripped.strip("# ").strip().lower()
        if heading_text in TRANSCRIPT_HEADINGS:
            return i, True
    for i, line in enumerate(lines):
        if re.match(r"^(Travis Dockter|[A-Za-z][A-Za-z0-9 ._-]{1,40}):\s*", line):
            return i, False
    return None, False


def normalize_file(path: Path):
    lines = path.read_text().splitlines()
    start, has_heading = find_transcript_start(lines)
    if start is None:
        return False

    pre = lines[:start]
    body = lines[start + 1:] if has_heading else lines[start:]
    speakers = collect_speakers(body)

    output = pre[:]
    while output and output[-1] == "":
        output.pop()
    output.extend(["", "## Transcript", ""])

    blocks = []
    current_speaker = None
    current_parts = []

    def flush():
        nonlocal current_speaker, current_parts
        if current_speaker and current_parts:
            text = clean_text(" ".join(current_parts))
            if text:
                blocks.append((current_speaker, text))
        current_speaker = None
        current_parts = []

    for raw in body:
        line = raw.strip()
        if not line:
            continue
        if line.strip("# ").strip().lower() in TRANSCRIPT_HEADINGS:
            continue
        for speaker, content in split_speaker_segments(line, speakers):
            content = clean_text(content)
            if not content:
                continue
            if speaker is None:
                if current_speaker:
                    current_parts.append(content)
                else:
                    # Keep unattributed text rather than guessing.
                    blocks.append((None, content))
                continue
            if current_speaker == speaker:
                current_parts.append(content)
            else:
                flush()
                current_speaker = speaker
                current_parts = [content]
    flush()

    for speaker, text in blocks:
        if speaker:
            output.append(f"**{speaker}:** {text}")
        else:
            output.append(text)
        output.append("")

    path.write_text("\n".join(output).rstrip() + "\n")
    return True


def main(argv):
    if not argv:
        print("Usage: normalize_interview_transcripts.py FILE [FILE ...]", file=sys.stderr)
        return 1
    for name in argv:
        path = Path(name)
        if normalize_file(path):
            print(f"normalized {path}")
        else:
            print(f"skipped {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
