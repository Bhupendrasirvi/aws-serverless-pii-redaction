"""
AWS service clients used across the application.
"""

import boto3

s3 = boto3.client("s3")
textract = boto3.client("textract")
comprehend = boto3.client("comprehend")