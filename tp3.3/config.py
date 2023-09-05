from dotenv import dotenv_values

class Config:
    config = dotenv_values(".env")
    
    SECRET_KEY ='clave secreta'
    SERVER_NAME ="127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = 'root'
    DATABASE_PASSWORD = 'holafa'
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = '3306'

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"