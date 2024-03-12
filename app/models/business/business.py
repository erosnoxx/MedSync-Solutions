from app.controllers.extensions import db


class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True)
    business = db.Column(db.String(255), nullable=False)

    # Relationships
    drs = db.relationship('Doctors', backref='business')
    employees = db.relationship('Employees', backref='employees')


class Doctors(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'),
                            nullable=False)


class Employees(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'),
                            nullable=False)
