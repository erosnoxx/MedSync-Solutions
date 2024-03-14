from app.controllers.extensions import db
from app.models.personal.users import Employees
from app.models.personal.patients import Patients
from app.services.utils.generators import get_now


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    dr_id = db.Column(
        db.Integer,
        db.ForeignKey('employees.id'),
        nullable=False
    )
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    date = db.Column(db.Date, default=get_now, nullable=False)