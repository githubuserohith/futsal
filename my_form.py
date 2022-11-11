from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, SelectField, \
    DateField, TimeField, RadioField, BooleanField

from wtforms.fields.datetime import DateTimeLocalField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class Login(FlaskForm):
    username = StringField('Username',
                           validators=[
                               Length(min=2, max=50),
                           ])

    password = PasswordField('Password')
    submit_login = SubmitField('Login')
    submit_login_otp = SubmitField('Login with otp')
    submit_signup = SubmitField('Sign in')
    rem_pwd = BooleanField()
    gender = RadioField()


class Login_otp(FlaskForm):
    email_add = StringField('Enter Username/Email', validators=[DataRequired()])
    send_otp = SubmitField('Send otp')
    otp = StringField('Enter otp', default='0000')
    verify_otp = SubmitField('Verify otp')


class Signup(FlaskForm):
    username1 = StringField('Email address',
                            validators=[Length(min=2, max=50)])

    password1 = PasswordField('Choose password')
    confirmpwd = PasswordField('Confirm Password')
    submit_signup1 = SubmitField('Sign in')
    submit_login1 = SubmitField('Login')


class Book(FlaskForm):
    slot_date = DateField()
    slot_time = TimeField()
    submit_booking = SubmitField('Check availability')
    confirm_booking = SubmitField('Book slot')


class Admin(FlaskForm):
    pass


class Logout(FlaskForm):
    pass
