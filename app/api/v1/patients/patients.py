from flask import Blueprint, request
from app.models.personal.patients import Patients
from app.database.patients.create import CreatePatient, SetSchedule
from app.database.users.read import IsADoctor
from app.services.utils.generators import generate_patient_pwd
from app.services.utils.validators import EmailValidator

patient_api = Blueprint('patient_api', __name__, url_prefix='/api/v1/patient')


@patient_api.post('/add/')
def add():
    data = request.json

    required_fields = ['dr_id', 'name', 'social_name', 'cpf', 'age', 'escort',
                       'email', 'date']

    if not all(field in data for field in required_fields):
        return {'message': 'missing required fields', 'statuscode': 400}, 400

    if not IsADoctor(data['dr_id']):
        return {'message': 'invalid dr_id', 'statuscode': 400}, 400

    if not EmailValidator(data['email']):
        return {'message': 'invalid email', 'statuscode': 400}, 400

    patient = Patients.query.filter_by(cpf=data['cpf']).first()

    if patient:
        return {'message': 'patient already exists', 'statuscode': 400}, 400

    pwd = generate_patient_pwd()
    pat_data = CreatePatient(
        **{
            'dr_id': data['dr_id'],
            'name': data['name'],
            'social_name': data['social_name'],
            'cpf': data['cpf'],
            'age': data['age'],
            'escort': data['escort'],
            'email': data['email'],
            'password': pwd
        }
    )

    if not pat_data['success']:
        return {'message': pat_data['message'], 'statuscode': 400}, 400

    schedule = SetSchedule(
        **{
            'dr_id': data['dr_id'],
            'dr_id': pat_data['user_id'],
            'patient_id': pat_data['patient_id'],
            'date': data['date']
        }
    )

    if schedule is None:
        return {
            'message': 'busy schedule',
            'statuscode': 400
        }, 400

    return {
        'message': 'patient registered successfully',
        'user_id': pat_data['user_id'],
        'patient_id': pat_data['patient_id'],
        'schedule_id': schedule,
        'pwd': pwd,
        'statuscode': 200
    }, 200
