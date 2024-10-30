from flask import render_template
from app import app
from werkzeug.security import check_password_hash
from app.auth.basic_auth.basic_auth import basic_auth_auth, basic_auth_users


@basic_auth_auth.verify_password
def verify_password(username, password):
    if username in basic_auth_users and \
            check_password_hash(basic_auth_users.get(username), password):
        return username


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login-required')
@basic_auth_auth.login_required
def login_required():
    return render_template('login-required.html')
