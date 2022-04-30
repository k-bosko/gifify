from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user

from .utils import User, signup_new_user, validate_user_data, delete_all_userdata

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # validate data
    if not validate_user_data(email, password):
        return redirect(url_for('auth.login')) # TODO add message about bad input and render template

    is_new_user = signup_new_user(username, email, password)

    if is_new_user:
        user = User(email, password)
        login_user(user)
        # print(f'user is ok - {user.is_authenticated}')
        return redirect(url_for('main.profile'))
    else:
        return redirect(url_for('auth.login')) # TODO add message that user exists and render template


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember_me = True if request.form.get('remember') else False

    # validate data
    if not validate_user_data(email, password):
        return redirect(url_for('auth.login')) # TODO add message that no user info is entered and render template

    user = User(email, password)
    # print(f'user is ok - {user.is_authenticated}')

    if user.is_authenticated:
        login_user(user, remember_me)
        return redirect(url_for('main.profile'))

    return render_template('login.html') # TODO add message why can't login


@auth.route('/logout')
@login_required
def logout():
    delete_all_userdata(current_user)
    logout_user()
    return redirect(url_for('main.index'))
