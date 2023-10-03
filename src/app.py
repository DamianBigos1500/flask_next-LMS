from flask import Flask
from flask_restful import Api
from routes.blueprint import blueprint
from routes.auth import auth
from database import db
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from models.user import User

def create_app():
    app = Flask(__name__) 
    app.config.from_object('config')  
    CORS(app)

    db.init_app(app)  

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    return app


app = create_app() 
api = Api(app)
ma = Marshmallow(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(blueprint, url_prefix='/machines')


if __name__ == '__main__':  # Running the app
    app.run(host='localhost', port=8000, debug=True)