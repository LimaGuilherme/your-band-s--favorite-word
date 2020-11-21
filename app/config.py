#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from importlib import import_module

from app import exceptions


class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    ENVIRONMENT = None
    SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
    SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
    ELASTICSEARCH_HOST = os.environ['ELASTICSEARCH_HOST']
    ELASTICSEARCH_PORT = os.environ['ELASTICSEARCH_PORT']
    GENIUS_ACCESS_TOKEN = os.environ['GENIUS_ACCESS_TOKEN']

    def __init__(self):
        if self.ENVIRONMENT is None:
            raise TypeError('You should use one of the specialized config class')


class ProductionConfig(Config):
    ENVIRONMENT = 'production'


class DevelopmentConfig(Config):
    ENVIRONMENT = 'development'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True


class TestingConfig(DevelopmentConfig):
    ENVIRONMENT = 'test'
    TESTING = True


def get_config():
    config_imports = os.environ['APP_SETTINGS'].split('.')
    config_class_name = config_imports[-1]
    config_module = import_module('.'.join(config_imports[:-1]))
    config_class = getattr(config_module, config_class_name, None)
    if not config_class:
        raise exceptions.ConfigClassNotFound('Unable to find a config class in {}'.format(os.environ['APP_SETTINGS']))
    return config_class()
