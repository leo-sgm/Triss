'''
Module for work with config
'''

import json
import os
from sys import platform
# from pathlib import Path, PosixPath

from Triss.helper import save_config

BASE_PATH_TO_SCRIPTS = os.path.dirname(__file__) + '/scripts/'
PATH_TO_SCRIPTS = os.path.dirname(__file__) + '/scripts/' # for compatibility with old (and unfixed) code
BASE_PATH_CONFIG = '~/.Triss/config.json'

def load_config(path=BASE_PATH_CONFIG):
    '''Load config (json) from file by path'''
    return json.load(open(path))


class Config(object):
    '''Config class.
    Store where placed scripts and config-file
    '''


class BaseConfig(Config):
    '''Default config class.
    '''
    # path_to_scripts = os.path.dirname(__file__) + '/scripts/'
    path_to_scripts = '~/.Triss/scripts/'
    path_to_config = '~/.Triss/config.json'

    # for scripts with spaces in the filename
    # different behavior on each system
    # need fix when there will be a more beautiful solution
    sub_shell = True if platform == 'win32' else False

    def __init__(self, filename=path_to_config):
        try:
            self.config = load_config(filename)
        except BaseException as error:
            print('Reading config error')
            print('An exception occurred: {}'.format(error))
            self.config = {
                "path_to_scripts": self.path_to_scripts
            }
            save_config(self.config, filename)
            print('BaseConfig saved to {}'.format(filename))
        self.path_to_scripts = self.config.get('path_to_scripts')
