from app import db


class Services(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    pid=db.Column(db.Integer, db.ForeignKey('profile.id'))
    services = db.Column(db.String(80), default=None)

