from enum import Enum
from typing import Self
from token_collection._token import _Token

class Token(Enum):
    """
    Token class representing different types of gems/tokens in the game.
    Each token has a name, color, symbol (emoji), and value.
    """

    EMERALD = _Token('Emerald', 'Green', '🟢')
    DIAMOND = _Token('Diamond', 'Blue', '🔵')
    SAPPHIRE = _Token('Sapphire', 'Purple', '🟣')
    RUBY = _Token('Ruby', 'Red', '🔴')
    ONYX = _Token('Onyx', 'Black', '⚫')

    def __str__(self: Self) -> str:
        return self.value.__str__()

    def __repr__(self: Self) -> str:
        return self.value.__repr__()
    
    @property
    def name(self: Self) -> str:
        return self.value.name
    
    @property
    def color(self: Self) -> str:
        return self.value.color
    
    @property
    def symbol(self: Self) -> str:
        return self.value.symbol