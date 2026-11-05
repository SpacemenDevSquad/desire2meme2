from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Optional, EqualTo

class SignUpForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = PasswordField("Password:", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password:", validators = [DataRequired(), EqualTo("password", "Must Match Your Chosen Password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = PasswordField("Password:", validators = [DataRequired()])
    submit = SubmitField("Login")

class MemeForm(FlaskForm):
    title = StringField("Title:", validators = [DataRequired()])
    image = FileField("Upload an Image:", validators = [FileRequired(), FileAllowed(["jpg", "jpeg", "png"])])
    fabric = StringField("Fabric JSON:", validators = [Optional()])
    caption = StringField("Caption:", validators = [Optional()])
    submit = SubmitField("Login")