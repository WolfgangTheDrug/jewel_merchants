from typing import Literal
from contents.cards.development_card import DevelopmentCard
from contents.cards.noble_tile import NobleTile
from token_collection._token_vector import _TokenVector

class Board:
    _noble_tiles: list[NobleTile]
    _development_cards: dict[int, list[DevelopmentCard]]
    _tokens: _TokenVector
    _gold_count: int

    def __init__(self, noble_tiles: list[NobleTile], development_cards: dict[int, list[DevelopmentCard]], player_count: Literal[2, 3, 4]):
        self._noble_tiles = noble_tiles
        self._development_cards = development_cards
        match player_count:
            case 2:
                self._tokens = _TokenVector().from_tokens({token: 4 for token in _TokenVector.tokens})
            case 3:
                self._tokens = _TokenVector().from_tokens({token: 5 for token in _TokenVector.tokens})
            case 4:
                self._tokens = _TokenVector().from_tokens({token: 7 for token in _TokenVector.tokens})
        self._gold_count = 0
