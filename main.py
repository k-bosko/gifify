from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .utils import s3_upload, get_uploaded_files_from_s3, get_gifs_from_s3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    uploaded_files = get_uploaded_files_from_s3(current_user)
    return render_template('profile.html', username=current_user.username, uploaded_files=uploaded_files)

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
    uploaded_files = []
    msg = ''
    if is_uploaded:
        # msg = "Uploaded"
        uploaded_files = get_uploaded_files_from_s3(current_user)
    else:
        #TODO add explanation what files can be uploaded + optionally add size limitations
        msg = "Upload failed"
    return render_template("profile.html",msg =msg, username=current_user.username, uploaded_files=uploaded_files)

@main.route('/pull_links')
@login_required
def pull_links():
    # get user data
    user_gifs = get_gifs_from_s3(current_user)
    return user_gifs
