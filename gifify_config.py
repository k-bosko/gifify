access_credentials = {
    "aws_access_key_id": "ASIAXWSOBH3NR5IAKHZ4",
    "aws_secret_access_key": "PlsdpEXeSVbXwJX3K7Mz7Vkc4RmlYGR627y6weYy",
    "aws_session_token": "FwoGZXIvYXdzEGIaDMX9bgEogzGgRaJd1CLJAb9aa9AZgE+mBamsw9y7tykmfMf8zBxxmhX20ZRVLJh/jkeRMHt1Tv1Wz9pqPtUVWfjkxzbGqhQqEwE+JGVjb/OQFWhEB8/opMpnR1aHAupNEfPeNhjhHoWkvMtBh0Xr1JLfJ+EQlKPjY6cTDCfdx8fbyzMpbAhQ6x+BzGNZaK+TjqIA5rPrqK6fqBmVOO/c7Wlbyag1BgkbeV435Dx+wUUT7B9oGc/BEa3TNt7orB9S1QvGSPAN4RD6UPwKfhjgwWYheG6va05JByihy7WTBjItlJHU63IhUSianOdOXfoDbP5a1KB4ya2d8Qq2cIs73gSrL/0ngPyCSsMePOpR",
    "region_name": "us-east-1"
}

USER_TABLE = 'Gifify-users'
UPLOAD_BUCKET = 'gifify-src-kbosko'
DOWNLOAD_BUCKET = 'gifify-out-kbosko'

ALLOWED_EXTENSIONS = set(['mov', 'mp4', 'wmv', 'avi', 'flv', 'm4p', 'mpg', 'mpeg', 'mpv', '3gp', '3g2', 'webm'])

# NOTE: allowed file size of 200 MB will be configured at /etc/ngnix/site-enabled/gififyapp after app deployment
