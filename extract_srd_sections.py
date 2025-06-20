"""Extract sections from SRD_CC_v5.2.1.pdf and write them to HTML files.

Requires the PyPDF2 package::

    pip install PyPDF2

The page ranges in SECTIONS must be updated to match the
corresponding section positions in the PDF.
"""
from pathlib import Path
import PyPDF2

PDF_FILE = Path("SRD_CC_v5.2.1.pdf")

# Mapping of output HTML files to (start_page, end_page) ranges.
# Page numbers are 1-indexed and the end page is inclusive.
SECTIONS = {
    "legal.html": (1, 3),              # TODO: update page ranges
    "playing-the-game.html": (4, 28),   # TODO
    "character-creation.html": (29, 50),# TODO
    "classes.html": (51, 80),           # TODO
    "character-origins.html": (81, 100),# TODO
    "feats.html": (101, 120),           # TODO
    "equipment.html": (121, 140),       # TODO
    "spells.html": (141, 180),          # TODO
    "rules-glossary.html": (181, 200),  # TODO
    "gameplay-toolbox.html": (201, 220),# TODO
    "magic-items.html": (221, 240),     # TODO
    "monsters.html": (241, 260),        # TODO
    "monsters-a-z.html": (261, 280),    # TODO
    "animals.html": (281, 290),         # TODO
    "stat-block-index.html": (291, 300) # TODO
}

HEADER = """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>{title}</title>
</head>
<body>
<header>
  <h1>{title}</h1>
</header>
<main>
"""

FOOTER = """
</main>
<footer>
  <p>
    This work includes material from the
    <em>System Reference Document 5.2.1 (“SRD 5.2.1”)</em> by Wizards of the Coast LLC,
    available at
    <a href='https://www.dndbeyond.com/srd' target='_blank' rel='noopener'>
      dndbeyond.com/srd
    </a>.
    The SRD 5.2.1 is licensed under the
    <a href='https://creativecommons.org/licenses/by/4.0/legalcode' target='_blank' rel='noopener'>
      Creative Commons Attribution 4.0 International License
    </a>.
  </p>
  <p>
    <a href='https://creativecommons.org/licenses/by/4.0/' target='_blank' rel='noopener'>
      <img src='https://mirrors.creativecommons.org/presskit/icons/cc.svg' alt='Creative Commons' height='22' />
      <img src='https://mirrors.creativecommons.org/presskit/icons/by.svg' alt='Attribution' height='22' />
    </a>
  </p>
</footer>
</body>
</html>
"""

def extract_section(reader, start, end):
    """Return text for pages start..end inclusive."""
    text_chunks = []
    for page_num in range(start - 1, end):
        if page_num >= len(reader.pages):
            break
        page = reader.pages[page_num]
        text_chunks.append(page.extract_text() or "")
    return "\n".join(text_chunks)

def main():
    if not PDF_FILE.exists():
        raise SystemExit(f"PDF file {PDF_FILE} not found")
    with PDF_FILE.open('rb') as f:
        reader = PyPDF2.PdfReader(f)
        for filename, (start, end) in SECTIONS.items():
            title = filename.replace("-", " ").replace(".html", "").title()
            text = extract_section(reader, start, end)
            with open(filename, 'w', encoding='utf-8') as out:
                out.write(HEADER.format(title=title))
                out.write('<pre>\n')
                out.write(text)
                out.write('\n</pre>')
                out.write(FOOTER)

if __name__ == '__main__':
    main()
