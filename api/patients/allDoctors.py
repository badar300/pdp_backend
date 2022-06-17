from app import app, db
from models import Profile, Review
from flask import make_response

@app.route('/all_doctors', methods=['POSt'])
def get_all_doctors():
    doctors = Profile.query.join(Review).filter(Profile.user_id == Review.user_id).first()
    doc_list = []
    for doctor in doctors:
        dict={
            'profile_id':doctor.id,
            'name':doctor.firstName,
            'city':doctor.city,
            'country':doctor.country,
            'pricing':doctor.pricing,
            'address':doctor.address,
            'gender':doctor.gender,
        }
        doc_list.append(dict)
    return make_response(doc_list, 200)
