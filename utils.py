import boto3
from werkzeug.security import generate_password_hash, check_password_hash
from . import gifify_config
from flask_login import UserMixin
from uuid import uuid4
import os

dynamodb = boto3.resource('dynamodb', **gifify_config.access_credentials)
s3_client = boto3.client('s3', **gifify_config.access_credentials)
s3_resource = boto3.resource('s3', **gifify_config.access_credentials)


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
        key = current_user.user_id + "/" + filename
        s3_client.put_object(
            Body=video_file,
            Bucket = gifify_config.UPLOAD_BUCKET,
            Key = key,
            ContentType=content_type
        )
        return True
    return False


def get_uploaded_files_from_s3(current_user):
    upload_bucket = s3_resource.Bucket(gifify_config.UPLOAD_BUCKET)
    uploaded_files = []
    for obj in upload_bucket.objects.filter(Prefix=current_user.user_id):
        key = obj.key
        filename = key.split('/')[-1]
        uploaded_files.append(filename)
    return uploaded_files

def get_gifs_from_s3(current_user):
    download_bucket = s3_resource.Bucket(gifify_config.DOWNLOAD_BUCKET)
    gif_links = {}
    for obj in download_bucket.objects.filter(Prefix=current_user.user_id):
        filename = os.path.basename(obj.key)
        presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket':
                                                download_bucket.name, 'Key': obj.key}, ExpiresIn = 3600)
        gif_links[filename] = presigned_url

    return gif_links
