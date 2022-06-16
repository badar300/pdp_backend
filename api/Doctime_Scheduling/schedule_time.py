from flask import *
from flask_login import current_user
from app import db,app
from models import Schedule

@app.route('/signup' ,methods=['POST'])
def schedule():
    schedule = request.get_json()
    duration = schedule['email']
    day = schedule['password']
    schedule = Schedule(user_id=current_user.id, duration=duration, day=day)
    db.session.add(schedule)
    db.session.commit()
    return make_response('Scheduled'), 200
