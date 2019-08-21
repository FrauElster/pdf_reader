# PDF READER

##Description

This Script tries to convert PDF from the `res` directory. It first to just decode them, but if that's not possible, 
e.g. due scanned documents, it tries to OCR them. 

The output text is then put in the `out` directory.

There is a logfile created with further details to each run, see `pdf_reader.log`

## Setup

Install python packages with `pip install -r requirements.txt`

Install *"tesseract-ocr"* with `sudo apt-get install tesseract-ocr`.
Or for windows: `https://github.com/UB-Mannheim/tesseract/wiki`