from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .utils import s3_upload, get_uploaded_files_from_s3, get_gifs_from_s3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/gifify')
@login_required
def gifify():
    uploaded_files = get_uploaded_files_from_s3(current_user)
    return render_template('gifify.html', username=current_user.username, uploaded_files=uploaded_files)

@main.route('/account')
@login_required
def account():
    return render_template('account.html', username=current_user.username, email=current_user.id)


@main.route('/upload',methods=['POST'])
@login_required
def upload():
    '''
    Upload video file to S3 source bucket
    '''
    content_type = request.mimetype
    video_file = request.files['file']

    is_uploaded = s3_upload(video_file, content_type, current_user)
    uploaded_files = get_uploaded_files_from_s3(current_user)
    msg = ''
    if is_uploaded:
        msg = "Uploaded"
        uploaded_files = get_uploaded_files_from_s3(current_user)
    else:
        #TODO add explanation what files can be uploaded
        msg = "Upload failed"
    return render_template("gifify.html", msg=msg, username=current_user.username, uploaded_files=uploaded_files)

@main.route('/pull_links')
@login_required
def pull_links():
    # get user data
    user_gifs = get_gifs_from_s3(current_user)
    return user_gifs
