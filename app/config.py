class Config:
    '''
    General Configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production Configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development Configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    DEBUG = True


