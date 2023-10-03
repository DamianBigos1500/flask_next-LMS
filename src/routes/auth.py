from flask import Blueprint
from controllers.authController import get_user, login,register

auth = Blueprint('auth', __name__)

auth.route('/user', methods=['GET'])(get_user)
auth.route('/login', methods=['GET'])(login)
auth.route('/register', methods=['GET'])(register)