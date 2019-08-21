# PDF READER

##Description

This Script tries to convert PDF from the `res` directory. It first to just decode them, but if that's not possible, 
e.g. due scanned documents, it tries to OCR them. Currently supported are english and german. You can add more OCR 
trainingsdata by adding them from `https://github.com/tesseract-ocr/tessdata` into the `tessdata` folder.

The output text is then put in the `out` directory.

There is a logfile created with further details to each run, see `pdf_reader.log`

## Setup
Install python packages with `pip install -r requirements.txt`

Install *"tesseract-ocr"* with `sudo apt-get install tesseract-ocr`.
Or for windows: `https://github.com/UB-Mannheim/tesseract/wiki`

## Usage

Put all your PDFs into the `res` directory within the project root.

Change directory to the project root and run `python -m pdf-reader`. This will take some time, depending on the amount 
of PDFs and how many of them have to be recognized via OCR, which is pretty intensive calculating.

If all is done, the recognized/decoded texts are in the `out` directory.