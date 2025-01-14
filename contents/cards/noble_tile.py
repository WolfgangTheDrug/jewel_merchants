from typing import Self
from token_collection._token import _Token
from util._card import _Card
from token_collection._token_vector import _TokenVector

class NobleTile(_Card):
    def __init__(self: Self, prestige_points: int, cost: dict[_Token, int]):
        super().__init__(prestige_points, cost)
    
    @property
    def prestige_points(self: Self) -> int:
        return self._prestige_points
    
    @property
    def cost(self: Self) -> _TokenVector:
        return self._cost

    def __str__(self: Self) -> str:
        return f"+--\n| Prestige: {self._prestige_points}\n| Cost: {self._cost}\n+--"