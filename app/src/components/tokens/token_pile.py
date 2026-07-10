from __future__ import annotations
from enum import Enum, auto

from .exceptions import InsufficientTokensError, TokenMismatchError


class TokenType(Enum):
    RUBY = auto()
    EMERALD = auto()
    SAPPHIRE = auto()
    DIAMOND = auto()
    ONYX = auto()
    GOLD = auto()


class TokenPile:
    """Manages a single type of currency pile for Splendor."""

    _type: TokenType
    _count: int

    def __init__(self, type: TokenType, count: int = 0, *, _bypass_validation: bool = False) -> None:
        """Initializes a token pile.

        Raises:
            InsufficientTokensError: If count is negative and validation isn't bypassed.
        """
        # Using a keyword-only argument _bypass_validation to ensure internal-only usage.
        if count < 0 and not _bypass_validation:
            raise InsufficientTokensError(f"Insufficient tokens of type {type.name}: {count}.")
            
        self._type = type
        self._count = count

    @property
    def type(self) -> TokenType:
        return self._type
    
    @property
    def count(self) -> int:
        return self._count

    def __add__(self, other: TokenPile) -> TokenPile:
        """Combines two token piles of the same type.

        Raises:
            TokenMismatchError: If token types do not match.
            InsufficientTokensError: If the resulting total drops below zero.
        """
        if self.type != other.type:
            raise TokenMismatchError(f"Cannot mix tokens of type: {self.type.name} with: {other.type.name}.")
        return TokenPile(self.type, self.count + other.count)

    def __neg__(self) -> TokenPile:
        """Inverts the count of the pile safely for internal algebraic subtraction."""
        return TokenPile(self.type, -self.count, _bypass_validation=True)

    def __sub__(self, other: TokenPile) -> TokenPile:
        """Subtracts a token pile using algebraic negation."""
        return self + -other

    def __repr__(self) -> str:
        return f"TokenPile({self.type.name}: {self.count})"