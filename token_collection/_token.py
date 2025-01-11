from dataclasses import dataclass
from typing import Self
@dataclass
class _Token:
    """
    Token class representing a gem/token in the game.
    """
    _name: str
    _color: str
    _symbol: str

    def __str__(self: Self) -> str:
        return f'{self._symbol}'

    def __repr__(self: Self) -> str:
        return f'{self._name=} {self._color=} {self._symbol=}'

