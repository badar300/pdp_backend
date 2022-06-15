from app import db

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    phoneNo = db.Column(db.String(12), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80), default=None)
    biography = db.Column(db.String(80), default=None)
    address = db.Column(db.String(80), default=None)
    city = db.Column(db.String(80), default=None)
    state = db.Column(db.String(80), default=None)
    country = db.Column(db.String(80), default=None)
    postalCode = db.Column(db.String(80), default=None)
    pricing = db.Column(db.String(80), default=None)
    pmc = db.Column(db.String(80), default=None)









