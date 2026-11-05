from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Optional

class SignUpForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = StringField("Password:", validators = [DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username:", validators = [DataRequired()])
    password = StringField("Password:", validators = [DataRequired()])
    submit = SubmitField("Login")

class MemeForm(FlaskForm):
    title = StringField("Title:", validators = [DataRequired()])
    image = FileField("Upload an Image:", validators = [FileRequired(), FileAllowed(["jpg", "jpeg", "png"])])
    fabric = StringField("Fabric JSON:", validators = [Optional()])
    caption = StringField("Caption:", validators = [Optional()])
    submit = SubmitField("Login")