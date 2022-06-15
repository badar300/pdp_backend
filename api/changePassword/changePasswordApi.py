from flask import *
from app import db, app
from passlib.hash import pbkdf2_sha256
from models import User
from flask_login import current_user
from flask import request


@app.route('/changePassword', methods=['POST'])
def changePassword():
    if request.method == 'POST':
        nPassApi = request.get_json()
        newPassword = nPassApi['newPassword']
        hashed = pbkdf2_sha256.hash(newPassword)
        user = User.query.filter(User.id == current_user.id).first()
        user.password = hashed
        db.session.add(user)
        db.session.commit()
        return make_response("Password change!")
