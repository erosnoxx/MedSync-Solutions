from app.controllers.extensions import db
from app.models.personal.patients import Patients, PatientUser
from app.models.personal.schedule import Schedule
from app.database.users.create import SetUser, SetUserLevel, SetProfilePic


def SetPatient(**kwargs):
    patient = Patients.query.filter_by(cpf=kwargs['cpf']).first()

    if patient is None:
        patient = Patients(**kwargs)

        db.session.add(patient)
        db.session.commit()

        return patient.id
    
    return None


def SetPatientUser(**kwargs):
    patient_user = PatientUser(
        patient_user=kwargs['patient_id'],
        user_id=kwargs['user_id']
    )
    db.session.add(patient_user)
    db.session.commit()

    return patient_user.user_id


def SetSchedule(**kwargs):
    schedule = Schedule.query.filter_by(date=kwargs['date']).first()
    if schedule is None:
        schedule = Schedule(**kwargs)

        db.session.add(schedule)
        db.session.commit()

        return schedule.id
    return None


def CreatePatient(**kwargs):
    data = kwargs
    patient = SetPatient(
        dr_id=data['dr_id'],
        name=data['name'],
        social_name=data['social_name'],
        cpf=data['cpf'],
        age=data['age'],
        escort=data['escort']
    )

    if patient is not None:
        user = SetUser(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        if user is not None:
            SetUserLevel(level_='pat', user_id=user)
            SetPatientUser(patient_id=patient, user_id=user)

            return {'success': True, 'user_id': user, 'patient_id': patient}
        return {'success': False, 'message': 'user already exists'}
    return {'success': False, 'message': 'patient already exists'}