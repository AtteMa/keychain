from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from application import db
from application.account.models import Account

class Unique(object):
    def __init__(self, column, session, message="That username is taken!"):
        self.column = column
        self.session = session
        self.message = message

    def __call__(self, form, field):
        if field.data == field.object_data:
            return
        model = self.column.class_
        query = model.query.filter(self.column == field.data).exists()
        if self.session.query(query).scalar():
            raise validators.ValidationError(self.message)

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf=False

class AccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=35)])
    username = StringField("Username", [validators.Length(min=1, max=35), Unique(Account.username, db.session)])
    password = PasswordField("Password", [validators.InputRequired(),
                validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Repeat password")

    class Meta:
        csrf=False