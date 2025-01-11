from dataclasses import dataclass


@dataclass
class _Token:
    _name: str
    _color: str
    _symbol: str
    _value: int

    def __str__(self):
        return f'{self._symbol} {self._name} ({self._color}): {self._value}'

    def __repr__(self):
        return f'{self._name} {self._color} {self._symbol} {self._value}'
