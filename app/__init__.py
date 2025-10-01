from flask import Flask, render_template
from app.config import Config
from flask_jwt_extended import jwt_required
from app.auth.jwt.jwt import jwt_init

def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)
    from . import models, routes
    models.init_app(_app)
    routes.init_app(_app)
    return _app


app = create_app()

# Flask-JWT-Extended
jwt = jwt_init(app)
@app.route('/')
def index():
    return render_template('index.html')
