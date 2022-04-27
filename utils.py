import boto3
from werkzeug.security import generate_password_hash, check_password_hash
from . import gifify_config
from flask_login import UserMixin
from uuid import uuid4
import time
import datetime

dynamodb = boto3.resource('dynamodb',
            aws_access_key_id=gifify_config.ACCESS_KEY_ID,
            aws_secret_access_key=gifify_config.ACCESS_SECRET_KEY,
            aws_session_token=gifify_config.AWS_SESSION_TOKEN,
            region_name=gifify_config.REGION)

s3_client = boto3.client('s3', aws_access_key_id = gifify_config.ACCESS_KEY_ID,
                        aws_secret_access_key = gifify_config.ACCESS_SECRET_KEY,
                        aws_session_token = gifify_config.AWS_SESSION_TOKEN,
                        region_name=gifify_config.REGION)

class User(UserMixin):
    """
    This user template builds objects that make accessing databased user information easier from the rest of the application.
    It inherits several properties and methods from "UserMixin" for use with
    """
    table = dynamodb.Table(gifify_config.USER_TABLE)

    def __init__(self, email, password, user_id=None):
        self.id = None
        if user_id:
            response = self.table.get_item(Key={'email': user_id})
            if 'Item' in response:
                self.id = response['Item']['email']
                self.username = response['Item']['username']
                self.user_id = response['Item']['user_id']
        else:
            response = self.table.get_item(Key={'email': email})

            if 'Item' in response:
                self.password_hash = response['Item']['password_hash']
                # print(f'found item, checking password')

                if self.verify_password(password):
                    self.id = response['Item']['email']
                    self.username = response['Item']['username']
                    self.user_id = response['Item']['user_id']
                    # print(f'found item, password is ok')
                    return
                # print(f'found item, password is bad')
            print(f'not found item')

    @staticmethod
    def get(user_id):
        user = User(None, None, user_id)
        if user.is_authenticated:
            return user

        return None

    @property
    def is_authenticated(self):
        return self.id is not None

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def signup_new_user(username, email, password):

    password_hash = generate_password_hash(password, method='sha256')

    table = dynamodb.Table(gifify_config.USER_TABLE)

    # check if user exists
    item = table.get_item(Key={'email': email})
    if 'Item' in item:
        return False

    table.put_item(
        Item={
                'username': username,
                'email': email,
                'password_hash': password_hash,
                'user_id': str(uuid4())
            }
    )
    return True

def validate_user_data(email, password):
    if email and password:
        return True
    return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in gifify_config.ALLOWED_EXTENSIONS


def s3_upload(video_file, content_type, current_user):
    filename = video_file.filename
    if video_file and allowed_file(filename):
        s3_client.put_object(
            Body=video_file,
            Bucket = gifify_config.UPLOAD_BUCKET,
            Key = current_user.user_id + "/" + filename,
            ContentType=content_type
        )
        ts=time.time()
        timestamp = datetime.datetime.\
                    fromtimestamp(ts).\
                    strftime('%Y-%m-%d %H:%M:%S')
        table = dynamodb.Table(gifify_config.USERDATA_TABLE)

        #TODO check if mov file already exists?
        table.put_item(
        Item={
                'user_id': current_user.user_id,
                'filename': filename,
                'timestamp': timestamp,
                'key': current_user.user_id + "/" + filename,
            }
    )
        return True
    return False
