from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = StringField("Password:", validators = [DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = StringField("Password:", validators = [DataRequired()])
    submit = SubmitField("Login")

class MemeForm(FlaskForm):
    submit = SubmitField("Login")