#!/bin/bash

docker build -t lambda-uploader .

docker run --name lambda-uploader \
    -p 9000:8080 \
    -v ~/.aws:/root/.aws \
    -e AWS_PROFILE=cdk-user \
    lambda-uploader
