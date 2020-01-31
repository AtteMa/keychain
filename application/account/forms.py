from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf=False

class AccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    username = StringField("Username", [validators.Length(min=1)])
    password = PasswordField("Password", [validators.InputRequired(),
                validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Repeat password")

    class Meta:
        csrf=False