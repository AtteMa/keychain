from application import db


class Service(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    passwords = db.relationship("accountDetails", backref='service', lazy=True)

    def __init__ (self, name):
        self.name = name

