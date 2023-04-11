# -*- coding: UTF-8 -*-

import configparser

DEFAULT_SECTION = "default"

if __name__ == '__main__':
    import os

    config = configparser.RawConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
    with open(config_path, 'r') as f:
        config_string = f'[{DEFAULT_SECTION}]\n' + f.read()
    config.read_string(config_string)
    print(config.get(DEFAULT_SECTION, "aaa"))