from app.controllers.extensions import db
from app.models.personal.patients import Patients
from app.models.personal.schedule import Schedule


def DeletePatient(patient_cpf):
    patient = Patients.query.filter_by(cpf=patient_cpf).first()

    if patient is not None:
        db.session.delete(patient)
        db.session.commit()

    return bool(patient)


def DeletePatientSchedule(patient_id):
    patient = Patients.query.filter_by(id=patient_id).first()
    
    if patient is not None:
        db.session.delete(patient)
        db.session.commit()
    
    return bool(patient)
