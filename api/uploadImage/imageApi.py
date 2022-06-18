from models import Profile, Image,User
from flask import request, make_response,Flask
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
        image.save(os.path.join('/Users/Adil Nisar/PycharmProjects/PdpBackend/pdp_backend/Images', paymentFilename))
        imagePath = ('Images/' + paymentFilename)

        imageData = Image(user_id=user.id, imagePath=imagePath)
        db.session.add(imageData)
        db.session.commit()

        return make_response("added"), 200

@app.route('/getImage', methods=['GET'])
def getImageApi():
    if request.method() == 'GET':
        getImage = request.get_json()
        userId = getImage['userId']
        image = Image.query.filter(Image.user_id == userId).first()
        newimg = io.BytesIO(image.imagePath)
        img = image(newimg)
        print(img)
        return Flask.redirect(Flask.url_for('PATH', filename=img), code=301)
