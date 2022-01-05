from functools import lru_cache
import os

import yaml

DEFAULT_CONFIG_FOLDER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'config'
)

DEFAULT_ASSET_FOLDER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'assets'
)

CONFIG_FOLDER = os.environ.get('PLAYGROUNDS_CONFIG_FOLDER', DEFAULT_CONFIG_FOLDER)
ASSET_FOLDER = os.environ.get('PLAYGROUNDS_ASSET_FOLDER', DEFAULT_ASSET_FOLDER)


@lru_cache(maxsize=None)
def load_config():
    '''
    Load YAML file representing application configuration based on the
    `PLAYGROUNDS_CONFIG` environment variable
    '''
    # TODO: make this a required environment variable instead of using a default value
    config_file = os.environ.get('PLAYGROUNDS_CONFIG', 'olympus.yaml')

    config_path = os.path.join(CONFIG_FOLDER, config_file)

    with open(config_path, 'r') as f:
        config_yaml = yaml.safe_load(f.read())

    return config_yaml
