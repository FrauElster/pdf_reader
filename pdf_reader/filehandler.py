import os
import logging
import shutil

LOGGER = logging.getLogger(__name__)


def to_file_path(file_name: str) -> str:
    """ :returns an existing absolute file path based on the project root directory + file_name"""
    package_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(package_directory, '..', file_name)
    return path


def create_dir(dir_name: str) -> str:
    """
    creates a directory if it is not already exiting
    :param dir_name: directory name
    :return: the absolute path to the directory
    """
    dir_path: str = to_file_path(dir_name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        LOGGER.info(f'created {dir_name} directory')

    return dir_path


def delete_dir(dir_name: str) -> bool:
    """
    deletes a directory if it exists
    :param dir_name: directory name
    :return: whether it exists or not
    """
    dir_path: str = to_file_path(dir_name)
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path, ignore_errors=True)
        LOGGER.info(f'Removed directory "{dir_name}"')
        return True
    if not os.path.exists(dir_path):
        LOGGER.warning(f'"{dir_name}" does not exists')
    else:
        LOGGER.warning(f'"{dir_name}" is not a directory')
    return False


def save_file(file_name: str, data: str) -> None:
    """ writes a file, if a file with file_name already exists its content gets overwritten """
    dir_path: str = create_dir(dir_name='out')
    file_path: str = os.path.join(dir_path, file_name)
    if os.path.isfile(file_path):
        LOGGER.warning(f'{file_path} already exists. Will be overwritten...')
    with open(file_path, 'w') as file:
        file.write(data)
    LOGGER.info(f'saved {file_name}')
