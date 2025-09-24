
# This is a template for a CDK Python project using Docker

### Why use CDK

Creating infrastructure by interacting by clicking through the several options on the AWS website is not scalable and error prone. 

CDK draws from the "infrastructure as code" framework, ultimately resolving this problem. CDK allows for infrastructure to be created using code (e.g., Python, Typescript or Go), and all the benefits that come with it: the ability to use controlflow, git and auto-complete.

CDK compiles code into a CloudFormation template, which is then used by AWS to create the required infrastructure.

### About this project

This project is a CDK proof of concept written in Python - using Docker. It downloads a dataset from url and uploads it to a s3 bucket.

### Getting started

To use this infrastructure you'll need to have:

1. AWS account
2. AWS CLI
3. AWS CDK
4. Python

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

You can check if the file has been uploaded sucessfully by going to AWS S3, or run `aws s3 ls s3://aws-bucket/path/`. Add the ` --profile name` if using more than one AWS profile.

There are a few manual steps: 
- add you AWS account id and region in `app.py`
- change the name of you s3 bucket in the `UploadRawData` stack 

The first step is to run `cdk bootstrap` which prepares the aws environment and create resources (CloudFormation stack, s3 buckets, sets up trust relationships) to prior to deployment. Only needed one time, after that we just need cdk deploy.

To deploy this lambda run `cdk deploy`. If the deployment is successful, you can test the lambda on AWS, before invoking it. 

### Bulding Docker locally

To build the container run `bash build.sh`. The file has the comands to build and the container. You may need to update your AWS credentials, including profile if you have more than one.

```
docker run --name lambda-uploader \
    -p 9000:8080 \
    -v ~/.aws:/root/.aws \
    -e AWS_PROFILE=cdk-user \
    lambda-uploader
```

For debugging purposes, open a new terminal and run `docker exec -it lambda-uploader /bin/bash`. This will allow you to interact with the container / environment. To test the lambda go to AWS Lambda or run 

```
curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{event payload}'
```

The event payload should have be added inside the brackets. For example:

```
{"bucket": "gla-demography", "url": "https://www.ons
.gov.uk/file?uri=/peoplepopulationandcommunity/birthsdeathsandmarriages/conceptionandfertilityrates/adhocs/2609livebirthsbyageofmotherbylocalaut
horitiesenglandandwales2022to2023/finalfileage.xlsx", "file_key": "fertility/raw/fertility_data.xlsx"}
```

### Testing locally using venv

You may want to interact with your code locally without the Docker first. You can still run the code locally via a virtual environment.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

#### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Have fun!