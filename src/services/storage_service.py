"""
Amazon S3 storage operations.
"""

from pathlib import Path

from botocore.exceptions import ClientError

from src.config.aws import s3


def download_file(bucket: str, key: str, destination: Path) -> None:
    """
    Download an object from Amazon S3.

    Args:
        bucket: Source bucket.
        key: Object key.
        destination: Local file path.
    """

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)

        s3.download_file(
            Bucket=bucket,
            Key=key,
            Filename=str(destination),
        )

    except ClientError as exc:
        raise RuntimeError(
            f"Failed to download '{key}' from bucket '{bucket}'."
        ) from exc


def upload_file(source: Path, bucket: str, key: str) -> None:
    """
    Upload a file to Amazon S3.

    Args:
        source: Local file.
        bucket: Destination bucket.
        key: Object key.
    """

    try:
        s3.upload_file(
            Filename=str(source),
            Bucket=bucket,
            Key=key,
        )

    except ClientError as exc:
        raise RuntimeError(
            f"Failed to upload '{key}' to bucket '{bucket}'."
        ) from exc