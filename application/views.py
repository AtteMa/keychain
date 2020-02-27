from flask import render_template
from application import app, db
from application.account.models import Account
from flask_login import current_user, login_required

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("index.html", find_services=Account.find_distinct_services(current_user.id),
                                no_saved=Account.find_users_with_details())
    else:
        return render_template("index.html")
