from app.controllers.extensions import db
from app.models.personal.patients import *


def SetPatient(**kwargs):
    patient = Patients(**kwargs)

    db.session.add(patient)
    db.session.commit()


def SetSchedule(**kwargs):
    pass