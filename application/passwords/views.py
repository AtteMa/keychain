from application import app, db
from flask import redirect, url_for, render_template, request
from application.passwords.models import accountDetails
from application.passwords.forms import PasswordForm, UpdateForm

@app.route("/passwords/", methods=["GET"])
def passwords_index():
    return render_template("passwords/list.html", passwords = accountDetails.query.all())

@app.route("/passwords/<password_id>/", methods=["GET"])
def passwords_update(password_id):
    a = accountDetails.query.get(password_id)
    return render_template("passwords/update.html", password = a, form = UpdateForm())

@app.route("/passwords/<password_id>", methods=["POST"])
def passwords_updateAccount(password_id):
    a = accountDetails.query.get(password_id)
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("passwords/update.html", password = a, form = form)

    new = form.password.data
    old = accountDetails.query.get(password_id)
    old.password = new
    
    db.session().commit()

    return redirect(url_for("passwords_index"))


@app.route("/passwords/new/")
def passwords_form():
    return render_template("passwords/new.html", form = PasswordForm())

@app.route("/passwords/", methods=["POST"])
def passwords_create():
    form = PasswordForm(request.form)

    if not form.validate():
        return render_template("passwords/new.html", form = form)

    p = accountDetails(form.password.data, 
        form.username.data)
    
    db.session().add(p)
    db.session().commit()

    return redirect(url_for("passwords_index"))
