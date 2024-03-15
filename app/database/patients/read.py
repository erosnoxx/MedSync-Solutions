from app.controllers.extensions import db
from app.models.personal.patients import Patients
from app.models.personal.schedule import Schedule


def GetPatient(patient_cpf):
    patient = Patients.query.filter_by(cpf=patient_cpf).first()
    return patient if patient is not None else False


def GetAllPatients():
    patients = Patients.query.all()
    return patients if patients is not None else False


def GetPatientSchedule(patient_id):
    patient_schedule = Schedule.query.filter_by(patient_id=patient_id)
    return patient_schedule if patient_schedule is not None else False


def GetSchedule(dr_id):
    schedule = Schedule.query.all(dr_id=dr_id)
    return schedule if schedule is not None else False
