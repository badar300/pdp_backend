import json

from flask import *
from passlib.hash import pbkdf2_sha256
from app import db, app
from models import User, DoctorAccount


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        signupAPI = request.get_json()
        bankName = signupAPI['bankName']
        branchName = signupAPI['branchName']
        accountNo = signupAPI['accountNo']
        accountName = signupAPI['accountName']
        requestAmount = signupAPI['requestAmount']
        description = signupAPI['description']

        doctor_account = DoctorAccount(bank_name=bankName, branch_name=branchName, account_name=accountName,
                                       account_number=accountNo, request_amount=requestAmount, description=description)
        db.session.add(doctor_account)
        db.session.commit()
        return make_response(jsonify({'message': "Account information has been added"}), 200)
    

