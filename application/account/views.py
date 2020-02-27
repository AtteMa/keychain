from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from application import app, db
from application.account.models import Account
from application.account.forms import LoginForm, AccountForm

@app.route("/account/login", methods = ["GET", "POST"])
def account_login():
    if request.method == "GET":
        return render_template("account/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)

    account = Account.query.filter_by(username=form.username.data,
        password=form.password.data).first()
    if not account:
        return render_template("account/loginform.html", form=form,
            error = "No such username of password")

    login_user(account)
    return redirect(url_for("index", find_services=Account.find_distinct_services(current_user.id)))

@app.route("/account/logout")
def account_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/account/new/")
def account_form():
    return render_template("account/new.html", form = AccountForm())

@app.route("/account/", methods=["POST"])
def account_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("account/new.html", form = form)

    a = Account.query.filter_by(username=form.username.data).first()

    if a:
        return render_template("account/new.html", form = form,
            error="That username is taken!")

    account = Account(form.name.data, form.username.data, form.password.data)
    
    db.session().add(account)
    db.session().commit()

    return redirect(url_for("index"))
