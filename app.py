from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
        
        
with app.app_context():
        db.create_all()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        new_user = User(name = name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "user": new_user.serialize(),
        })



if __name__ == "__main__":
    app.run(debug=True)
