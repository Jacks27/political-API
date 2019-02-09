import os


class DevConfig:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(DevConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

class StagingConfig(DevConfig):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(DevConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}