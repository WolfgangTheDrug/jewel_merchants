import random
from typing import Literal, Self

from contents.cards.development_card import DevelopmentCard
from contents.cards.noble_tile import NobleTile
from token_collection._token_vector import _TokenVector

class Board:
    _noble_tiles: list[NobleTile]
    _development_cards: dict[int, list[DevelopmentCard]]
    _uncovered_development_cards: dict[int, list[DevelopmentCard]]
    _tokens: _TokenVector
    _gold_count: int

    def __init__(self: Self, noble_tiles: list[NobleTile], development_cards: dict[int, list[DevelopmentCard]], player_count: Literal[2, 3, 4]):
        self._noble_tiles = random.sample(noble_tiles, player_count + 1)
        self._development_cards = development_cards
        self._uncovered_development_cards = {k: [v.pop(random.randrange(len(v))) for _ in range(4)] for k, v in development_cards.items()}
        match player_count:
            case 2:
                self._tokens = _TokenVector().from_tokens({token: 4 for token in _TokenVector.tokens})
            case 3:
                self._tokens = _TokenVector().from_tokens({token: 5 for token in _TokenVector.tokens})
            case 4:
                self._tokens = _TokenVector().from_tokens({token: 7 for token in _TokenVector.tokens})
        self._gold_count = 0

    @property
    def tokens(self: Self) -> _TokenVector:
        return self._tokens

    @property
    def gold_count(self: Self) -> int:
        return self._gold_count
    

    @property
    def uncovered_development_cards(self: Self, player_id: int) -> list[DevelopmentCard]:
        return self._uncovered_development_cards[player_id]
    
    @property
    def noble_tiles(self: Self) -> list[NobleTile]:
        return self._noble_tiles
    
    def __str__(self: Self) -> str:
        return f"Board(Tokens: {self.tokens}\nGold: {self.gold_count}\nNoble Tiles: {self.noble_tiles}\nUncovered Development Cards: {self.uncovered_development_cards})"
