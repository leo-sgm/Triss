'''
Module for some additional fucntions
'''

import json
import os


def list_available_commands(path):
    '''Return list available commands stored at the `path`'''
    return os.listdir(path)


def create_dir_for_path(path):
    '''Check and create dirs (!) if not exists'''
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def save_config(config, path='~/.Triss/config.json'):
    '''Save config in file by path as json'''
    create_dir_for_path(path)
    with open(path, 'w') as file:
        print(json.dumps(config, indent=4, sort_keys=True), file=file)
