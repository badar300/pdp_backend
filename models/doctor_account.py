from flask_login import UserMixin

from app import db, login_manager



class DoctorAccount(UserMixin,db.Model):
    __tablename__ = 'doctor_account'
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(80), nullable=False)
    branch_name = db.Column(db.String(120), unique=True, nullable=False)
    account_number = db.Column(db.String(11) , nullable=False)
    account_name = db.Column(db.String(120), nullable=False)
    request_amount=db.Column(db.Boolean,nullable=False)
    description = db.Column(db.String(120),nullable=False)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
