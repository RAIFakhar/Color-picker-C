"""
Clipboard utilities — clipboard helpers.
Clipboard is handled by the browser in the web version;
these stubs exist only for compatibility.
"""


def copy_to_clipboard(text: str, root=None) -> bool:
    """No-op in the web version — browser JS handles clipboard."""
    return False


def get_from_clipboard(root=None) -> str | None:
    """No-op in the web version."""
    return None
