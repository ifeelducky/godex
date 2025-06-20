# godex

Godex provides a browsable HTML5 version of the open Dungeons & Dragons SRD 5.2.1.
The repository includes the official PDF (`SRD_CC_v5.2.1.pdf`) and scripts to
extract each section into individual HTML files.

## Generating pages

1. Install the required Python dependency:
   ```bash
   pip install PyPDF2
   ```
2. Adjust the page ranges in `extract_srd_sections.py` to match the start and
   end page numbers for each section of the SRD.
3. Run the script to generate the HTML files:
   ```bash
   python3 extract_srd_sections.py
   ```

Placeholder pages are already checked in. Running the script will replace those
files with the extracted text from the PDF.
