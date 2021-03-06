from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///passwords.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.passwords import models
from application.passwords import views

from application.service import models

from application.account import models
from application.account import views

# kirjautuminen
from application.account.models import Account
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "account_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(account_id)

try:
    db.create_all()
except:
    pass



