import json
from flask import request
from flask_login import current_user, login_user, logout_user, login_required
from database import db
from models.user import User
from services.user_service import insert_logic, create_logic

@login_required
def get_user():
    return {
        'user': current_user.id,
    }

def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')  

    user = User.query.filter_by(email=email).first()
    if user:
        if user.check_password(password):
            login_user(user, remember=True)
            return {
                "message": "You are logged in"
            }
        return {
            "message": "password not match"
        }
    return {
        "message": "user do not exist"
    }


  

def register():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    new_user = User(name, email, password)
    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "Succesfully login",
        "data": email
    }