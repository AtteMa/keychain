from application import db
from sqlalchemy.sql import text
from flask_login import current_user

class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    passwords = db.relationship("accountDetails", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True
    
    @staticmethod
    def find_users_with_no_details():
        stmt = text("SELECT COUNT(account_details.id) FROM account_details"
                    " GROUP BY account_details.id")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0]})
        
        count = len(response)
        return count

