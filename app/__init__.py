import pymysql
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app = Flask(__name__, static_url_path='',
            static_folder='images')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:badar@localhost:3306/pdpback'
app.config['SECRET_KEY'] = 'iamsecret'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
CORS(app)
from models import *

db.create_all()

from api.uploadImage.imageApi import *
from api.signup import *
from api.login import *
from api.docProfile.docProfileSetting import *
from api.Doctime_Scheduling.schedule_time import *
