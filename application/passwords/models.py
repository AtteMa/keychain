from application import db

class accountDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    password = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'),
                    nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                    nullable=False)

    def __init__(self, password, username):
        self.password = password
        self.username = username

