from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import boto3
from . import key_config as keys
from boto3.dynamodb.conditions import Key, Attr
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

USER_TABLE = 'Gifify-users'

dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=keys.ACCESS_KEY_ID,
                    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                    aws_session_token=keys.AWS_SESSION_TOKEN,
                    region_name=keys.REGION)

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    password_hashed = generate_password_hash(password, method='sha256')
    userId = str(uuid4())

    # check if user with this email already exists
    response = table.query(
                KeyConditionExpression=Key('email').eq(email)
    )

    # if such user exists, redirect to login
    if response:
        return redirect(url_for('auth.login'))

    table = dynamodb.Table(USER_TABLE)
    table.put_item(
            Item={
                    'userID': userId,
                    'name': name,
                    'email': email,
                    'password': password_hashed
                }
    )
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User(email)
    if user.verify_password(password):
        login_user(user, remember)
        return redirect(url_for('main.profile]'))

    return render_template('login.html')

    # table = dynamodb.Table(USER_TABLE)
    # response = table.query(
    #             KeyConditionExpression=Key('email').eq(email)
    # )
    # if response:
    #     items = response['Items']
    #     if check_password_hash(items[0]['password'], password):

    #         login_user(user, remember=remember) #TODO get user from response?
    #         return redirect('main.profile')
    #     else:
    #         msg = "Incorrect password. Try again."
    #         return render_template('login.html', msg=msg)
    # else:
    #     return redirect(url_for('auth.signup'))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('main.index')
