access_credentials = {
    "aws_access_key_id": "ASIAXWSOBH3NUQK2KBG5",
    "aws_secret_access_key": "Vy1ia3/9mPUoqLCyBP1a4AS78jru4wqvFhp6P7aw",
    "aws_session_token": "FwoGZXIvYXdzEFcaDEpTrqMxh5SvAmyaISLJATrFJWIvARBpxXWLxZ8pllZlXP8B3xZvJMets/RJjWQoEbuwoRIzrpZ213ohNuoB75kgQIyBXkcGPb+KBaa5PJmS9iWtg96VQePsd5fqoNrQy6fvm9M3kaoyeI1w20AKnTff5HIpyYeqWciObi9jZekdMRICzUIrjlKu4eHXUba2VrvwRZXmw1ci1n1xOuy4PCXE+kJsuklnanXXRKWIWDUKqTsycm5ds9gQHjwVV5nUcbF5MezC1LCmaXpdUI0m1HkNcs21mI4fRyiyjLOTBjItl49IpwFOv8m2C//UTTsZTyweU3uj4IdXwXwEVQgGRjbFyhJOKDafgADfs34i",
    "region_name": "us-east-1"
}

USER_TABLE = 'Gifify-users'
UPLOAD_BUCKET = 'gifify-src-kbosko'
DOWNLOAD_BUCKET = 'gifify-out-kbosko'

ALLOWED_EXTENSIONS = set(['mov', 'mp4', 'wmv', 'avi', 'flv', 'm4p', 'mpg', 'mpeg', 'mpv', '3gp', '3g2', 'webm'])

# NOTE: allowed file size of 200 MB will be configured at /etc/ngnix/site-enabled/gififyapp after app deployment
