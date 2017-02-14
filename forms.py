from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("Please enter your First Name.")])
    last_name = StringField('Last Name', validators=[DataRequired("Please enter your Last Name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email. name@host.com")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min = 6, message = "Passwords must be at least 6 characters in length.")])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email. name@host.com")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField("Sign In")