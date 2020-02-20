from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PasswordForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=1, max=35)])
    password = StringField("Password", [validators.Length(min=1, max=35)])
    service = StringField("Service Provider", [validators.Length(min=1, max=35)])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    password = StringField("New Password", [validators.Length(min=1, max=35)])

    class Meta:
        csrf = False