# Feature specific exceptions

class ShortCodeGenerationError(Exception):
    """Raised when a unique short code cannot be generated after multiple attempts."""
    pass

class LinkNotFoundError(Exception):
    """Raised when a link with the given short code is not found."""
    pass