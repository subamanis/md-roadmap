import argparse
import html
import pathlib
import re
import sys

VIEWER = pathlib.Path(__file__).with_name("roadmap.html")
SOURCE_TAG = re.compile(r'<script id="roadmap-source" type="text/markdown"[^>]*>.*?</script>', re.S)


def main():
    parser = argparse.ArgumentParser(description="Write a copy of roadmap.html that opens with a markdown file inside it.")
    parser.add_argument("markdown", type=pathlib.Path, help="the markdown file")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="the HTML file to write, the markdown path with .html by default")
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8")
    tag = create_source_tag(text, args.markdown.name)
    page, count = SOURCE_TAG.subn(lambda _: tag, VIEWER.read_text(encoding="utf-8"))
    if count != 1:
        sys.exit(f"{VIEWER} holds {count} source tags, expected 1")

    output = args.output or args.markdown.with_suffix(".html")
    output.write_text(page, encoding="utf-8", newline="\n")
    print(output)


def create_source_tag(text, name):
    escaped = re.sub(r"</(script)", r"<\\/\1", text, flags=re.I).replace("<!--", "<\\!--")
    return f'<script id="roadmap-source" type="text/markdown" data-name="{html.escape(name)}">\n{escaped}\n</script>'


if __name__ == "__main__":
    main()
