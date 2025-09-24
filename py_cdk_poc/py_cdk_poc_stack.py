from aws_cdk import (
    Duration,
    Stack,
)
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from constructs import Construct


class UploadRawData(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gla_demography_bucket = s3.Bucket.from_bucket_name(
            self, "demography_bucket", "gla-demography"
        )

        lambda_fn = _lambda.DockerImageFunction(
            self,
            "LambdaFunction",
            function_name="lambda_function_docker",
            code=_lambda.DockerImageCode.from_image_asset(directory="./"),
            timeout=Duration.minutes(5),
            environment={"LOG_LEVEL": "INFO"},
            architecture=_lambda.Architecture.ARM_64,  # Setting architecture resolved entrypoint error
        )

        # Need to give lambda access to s3 to write files.
        gla_demography_bucket.grant_write(lambda_fn)
