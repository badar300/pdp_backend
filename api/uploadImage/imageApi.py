from models import Profile, Image
from flask_login import current_user
from flask import request, make_response
from werkzeug.utils import secure_filename
from app import app, db
import os


@app.route('/image', methods=["POST"])
def image():
    image = request.files['profileImage']
    print(current_user.id)
    profile = Profile.query.filter(Profile.user_id == current_user.id).first()

    if image:
        paymentFilename = secure_filename(image.filename)
        image.save(os.path.join('images', paymentFilename))
        imagePath = ('images/' + paymentFilename)
        print(profile.id)

        imageData = Image(pid=profile.id, imagePath=imagePath)
        db.session.add(imageData)
        db.session.commit()

        return make_response("added"), 200
