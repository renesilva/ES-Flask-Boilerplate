from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

# Basic Auth
basic_auth_auth = HTTPBasicAuth()
basic_auth_users = {
    os.getenv("USER_1"): generate_password_hash(os.getenv("PASSWORD_1")),
}
