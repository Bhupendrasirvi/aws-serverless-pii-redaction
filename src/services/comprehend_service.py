from typing import Any

from src.config.aws import comprehend


def detect_pii(text: str) -> list[dict[str, Any]]:
    """
    Detect Personally Identifiable Information (PII) in text.

    Args:
        text: Extracted document text.

    Returns:
        List of detected PII entities.
    """

    if not text.strip():
        return []

    response = comprehend.detect_pii_entities(
        Text=text,
        LanguageCode="en",
    )

    return response.get("Entities", [])