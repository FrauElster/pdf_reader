import logging
import os

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

from .filehandler import to_file_path, create_dir, delete_dir

LOGGER = logging.getLogger(__name__)


def convert(pdf_filename: str) -> str:
    """
    tries to convert the pdf to string via OCR
    https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
    :param pdf_filename: the filename of the pdf
    :return: the recognized text
    """
    text: str = ""
    dir_path: str = create_dir('tmp')
    if not _check_tessdata('tessdata'):
        return ''

    os.environ["TESSDATA_PREFIX"] = to_file_path('tessdata')

    convert_from_path(pdf_path=pdf_filename, dpi=500, output_folder=dir_path)
    LOGGER.debug(f'"{pdf_filename}" has {len(os.listdir(dir_path))} pages.')
    for filename in os.listdir(dir_path):
        text += str((pytesseract.image_to_string(Image.open(to_file_path(f'tmp/{filename}')))))

    delete_dir('tmp')
    if not text:
        LOGGER.warning(f'"{pdf_filename}" no text recognized')

    LOGGER.info(f'Finished OCR on "{pdf_filename}"')
    return text


def _check_tessdata(dir_name: str) -> bool:
    """
    cehcks if tessdata dir is correct
    :param dir_name:
    :return: whether its correct or not
    """
    if dir_name != 'tessdata':
        LOGGER.error(
            f'"{dir_name}" has to be "tessdata". It has to contain traindata from "https://github.com/tesseract-ocr/tessdata"')
        return False
    tessdata_dir: str = to_file_path(dir_name)
    if not os.path.exists(tessdata_dir):
        LOGGER.error(
            f'"{tessdata_dir}" is missing. It has to contain traindata from "https://github.com/tesseract-ocr/tessdata"')
        return False
    if not os.path.isdir(tessdata_dir):
        LOGGER.error(
            f'"{tessdata_dir}" is not a directory. It has to contain traindata from "https://github.com/tesseract-ocr/tessdata"')
        return False
    if len(os.listdir(tessdata_dir)) == 0:
        LOGGER.error(
            f'"{tessdata_dir}" is empty. It has to contain traindata from "https://github.com/tesseract-ocr/tessdata"')
        return False
    LOGGER.debug(f'Tessdata directory all fine!')
    return True
