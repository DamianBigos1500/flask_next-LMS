import bcrypt
from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))

  
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

  # def serialize(self):
  #     return self)