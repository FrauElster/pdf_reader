import os
import logging

LOGGER = logging.getLogger(__name__)


def to_file_path(file_name: str) -> str:
    """ :returns an existing absolute file path based on the project root directory + file_name"""
    package_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(package_directory, '..', file_name)
    return path


def save_file(file_name: str, data: str) -> None:
    """ writes a file, if a file with file_name already exists its content gets overwritten """
    dir_path:str = to_file_path('out')
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        LOGGER.info('created "out" directory')

    file_path: str = os.path.join(dir_path, file_name)
    with open(file_path, 'w') as file:
        file.write(data)
    LOGGER.info(f'saved {file_name}')
