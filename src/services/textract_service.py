from src.config.aws import textract

def extract_text(bucket_name: str, object_key: str) -> str:
    response = textract.detect_document_text(
        Document={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": object_key,
            }
        }
    )

    lines = []

    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            lines.append(block["Text"])

    return "\n".join(lines)