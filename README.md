# Gifify

A Gifify app allows the users to upload a video and get it processed into a gif. 

# Demo
![gifify](https://user-images.githubusercontent.com/46878035/221690264-78198ae0-b96e-428b-9449-dcfc657026b9.gif)

# Technologies
This is a Flask app deployed to AWS EC2 instance. The user login data is saved into DynamoDB, while the users’ uploaded videos and resulting gifs are stored on S3 buckets. The video processing is implemented through a Lambda function (deployed via Docker to ECS).

## Architecture

<img width="557" alt="image" src="https://user-images.githubusercontent.com/46878035/221692946-1a326ca0-1767-41ca-bd08-be057ec1dc0a.png">


## Lambda function example

<img width="566" alt="image" src="https://user-images.githubusercontent.com/46878035/221694091-44b29c52-449f-428a-8093-f1d5c53e483d.png">
