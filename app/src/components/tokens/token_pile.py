from __future__ import annotations
from enum import Enum, auto

from app.src.config import TOKEN_INSUFFICIENCY_LIMIT

from .exceptions import InsufficientTokensError, TokenMismatchError


class TokenType(Enum):
    RUBY = auto()
    EMERALD = auto()
    SAPPHIRE = auto()
    DIAMOND = auto()
    ONYX = auto()
    GOLD = auto() # This one is special...


class TokenPile:
    """Manages a single type of currency pile for the game."""

    _type: TokenType
    _count: int

    def __init__(self, token_type: TokenType, count: int = 0, *, _bypass_count_validation: bool = False) -> None:
        """Initializes a token pile.

        Raises:
            InsufficientTokensError: If count is below TOKEN_INSUFFICIENCY_LIMIT and validation isn't bypassed.
        """
        # Using a keyword-only argument _bypass_count_validation to ensure internal-only usage.
        if count < TOKEN_INSUFFICIENCY_LIMIT and not _bypass_count_validation:
            raise InsufficientTokensError(f"Insufficient tokens of type {token_type.name}: {count}.")
            
        self._type = token_type
        self._count = count

    @classmethod
    def single(cls, token_type: TokenType):
        """Syntactic sugar to create a single token acting as a pile."""
        return cls(token_type, 1)
    
    @property
    def token_type(self) -> TokenType:
        return self._type
    
    @property
    def count(self) -> int:
        return self._count

    def __add__(self, other: TokenPile) -> TokenPile:
        """Combines two token piles of the same type.

        Raises:
            TokenMismatchError: If token types do not match.
            InsufficientTokensError: If the resulting total drops below TOKEN_INSUFFICIENCY_LIMIT.
        """
        if self.token_type != other.token_type:
            raise TokenMismatchError(f"Cannot mix tokens of type: {self.token_type.name} with: {other.token_type.name}.")
        return TokenPile(self.token_type, self.count + other.count)

    def __neg__(self) -> TokenPile:
        """Inverts the count of the pile safely for internal algebraic subtraction."""
        return TokenPile(self.token_type, -self.count, _bypass_count_validation=True)

    def __sub__(self, other: TokenPile) -> TokenPile:
        """Subtracts a token pile using algebraic negation."""
        return self + (-other)

    def __eq__(self, other: object) -> bool:
        """Check if a token pile is the same as the other one, type and value."""
        if not isinstance(other, TokenPile):
            return NotImplemented
        
        return self.token_type == other.token_type and self.count == other.count
    
    def __repr__(self) -> str:
        return f"TokenPile({self._type.name}: {self._count})"