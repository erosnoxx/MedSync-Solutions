from app.services.utils.generators import get_now
from app.controllers.extensions import db
from app.models.personal.users import User


# Register
class Patients(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    dr_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    name = db.Column(db.String(255), nullable=False)
    social_name = db.Column(db.String(255), default='', nullable=False)
    age = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    escort = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=get_now, nullable=False)

    # Relationships
    patient_info = db.relationship('PatientInfo', backref='patients')
    patient_preg_info = db.relationship('PatientPregInfo', backref='patients')
    baby_info = db.relationship('BabyInfo', backref='patients')
    blood_type = db.relationship('BloodType', backref='patients')
    vaccines = db.relationship('Vaccines', backref='patients')
    history = db.relationship('History', backref='patients')


# Record
class PatientInfo(db.Model):
    __tablename__ = 'patient_info'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)


class PatientPregInfo(db.Model):
    __tablename__ = 'patient_preg_info'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    last_period = db.Column(db.Date, nullable=False)
    babys = db.Column(db.Integer, default=1, nullable=False)
    pregnancies = db.Column(db.Integer, default=0, nullable=False)
    normal = db.Column(db.Integer, default=0, nullable=False)
    cesarean = db.Column(db.Integer, default=0, nullable=False)
    mola = db.Column(db.Integer, default=0, nullable=False)
    abortions = db.Column(db.Integer, default=0, nullable=False)
    ectopic = db.Column(db.Integer, default=0, nullable=False)


class BabyInfo(db.Model):
    __tablename__ = 'baby_info'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    name = db.Column(db.String(255), nullable=True)
    sex = db.Column(db.Boolean, nullable=True)


class BloodType(db.Model):
    __tablename__ = 'blood_type'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    maternal_bt = db.Column(db.String(5), nullable=False)
    paternal_bt = db.Column(db.String(5), nullable=True)
    maternal_hm = db.Column(db.Float, default=0.00, nullable=False)
    paternal_hm = db.Column(db.Float, default=0.00, nullable=True)


class Vaccines(db.Model):
    __tablename__ = 'vaccines'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    tetanus = db.Column(db.Boolean, default=False, nullable=False)
    pertussis = db.Column(db.Boolean, default=False, nullable=False)
    hepatitis = db.Column(db.Boolean, default=False, nullable=False)
    influenza = db.Column(db.Boolean, default=False, nullable=False)
    covid19 = db.Column(db.Boolean, default=False, nullable=False)


class GestAge(db.Model):
    __tablename__ = 'gest_age'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    first_us = db.Column(db.Date, nullable=True)
    ga_first_us = db.Column(db.String(10), nullable=True)


class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Numeric(precision=5, scale=2), nullable=False)
    gain = db.Column(db.Integer, nullable=False)
    blood_pressure = db.Column(db.String(10), nullable=False)
    uterine_height = db.Column(db.Integer, nullable=False)
    fetal_heartbeat = db.Column(db.Integer, nullable=False)
    edema = db.Column(db.Integer, nullable=False)
    show = db.Column(db.String(30), nullable=False)
    assessment = db.Column(db.Text, nullable=False)
    conduct = db.Column(db.Text, nullable=False)
