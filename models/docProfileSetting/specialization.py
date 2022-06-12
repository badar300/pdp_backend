from app import db


class Specialization(db.Model):
    __tablename__ = 'specialization'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('profile.id'))
    specialization = db.Column(db.String(80), default=None)

