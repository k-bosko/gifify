from flask import Flask
from flask_login import LoginManager

from .utils import User


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret_key' #TODO change to cookie

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
