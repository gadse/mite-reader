import configparser


CONFIG_FILE_PATH = "config.ini"
AUTH_SECTION_KEY = "auth"


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