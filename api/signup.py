import json

from flask import *
from passlib.hash import pbkdf2_sha256
from app import db, app
from models import User


@app.route('/register', methods=['POST'])
def signup():
    if request.method == 'POST':
        signupAPI = request.get_json()
        userName = signupAPI['firstName'] + " " + signupAPI['lastName']
        email = signupAPI['email']
        password = signupAPI['password']
        hashed = pbkdf2_sha256.hash(password)
        phoneNo = signupAPI['phone']
        # role = signupAPI['role']
        checkEmail = User.query.filter_by(email=email).first()
        checkphone = User.query.filter_by(phoneNo=phoneNo).first()

        if checkEmail != None or checkphone != None:
            return make_response("Email or PhoneNo already exists!"), 400
        else:
            if checkEmail == None:
                if checkphone == None:
                    newUser = User(userName=userName, email=email,
                                   password=hashed, phoneNo=phoneNo, role="doctor", isProfileCompleted=False)
                    db.session.add(newUser)
                    db.session.commit()

                    temp = {
                        "id": newUser.id,
                        "username": newUser.userName,
                        "email": newUser.email,
                        "phoneNo": newUser.phoneNo,
                        "role": newUser.role,
                        "isProfileCompleted": newUser.isProfileCompleted
                    }
                    signupData = json.dumps(temp)
                    return make_response(signupData), 200
                else:
                    return make_response("phone no already exists"), 400
            else:
                return make_response("email already exists"), 400
