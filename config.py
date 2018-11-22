import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:cliff@localhost/blog'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:cliff@localhost/blog'
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:cliff@localhost/blog'
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}