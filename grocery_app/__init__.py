from flask import Flask
from flask import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
from flask_login import LoginManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

#login_manager = LoginManager()
#login_manager.login_view = 'auth.login'
#login_manager.init_app(app)


login_manager = LoginManager()
 #Added this line fixed the issue.
login_manager.init_app(app) 
login_manager.login_view = 'auth.login'


from _importlib_modulespec import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)




###########################
# Blueprints
###########################

from grocery_app.routes import main, auth

app.register_blueprint(main)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()




