import logging
from typing import Any

from src.aws_helpers import upload_file_to_s3
from src.get_data_from_url import get_data_from_url

logger = logging.getLogger(__name__)


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    print("🔍 Event received:", event)
    try:
        bucket = event["bucket"]
        url = event["url"]
        file_key = event["file_key"]

        response = get_data_from_url(url=url)

        upload_file_to_s3(bucket=bucket, file_key=file_key, response=response)

        logger.info(f"File {file_key} sucessfully uploaded to S3 bucket {bucket}")
        return {
            "statusCode": 200,
            "message": f"File {file_key} sucessfully uploaded to S3 bucket {bucket}",
        }
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise
