from app.api.v1.auth import auth_api

def init_app(app):
    app.register_api(auth_api)
    