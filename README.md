# Gifify

A Gifify app allows the users to upload a video and get it processed into a gif. 

# Demo
![gifify](https://user-images.githubusercontent.com/46878035/221690264-78198ae0-b96e-428b-9449-dcfc657026b9.gif)

# Technologies
This is a Flask app deployed to AWS EC2 instance. The user login data is saved into DynamoDB, while the users’ uploaded videos and resulting gifs are stored on S3 buckets. The video processing is implemented through a Lambda function (deployed via Docker to ECS).
