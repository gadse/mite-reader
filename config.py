import configparser

from main import CONFIG_FILE_PATH, AUTH_SECTION_KEY


def read():
    """
    Reads the config.ini

    Returns (dict):
        The config as a dict.

    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)

    return config


def auth_info():
    return dict(read()[AUTH_SECTION_KEY])