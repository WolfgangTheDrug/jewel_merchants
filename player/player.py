from contents.cards.development_card import DevelopmentCard
from contents.cards.noble_tile import NobleTile
from token_collection._token_vector import _TokenVector


class Player:
    """
    Player class
    """

    _name: str
    _tokens: _TokenVector
    _cards: list[DevelopmentCard]
    _noble_tiles: list[NobleTile]

    def __init__(self, name: str):
        self._name = name
        self._tokens = _TokenVector()
        self._cards = []
        self._noble_tiles = []

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @name.deleter
    def name(self):
        self._name = ""

    @property
    def tokens(self) -> _TokenVector:
        return self._tokens
    
    @tokens.setter
    def tokens(self, tokens: _TokenVector):
        self._tokens = tokens

    @tokens.deleter
    def tokens(self):
        self._tokens = _TokenVector()

    @property
    def cards(self) -> list[DevelopmentCard]:
        return self._cards
    
    @cards.setter
    def cards(self, cards: list[DevelopmentCard]):
        self._cards = cards

    @cards.deleter
    def cards(self):
        self._cards = []

    @property
    def noble_tiles(self) -> list[NobleTile]:
        return self._noble_tiles
    
    @noble_tiles.setter
    def noble_tiles(self, noble_tiles: list[NobleTile]):
        self._noble_tiles = noble_tiles

    @noble_tiles.deleter
    def noble_tiles(self):
        self._noble_tiles = []

    @property
    def points(self) -> int:
        return sum(card.points for card in self._cards) + sum(noble_tile.points for noble_tile in self._noble_tiles)

    def add_card(self, card: DevelopmentCard):
        self._cards.append(card)

    def add_noble_tile(self, noble_tile: NobleTile):
        self._noble_tiles.append(noble_tile)

    
