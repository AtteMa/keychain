from flask import render_template
from application import app
from application.account.models import Account

@app.route("/")
def index():
    return render_template("index.html", no_saved=Account.find_users_with_no_details())
