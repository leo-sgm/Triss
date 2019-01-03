'''
Module for some additional fucntions
'''

import json
import os


def create_dir_for_path(path):
    '''Check and create dir if not exist'''
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def save_config(config, path='~/.Triss/config.json'):
    '''Save config in file by path as json'''
    create_dir_for_path(path)
    with open(path, 'w') as file:
        print(json.dumps(config, indent=4, sort_keys=True), file=file)
