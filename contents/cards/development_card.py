from token_collection._token import _Token
from token_collection._token_vector import _TokenVector
from typing import Literal, Self
from util._card import _Card

class DevelopmentCard(_Card):
    _bonus: _TokenVector
    _level: Literal[1, 2, 3]

    def __init__(self, level: Literal[1, 2, 3], prestige_points: int, cost: dict[_Token, int], bonus: _Token):
        super().__init__(prestige_points, cost)
        self._level = level
        self._bonus = _TokenVector.from_tokens({bonus: 1})
    
    
    @property
    def prestige_points(self: Self) -> int:
        return self._prestige_points

    @property
    def cost(self: Self) -> _TokenVector:
        return self._cost
    
    @property
    def bonus(self: Self) -> _TokenVector:
        return self._bonus
    
    @property
    def level(self: Self) -> Literal[1, 2, 3]:
        return self._level
    
    def __str__(self: Self) -> str:
        bonus = list(self._bonus.tokens.keys())[0]
        bonus_symbol, bonus_name = bonus.symbol, bonus.name

        return f"+--\n| Level: {'.'*self._level}\n{super().__str__()}\n| Bonus: {bonus_symbol} ({bonus_name})\n+--"