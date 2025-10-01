def init_app(app):
    from .test import test_bp
    from .todo import todo_bp
    from .jwt_auth import jwt_auth_bp
    app.register_blueprint(test_bp)
    app.register_blueprint(todo_bp)
    app.register_blueprint(jwt_auth_bp)
    return app
