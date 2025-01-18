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
    _gold_count: int

    def __init__(self, name: str):
        self._name = name
        self._tokens = _TokenVector()
        self._cards = []
        self._noble_tiles = []
        self._gold_count = 0
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
    def gold(self) -> int:
        return self._gold_count
    
    @gold.setter
    def gold(self, gold: int):
        self._gold_count = gold

    @gold.deleter
    def gold(self):
        self._gold_count = 0

    @property
    def points(self) -> int:
        return sum(card.prestige_points for card in self._cards) + sum(noble_tile.prestige_points for noble_tile in self._noble_tiles)

    @property
    def bonuses(self) -> _TokenVector:
        return sum(card.bonus for card in self._cards) 
    
    def _add_card(self, card: DevelopmentCard):
        self._cards.append(card)

    def _add_noble_tile(self, noble_tile: NobleTile):
        self._noble_tiles.append(noble_tile)

    def _add_gold(self, gold: int):
        self._gold_count += gold

    def _subtract_gold(self, gold: int):
        self._gold_count -= gold

    def _add_tokens(self, tokens: _TokenVector):
        self._tokens += tokens

    def _subtract_tokens(self, tokens: _TokenVector):
        self._tokens -= tokens

    def purchase_card(self, card: DevelopmentCard):
        discounted_cost: _TokenVector = card.cost - self.bonuses
        difference: _TokenVector = self._tokens - discounted_cost

        if all(token >= 0 for token in difference.tokens.values()):
            self._add_card(card)
            self._subtract_tokens(discounted_cost)
        elif difference.magnitude() <= self._gold_count:
            self._add_card(card)
            self._subtract_gold(difference.magnitude())
            self._subtract_tokens(discounted_cost)
            self._tokens = _TokenVector.from_tokens( {token: count for token, count in self._tokens.tokens.items() if count >= 0} )
        else:
            raise ValueError("Not enough tokens to purchase card")

    def receive_noble_tile(self, noble_tile: NobleTile):
        if self.bonuses >= noble_tile.cost:
            self._add_noble_tile(noble_tile)
        else:
            raise ValueError("Not enough tokens to receive a noble tile")
