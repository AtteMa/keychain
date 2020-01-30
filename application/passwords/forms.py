from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PasswordForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=1)])
    password = StringField("Password", [validators.Length(min=1)])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    password = StringField("New Password", [validators.Length(min=1)])

    class Meta:
        csrf = False