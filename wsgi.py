from flask import Flask
from flask_login import LoginManager

from gififyapp.main import main as main_blueprint
from gififyapp.auth import auth as auth_blueprint
from gififyapp.utils import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run()
