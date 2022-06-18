from models import Profile, Image, User
from flask import request, make_response, send_from_directory
from werkzeug.utils import secure_filename
from app import app, db
import os
import io


@app.route('/image', methods=["POST"])
def image():
    image = request.files['profileImage']
    userId = request.form['userId']
    user = User.query.filter(User.id == userId).first()

    if image:
        paymentFilename = secure_filename(image.filename)
        print(paymentFilename)
        image.save(os.path.join('/Users/Adil Nisar/PycharmProjects/PdpBackend/pdp_backend/static/Images', paymentFilename))
        imagePath = ('Images/' + paymentFilename)

        imageData = Image(user_id=user.id, imagePath=imagePath)
        db.session.add(imageData)
        db.session.commit()

        return make_response("added"), 200


@app.route('/getImage/<int:idd>', methods=['GET'])
def getImageApi(idd):
    image = Image.query.filter(Image.user_id == idd).first()
    return send_from_directory(
        directory=app.config['UPLOAD_FOLDER'], path=image.imagePath)
