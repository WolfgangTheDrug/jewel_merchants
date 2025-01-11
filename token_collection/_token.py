from dataclasses import dataclass
from typing import Self
@dataclass
class _Token:
    _name: str
    _color: str
    _symbol: str
    _value: int

    def __str__(self: Self):
        return f'{self._symbol} {self._name} ({self._color}): {self._value}'

    def __repr__(self: Self):
        return f'{self._name} {self._color} {self._symbol} {self._value}'

