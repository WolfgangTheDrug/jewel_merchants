from enum import Enum
from typing import Self
from token_collection._token import _Token

class Token(Enum):
    """
    Token class representing different types of gems/tokens in the game.
    Each token has a name, color, symbol (emoji), and value.
    """

    GOLD = _Token('Gold', 'Yellow', '🟡', 1)
    EMERALD = _Token('Emerald', 'Green', '🟢', 1)
    DIAMOND = _Token('Diamond', 'Blue', '🔵', 1)
    SAPPHIRE = _Token('Sapphire', 'Purple', '🟣', 1)
    RUBY = _Token('Ruby', 'Red', '🔴', 1)
    ONYX = _Token('Onyx', 'Black', '⚫', 1)

    def __str__(self: Self):
        return self.value.__str__()

    def __repr__(self: Self):
        return self.value.__repr__()
