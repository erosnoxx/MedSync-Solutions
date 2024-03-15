from app.api.v1.auth.user import auth_api
from app.api.v1.patients.patients import patient_api


def init_app(app):
    app.register_blueprint(auth_api)
    app.register_blueprint(patient_api)
