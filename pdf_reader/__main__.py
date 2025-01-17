from tika import parser
import glob
import logging
import os
from typing import List

from .spinner import Spinner
from .ocr import convert
from .filehandler import to_file_path, save_file

PDF_DIR: str = to_file_path('res')
LOGGER: logging.Logger = logging.getLogger("pdf_reader")


def main() -> None:
    """
    Main entry point
    :return:
    """
    setup_logger()
    pdfs: List[str] = get_pdfs(PDF_DIR)
    if not pdfs:
        exit(1)
    with Spinner():
        _convert_pdfs(pdfs)


def _convert_pdfs(pdfs: List[str]) -> None:
    """
    converts the pdfs, so it does the main job
    :param pdfs: the pdf paths
    :return:
    """
    for pdf in pdfs:
        filename: str = f'{pdf.split(".")[-2]}.txt'.split(os.sep)[-1]

        raw: str = parser.from_file(pdf)
        if raw['content']:
            save_file(file_name=filename, data=raw['content'].strip())
            LOGGER.info(f'Decoded "{pdf}"')
        else:
            # PDF was not readable: trigger OCR
            LOGGER.info(f'"{pdf}" was not decodable, start OCR...')
            text: str = convert(pdf)
            if not text:
                exit(1)
            save_file(file_name=filename, data=text)


def setup_logger() -> None:
    """
    setup for the various handler for logging
    :return:
    """
    LOGGER.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s \t|%(asctime)s \t| %(name)s \t|  %(message)s')

    file_handler: logging.FileHandler = logging.FileHandler(to_file_path('pdf_reader.log'), mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler: logging.StreamHandler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    LOGGER.addHandler(file_handler)
    LOGGER.addHandler(console_handler)
    LOGGER.info('Filehandler and Console_Handler were born, let\'s start logging')


def get_pdfs(dir: str) -> List[str]:
    """
    returns the filepaths of all pdf files in the givven directory. Not recursively
    :param: dir the directory to loop over
    :return: a list of all file paths
    """
    if not os.path.exists(dir):
        LOGGER.error(f'Directory "{dir}" not found')
        return []
    elif not os.path.isdir(dir):
        LOGGER.error(f'"{dir}" is not a directory')
        return []

    pdfs: List[str] = []
    os.chdir(dir)
    for file in glob.glob("*.pdf"):
        pdfs.append(to_file_path(f'res/{file}'))

    if not pdfs:
        LOGGER.warning(f"No PDFs found in {dir}")
    else:
        LOGGER.info(f'PDFs found: {pdfs}')
    return pdfs


if __name__ == '__main__':
    main()
