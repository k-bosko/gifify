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

@main.route('/pull_links')
@login_required
def pull_links():
    # get user data
    result_dict = {
        'uploads': [
            {
                'name': 'dogs.mov',
                'timestamp': '2012-01-01',
                'url': 'https://example.com/uploads/2012-01-01/dogs.mov'
            },
        ],
        'downloads': [
            {
                'name': 'dogs.gif',
                'timestamp': '2012-01-02',
                'url': 'https://example.com/uploads/2012-01-02/dogs.gif'
            },
        ]
    }
    return result_dict

# @main.route('/download')
# @login_required
# def download():
#     '''
#     Download gif from S3 out bucket
#     '''

#     is_downloaded = s3_download(video_file, content_type, current_user)

#     if is_downloaded:
#         msg = "Downloaded"
#         # write to DB
#     else:
#         msg = "Download failed" #TODO add explanation what files can be uploaded + optionally add size limitations
#     return render_template("profile.html",msg =msg)
