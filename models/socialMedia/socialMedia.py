from app import db


class SocialMedia(db.Model):
    __tablename__ = 'socialMedia'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    facebook = db.Column(db.String(80), default=None)
    twitter = db.Column(db.String(80), default=None)
    instagram = db.Column(db.String(80), default=None)
    pintrest = db.Column(db.String(80), default=None)
    linkedIn = db.Column(db.String(80), default=None)
    youtube = db.Column(db.String(80), default=None)