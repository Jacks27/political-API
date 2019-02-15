import os


class DevConfig:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    Database_Url = os.getenv("Main_Database")
    SECRET = os.getenv('SECRET')
    

class TestingConfig(DevConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    Database_Url = os.getenv("Test_Database")

class StagingConfig(DevConfig):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(DevConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    Database_Url = os.getenv("DATABASE_URL")


app_config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}