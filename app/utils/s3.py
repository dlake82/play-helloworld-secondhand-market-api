from typing import Any

import boto3
from botocore.client import Config

from app.core.config import settings
from app.utils.logger import make_logger

logger = make_logger(__name__)


# AWS와 호환되기 때문에,
class S3:
    def __init__(self):
        self.aws_s3_client = boto3.client(
            "s3",
            endpoint_url=settings.s3_endpoint_url,
            aws_access_key_id=settings.s3_access_key,
            aws_secret_access_key=settings.s3_secret_key,
            config=Config(signature_version="s3v4"),
            region_name="ap-northeast-2",
            verify=False,
        )

    def get_keys(self, bucket_name: str, file_path: str = ""):
        list_objects = self.aws_s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=file_path,
        )

        if list_objects.get("KeyCount") == 0:
            return []

        keys = [
            s3_object_metadata.get("Key")
            for s3_object_metadata in list_objects.get("Contents")
        ]

        return keys

    def get(self, bucket_name: str, key: str) -> Any:
        s3_object = self.aws_s3_client.get_object(Bucket=bucket_name, Key=key)
        s3_object_binary_data = s3_object["Body"].read()
        return s3_object_binary_data

    def put(self, bucket_name: str, key: str, data: bytes):
        result = self.aws_s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=data,
            ContentType="binary/octet-stream",
        )

        return result

    def get_presigned_url(self, bucket_name: str, key: str) -> str:
        result = self.aws_s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": bucket_name,
                "Key": key,
            },
            ExpiresIn=3600,
            HttpMethod="PUT",
        )

        return result

    def delete(self, bucket_name: str, key: str):
        result = self.aws_s3_client.delete_object(Bucket=bucket_name, Key=key)
        return result
