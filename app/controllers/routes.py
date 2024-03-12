from app.blueprints.auth.auth_bp import auth
# from app.blueprints.home.home_bp import home

def init_app(app):
    app.register_blueprint(auth)
    # app.register_blueprint(home)