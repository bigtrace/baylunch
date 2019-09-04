import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'caia.bigtrace@gmail.com'
    MAIL_PASSWORD = '123' #os.environ.get('EMAIL_PASS')
    RECAPTCHA_USE_SSL= False
    RECAPTCHA_PUBLIC_KEY='6Leg-qsUAAAAANLxfagFF0ODbEDSH3cEwc3Ll4TE'
    RECAPTCHA_PRIVATE_KEY='6Leg-qsUAAAAAA7bukfUttDw-6Csc46WGeAEit0H'
    RECAPTCHA_OPTIONS= {'theme':'black'}