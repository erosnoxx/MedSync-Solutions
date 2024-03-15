from app.controllers.extensions import db
from app.models.personal.patients import Patients, PatientUser
from app.models.personal.schedule import Schedule


def DeletePatient(patient_id):
    patient = Patients.query.filter_by(id=patient_id).first()

    if patient is not None:
        db.session.delete(patient)
        db.session.commit()

    return bool(patient)


def DeleteSchedule(schedule_id):
    schedule = Schedule.query.filter_by(id=schedule_id).first()

    if schedule is not None:
        db.session.delete(schedule)
        db.session.commit()

    return bool(schedule)


def DeletePatientUser(id):
    patient = PatientUser.query.filter_by(id=id).first()

    if patient is not None:
        db.session.delete(patient)
        db.session.commit()

    return bool(patient)
