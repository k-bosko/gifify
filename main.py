from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .utils import s3_upload

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # print(f'username - {current_user.username}')
    return render_template('profile.html', username=current_user.username)

@main.route('/account')
@login_required
def account():
    return render_template('account.html')

@main.route('/upload',methods=['POST'])
@login_required
def upload():
    '''
    Upload video file to S3 source bucket
    '''
    content_type = request.mimetype
    video_file = request.files['file']

    is_uploaded = s3_upload(video_file, content_type, current_user)
    if is_uploaded:
        msg = "Uploaded"
        # write to DB
    else:
        msg = "Upload failed" #TODO add explanation what files can be uploaded + optionally add size limitations
    return render_template("profile.html",msg =msg)
