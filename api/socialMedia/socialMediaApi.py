from app import app, db
from models import SocialMedia, User
from flask_login import current_user
import json
from flask import request, make_response


@app.route('/socialMedia', methods=['POST'])
def socialMedia():
    if request.method == 'POST':
        socialApi = request.get_json()
        facebook = socialApi['facebook']
        twitter = socialApi['twitter']
        instagram = socialApi['instagram']
        pintrest = socialApi['pintrest']
        linkedIn = socialApi['linkedIn']
        youtube = socialApi['youtube']
        # user = User.query.filter(User.id == current_user.id).first()

        socialMediaData = SocialMedia(uid=current_user.id, facebook=facebook, twitter=twitter, instagram=instagram,
                                      pintrest=pintrest, linkedIn=linkedIn, youtube=youtube)
        db.session.add(socialMediaData)
        db.session.commit()

        return make_response("added"), 200


@app.route('/getSocialMedia', methods=['GET'])
def getSocialMedia():
    if request.method == 'GET':
        allData = []
        getData = SocialMedia.query.all()
        if getData:
            for i in getData:
                dict = {
                    "uid": i.uid,
                    "facebook": i.facebook,
                    "twitter": i.twitter,
                    "instagram": i.instagram,
                    "pintrest": i.pintrest,
                    "linkedIn": i.linkedIn,
                    "youTube": i.youtube
                }
                allData.append(dict)
            print(allData)
            socialMediaData = json.dumps(allData)
            return socialMediaData
        else:
            return make_response("No data Found"), 400