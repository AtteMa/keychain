from flask import redirect, url_for, render_template, request
from flask_login import current_user, login_required
from application import app, db
from application.passwords.models import accountDetails
from application.account.models import Account
from application.service.models import Service
from application.passwords.forms import PasswordForm, UpdateForm

@app.route("/passwords/", methods=["GET"])
def passwords_index():
    return render_template("passwords/list.html",
            passwords = accountDetails.query.filter_by(account_id=current_user.id).order_by(accountDetails.username))

@app.route("/passwords/delete/<password_id>/", methods=["GET"])
@login_required
def passwords_delete(password_id):
    p = accountDetails.query.get(password_id)
    p.service_id = password_id
    s = Service.query.get(p.service_id)
    db.session.delete(s)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("passwords_index"))

@app.route("/passwords/<password_id>/", methods=["GET"])
@login_required
def passwords_update(password_id):
    a = accountDetails.query.get(password_id)
    return render_template("passwords/update.html", password = a, form = UpdateForm())

@app.route("/passwords/<password_id>", methods=["POST"])
@login_required
def passwords_updateAccount(password_id):
    formU = UpdateForm(request.form)
    a = accountDetails.query.get(password_id)
    s = Service.query.get(a.service_id)
    
    if not formU.validate():
        return render_template("passwords/update.html", password = a, username=a.username, service=s, form = formU)

    newP = formU.password.data
    newU = formU.username.data
    newS = formU.service.data
    oldAcc = accountDetails.query.get(password_id)
    oldSer = Service.query.get(oldAcc.service_id)

    oldAcc.password = newP
    oldAcc.username = newU
    oldSer.name = newS
    
    db.session().commit()

    return redirect(url_for("passwords_index"))


@app.route("/passwords/new/")
@login_required
def passwords_form():
    return render_template("passwords/new.html", form = PasswordForm())

@app.route("/passwords/", methods=["POST"])
def passwords_create():
    form = PasswordForm(request.form)

    if not form.validate():
        return render_template("passwords/new.html", form = form)

    s = Service(form.service.data)

    db.session().add(s)

    p = accountDetails(form.password.data, 
        form.username.data)
    p.account_id = current_user.id
    p.service_id = s.id
    
    db.session().add(p)
    db.session().commit()

    return redirect(url_for("passwords_index"))
