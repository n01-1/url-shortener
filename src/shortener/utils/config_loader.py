import json
import os


def load_config_directory(config_directory, environment):
    config = {}
    _config_file_default_path = os.path.join(config_directory, 'base.json')
    _config_file_env_path = os.path.join(config_directory, environment.lower() + '.json')
    _config_file_local_path = os.path.join(config_directory, 'local.json')

    if os.path.isfile(_config_file_default_path):
        with open(_config_file_default_path) as config_file:
            config.update(json.load(config_file))

    if os.path.exists(_config_file_env_path):
        with open(_config_file_env_path) as config_file:
            config.update(json.load(config_file))

    if os.path.exists(_config_file_local_path):
        with open(_config_file_local_path) as config_file:
            config.update(json.load(config_file))

    return config
