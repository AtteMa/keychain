from application import app, db
from flask import redirect, url_for, render_template, request
from application.passwords.models import accountDetails

@app.route("/passwords/", methods=["GET"])
def passwords_index():
    return render_template("passwords/list.html", passwords = accountDetails.query.all())

@app.route("/passwords/<password_id>/", methods=["GET"])
def passwords_update(password_id):
    a = accountDetails.query.get(password_id)
    return render_template("passwords/update.html", password = a)

@app.route("/passwords/<password_id>", methods=["POST"])
def passwords_updateAccount(password_id):
    new = accountDetails(request.form.get("password"), 
        request.form.get("username"))
    old = accountDetails.query.get(password_id)
    old.password = new.password
    old.username = new.username
    
    db.session().commit()

    return redirect(url_for("passwords_index"))


@app.route("/passwords/new/")
def passwords_form():
    return render_template("passwords/new.html")

@app.route("/passwords/", methods=["POST"])
def passwords_create():
    p = accountDetails(request.form.get("password"),
        request.form.get("username"))
    
    db.session().add(p)
    db.session().commit()

    return redirect(url_for("passwords_index"))
