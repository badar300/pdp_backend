from app import db


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('profile.id'))
    imagePath = db.Column(db.String(200), default=None)
