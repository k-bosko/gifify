access_credentials = {
    "aws_access_key_id": "ASIAXWSOBH3NTOQX2MM7",
    "aws_secret_access_key": "dLcaPx1ShHGqn+6tEIlFjIvCbNWrW8Yr1IFS+vbJ",
    "aws_session_token": "FwoGZXIvYXdzEHoaDE03QkGiTIlKmpsQgiLJAVFhssK1dtLpdeaKZ8a9o8ywjFbzUbvADTmI8JMe66J+tLNYdKNDMtFyNWvNHFV4YHLTRMeTdWwRbR6AeUlkVtIhqN2OXXUAq6RAxyce7MbSqPFNvDKN5YfsmSZptqMpVJXyL0enH+C9kjgb5vraCpxDAWqeDd/Z8gqksJ69jquoJmvACAfVl/R5jzuWkG8w9HBIfD8RtDOetnwV8+qeqygaS1q8I/L3JLQJx/7ZyvIwlUZBVBd2OdxnsZg2RvTkLxhRDcCTI2kFmSjv7bqTBjItAF67U/yapmMCi+w5Qggv3LjusrMW4aJVSLhdETz3WSmP4OAYAVxpA/fpDC44",
    "region_name": "us-east-1"
}

USER_TABLE = 'Gifify-users'
UPLOAD_BUCKET = 'gifify-src-kbosko'
DOWNLOAD_BUCKET = 'gifify-out-kbosko'

ALLOWED_EXTENSIONS = set(['mov', 'mp4', 'wmv', 'avi', 'flv', 'm4p', 'mpg', 'mpeg', 'mpv', '3gp', '3g2', 'webm'])

# NOTE: allowed file size of 200 MB will be configured at /etc/ngnix/site-enabled/gififyapp after app deployment
