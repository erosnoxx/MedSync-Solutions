from wtforms.fields import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import Email, Length, DataRequired
from flask_wtf.file import FileAllowed
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):

    name = StringField('name', validators=[DataRequired(), Length(min=5, max=255)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=255)])
    profile_pic = FileField('profile_pic', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Apenas imagens são permitidas.')])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=255)])
    submit = SubmitField('submit')