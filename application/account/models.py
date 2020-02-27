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
    def find_users_with_details():
        stmt = text("SELECT account.name, COUNT(account_details.id) FROM account"
                    " LEFT JOIN account_details on account_details.account_id = account.id"
                    " GROUP BY account.id"
                    " HAVING COUNT(account_details.id) > 0")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0], "count":row[1]})
        
        return response
    
    @staticmethod
    def find_distinct_services(id):
        stmt = text("SELECT DISTINCT service.name FROM service"
                    " JOIN account_details on account_details.service_id = service.id"
                    " JOIN account on account.id = account_details.account_id"
                    " WHERE (account.id = :id)"
                    " ORDER BY service.name").params(id=id)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[0]})
        
        return response

