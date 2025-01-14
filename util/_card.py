from typing import Self
from token_collection._token_vector import _TokenVector
from token_collection._token import _Token

class _Card:
    def __init__(self: Self, prestige_points: int, cost: dict[_Token, int]):
        self._prestige_points = prestige_points
        self._cost = _TokenVector.from_tokens(cost)
    
    @property
    def prestige_points(self: Self) -> int:
        return self._prestige_points

    @property
    def cost(self: Self) -> _TokenVector:
        return self._cost
    
    def __str__(self: Self) -> str:
        return f"| Prestige: {self._prestige_points}\n| Cost: {self._cost}"
