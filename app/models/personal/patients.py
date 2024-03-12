from app.services.utils.generators import get_now
from app.controllers.extensions import db


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    social_name = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    mar_status = db.Column(db.String(15), nullable=False)
    occupation = db.Column(db.String(255), nullable=False)
    education = db.Column(db.String(255), nullable=False)
    health_insurance = db.Column(db.String(255), nullable=False)
    escort = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=get_now, nullable=False)
    # Relationships
    general_info = db.relationship('GeneralInfo', backref='patient')
    preg_info = db.relationship('PregInfo', backref='patient')
    blood_type = db.relationship('BloodType', backref='patient')
    vaccines = db.relationship('Vaccines', backref='patient')
    gest_age = db.relationship('GestAge', backref='patient')
    follow_history = db.relationship('FollowHistory', backref='patient')


class GeneralInfo(db.Model):
    __tablename__ = 'general_info'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    dr_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    height = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    weight = db.Column(db.Numeric(precision=5, scale=2), nullable=False)
    imc = db.Column(db.Numeric(precision=5, scale=2), nullable=False)


class PregInfo(db.Model):
    __tablename__ = 'preg_info'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    pregnancies = db.Column(db.Integer, nullable=False)
    normal_birth = db.Column(db.Integer, nullable=False)
    cesarean_births = db.Column(db.Integer, nullable=False)
    mole = db.Column(db.Integer, nullable=False)
    abortions = db.Column(db.Integer, nullable=False)
    ectopic = db.Column(db.Integer, nullable=False)


class BloodType(db.Model):
    __tablename__ = 'blood_type'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    maternal = db.Column(db.String(5), nullable=False)
    paternal = db.Column(db.String(5), nullable=False)
    m_hemoglobin = db.Column(db.Numeric(precision=3, scale=2), nullable=False)
    p_hemoglobin = db.Column(db.Numeric(precision=3, scale=2), nullable=False)


class Vaccines(db.Model):
    __tablename__ = 'vaccines'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    tetanus = db.Column(db.Boolean, nullable=False)
    whooping_cough = db.Column(db.Boolean, nullable=False)
    hepatitis = db.Column(db.Boolean, nullable=False)
    influenza = db.Column(db.Boolean, nullable=False)
    covid_19 = db.Column(db.Boolean, nullable=False)


class GestAge(db.Model):
    __tablename__ = 'gest_age'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    last_period = db.Column(db.DateTime, default=get_now, nullable=False)
    ga_chrono = db.Column(db.String(5))
    birth_prev = db.Column(db.DateTime, default=get_now, nullable=False)
    first_ultrasound = db.Column(db.DateTime, default=get_now, nullable=False)
    ga_first_ultrasound = db.Column(db.String(5))
    echo_birth_prev = db.Column(db.DateTime, default=get_now, nullable=False)


class FollowHistory(db.Model):
    __tablename__ = 'follow_history'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    dr_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=get_now, nullable=False)
    ga_chrono = db.Column(db.String(5), nullable=False)
    ga_echo = db.Column(db.String(5), nullable=False)
    weight = db.Column(db.Numeric(precision=5, scale=2), nullable=False)
    gain = db.Column(db.Integer, nullable=False)
    blood_pressure = db.Column(db.String(10), nullable=False)
    uterine_height = db.Column(db.Integer, nullable=False)
    fetal_heartbeat = db.Column(db.Integer, nullable=False)
    edema = db.Column(db.Integer, nullable=False)
    show = db.Column(db.String(15), nullable=False)
    assessment = db.Column(db.Text, nullable=False)
    conduct = db.Column(db.Text, nullable=False)