from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password:", validators=[EqualTo('password'), DataRequired()]) #validate that both passwords match
    submit = SubmitField(label="Create Account")