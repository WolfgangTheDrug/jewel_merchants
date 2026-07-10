class TokenMismatchError(ValueError):
    """Raised when operating on token piles of different types."""
    pass


class InsufficientTokensError(ValueError):
    """Raised when a subtraction results in a negative token count."""
    pass