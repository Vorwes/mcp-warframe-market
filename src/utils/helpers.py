def to_url_name(item_name: str) -> str:
    """Convert an item name to a URL-friendly format."""
    return item_name.lower().replace(" ", "_")
