# config.py

class Config(object):
    """ 

    Common Configurations

    """
    DEBUG = True

class DevelopmentConfig(Config):
   
    """ 

    Development Configurations

    """

    #DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):

    """ 

    Production Configurations

    """
    
    DEBUG = False

class TestingConfig(Config):
    """ 

    Testing Configurations

    """
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}



