from pprint import pprint

import config
import mite

CONFIG_FILE_PATH = "config.ini"
AUTH_SECTION_KEY = "auth"


def main():
    pprint(config.auth_info())
    pprint(mite.get_base_info())


if __name__ == "__main__":
    main()


