from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)   

with app.app_context():
   db.create_all()


###########################
# Authentication
###########################


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt(app)


###########################
# Blueprints
###########################

from grocery_app.routes import main, auth

app.register_blueprint(main)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

from flask_bcrypt import Bcrypt

app.register_blueprint(main)

with app.app_context():
   db.create_all()

bcrypt = Bcrypt(app)





