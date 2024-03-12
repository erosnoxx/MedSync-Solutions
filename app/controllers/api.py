from app.api.v1.auth.user import auth_api


def init_app(app):
    app.register_blueprint(auth_api)
