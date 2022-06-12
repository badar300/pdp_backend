from app import db


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    duration = db.Column(db.String(80), nullable=False)
    day = db.Column(db.String(120), unique=True, nullable=False)

