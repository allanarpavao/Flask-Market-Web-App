from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="username")
    email_address = StringField(label="email_address")
    password1 = PasswordField(label="password1")
    password2 = PasswordField(label="password2") #validate that both passwords match
    submit = SubmitField(label="submit")