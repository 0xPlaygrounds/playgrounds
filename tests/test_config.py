import os
from unittest import mock

from ..utils import load_config


@mock.patch.dict(os.environ, {'PLAYGROUNDS_CONFIG': 'klima.yaml'})
def test_klima_config():
    config = load_config()

    assert type(config) == dict

    assert config['protocol'] == 'Klima'
    assert config['token'] == 'KLIMA'

    load_config.cache_clear()


@mock.patch.dict(os.environ, {'PLAYGROUNDS_CONFIG': 'olympus.yaml'})
def test_olympus_config():
    config = load_config()

    assert type(config) == dict

    assert config['protocol'] == 'Olympus'
    assert config['token'] == 'OHM'

    load_config.cache_clear()
