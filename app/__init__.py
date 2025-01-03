from flask import Flask, render_template
from app.config import Config


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)
    from . import routes
    routes.init_app(_app)
    return _app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')
