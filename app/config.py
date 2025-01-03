import os

from dotenv import load_dotenv

load_dotenv()

# postgres_user = os.getenv('POSTGRES_USER')
# postgres_password = os.getenv('POSTGRES_PASSWORD')
# postgres_host = os.getenv('POSTGRES_HOST')
# postgres_db = os.getenv('POSTGRES_DB')


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    file_path = os.path.abspath(os.getcwd()) + "/data_db/database.sqlite"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path

    # SQLALCHEMY_DATABASE_URI = (
    #         'postgresql://' + postgres_user + ':' + postgres_password + '@' + postgres_host + '/' + postgres_db)
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
