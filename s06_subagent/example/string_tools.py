"""String utility helpers."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert arbitrary text into a URL-safe slug.

    The resulting slug is lowercased, simplified using Unicode NFKD
    normalization (dropping diacritics where possible), stripped of
    characters outside ASCII letters and digits, and has runs of
    non-alphanumeric characters replaced by single hyphens. Leading and
    trailing hyphens are removed.

    Args:
        text: The input string to slugify.

    Returns:
        A URL-safe slug string, or an empty string if the input contains
        no alphanumeric characters.
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-")
