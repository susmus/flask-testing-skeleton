class Config(object):
    SECRET_KEY = 'secret'
    BUNDLE_ERRORS = True

class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000

class DebugConfig(Config):
    DEBUG = True
    TESTING = False
    USE_RELOADER = True
    HOST = '0.0.0.0'
    PORT = 5000
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    USE_RELOADER = False
    HOST = '127.0.0.1'
    PORT = 8943
