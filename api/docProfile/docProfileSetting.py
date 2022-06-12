import json
from models import Profile, User, Services, Education, Experience, Specialization
from app import app, db
from flask_login import current_user
from flask import request, make_response


@app.route('/docProfile', methods=['POST'])
def docProfileSettings():
    if request.method == 'POST':
        docProfileApi = request.get_json()
        firstName = docProfileApi['firstName']
        lastName = docProfileApi['lastName']
        phoneNo = docProfileApi['phoneNo']
        gender = docProfileApi['gender']
        dob = docProfileApi['dob']
        biography = docProfileApi['biography']
        address = docProfileApi['address']
        city = docProfileApi['city']
        state = docProfileApi['state']
        country = docProfileApi['country']
        postalCode = docProfileApi['postalCode']
        pricing = docProfileApi['pricing']
        services = docProfileApi['services']
        specialization = docProfileApi['specialization']
        education = docProfileApi['education']
        experience = docProfileApi['experience']
        # image = request.files['image']
        print("adil")

        getData = Profile.query.filter(Profile.phoneNo == phoneNo).first()
        print(current_user.id)
        user = User.query.filter(User.id == current_user.id).first()

        if getData != None:
            return make_response("Record already added!")
        else:
            user.isProfileCompleted = True
            user.role = "Doctor"
            db.session.add(user)
            db.session.commit()
            profile_data = Profile(user_id=current_user.id, firstName=firstName, lastName=lastName, phoneNo=phoneNo,
                                   gender=gender, dob=dob, biography=biography,
                                   address=address, city=city, state=state, country=country, postalCode=postalCode,
                                   pricing=pricing)
            db.session.add(profile_data)
            db.session.commit()

        for i in services:
            addDataServ = Services(pid=profile_data.id, services=i)
            db.session.add(addDataServ)
            db.session.commit()

        for i in specialization:
            addDataSpecia = Specialization(pid=profile_data.id, specialization=i)
            db.session.add(addDataSpecia)
            db.session.commit()

        for i in education:
            addDataEdu = Education(pid=profile_data.id, degree=i['degree'], institute=i['institute'],
                                   yearOfCompletion=i['yearOfCompletion'])
            db.session.add(addDataEdu)
            db.session.commit()

        for i in experience:
            addDataExp = Experience(pid=profile_data.id, hospitalName=i['hospitalName'], start=i['start'], end=i['end'],
                                    designation=i['designation'])
            db.session.add(addDataExp)
            db.session.commit()

        temp = {
            "id": profile_data.id,
            "uid": profile_data.user_id,
            "firstName": profile_data.firstName,
            "lastName": profile_data.lastName,
            "phoneNo": profile_data.phoneNo,
            "gender": profile_data.gender,
            "dob": profile_data.dob,
            "biography": profile_data.biography,
            "address": profile_data.address,
            "city": profile_data.city,
            "state": profile_data.state,
            "country": profile_data.country,
            "postalCode": profile_data.postalCode,
            "pricing": profile_data.pricing
        }
        profileJson = json.dumps(temp)

        return make_response(profileJson), 200
