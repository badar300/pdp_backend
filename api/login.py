from flask import *
from app import app

from passlib.hash import pbkdf2_sha256
from models import User
import datetime
import jwt
from flask_login import login_user

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        loginApi = request.get_json()
        email = loginApi['email']
        password = loginApi['password']
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        user = User.query.filter(User.email == email).first()
        if not user:
            return 'User Not Found!', 404

        if pbkdf2_sha256.verify(password, user.password):
            login_user(user)
            data = {
                'id': user.id,
                'username': user.userName,
                'email': user.email,
                'role': user.role,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = (jwt.encode(data, app.config['SECRET_KEY']))
            temp = [token]
            obj = json.dumps(temp)
            return obj
        else:
            return 'Invalid Login Info!', 400
    else:
        return "chutti ker"
