import json
import os
from pathlib import Path, PosixPath

PATH_TO_SCRIPTS = os.path.dirname(__file__) + '/scripts/'

base_path_config = '~/.Triss/config.json'

def load_config(path=base_path_config):
    '''Load config (json) from file by path'''
    return json.load(open(path))
