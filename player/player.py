from typing import Literal, Self
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
    _reserved_cards: list[DevelopmentCard]
    _noble_tiles: list[NobleTile]
    _gold_count: int

    def __init__(self: Self, name: str):
        self._name = name
        self._tokens = _TokenVector()
        self._cards = []
        self._reserved_cards = []
        self._noble_tiles = []
        self._gold_count = 0
        self._victory_points_count = 0

    @property
    def name(self: Self) -> str:
        return self._name
    
    @name.setter
    def name(self: Self, name: str) -> None:
        self._name = name

    @name.deleter
    def name(self: Self) -> None:
        self._name = ""

    @property
    def tokens(self: Self) -> _TokenVector:
        return self._tokens
    
    @tokens.setter
    def tokens(self: Self, tokens: _TokenVector) -> None:
        self._tokens = tokens

    @tokens.deleter
    def tokens(self: Self) -> None:
        self._tokens = _TokenVector()

    @property
    def cards(self: Self) -> list[DevelopmentCard]:
        return self._cards
    
    @cards.setter
    def cards(self: Self, cards: list[DevelopmentCard]) -> None:
        self._cards = cards

    @cards.deleter
    def cards(self: Self) -> None:
        self._cards = []

    @property
    def reseved_cards(self: Self) -> list[DevelopmentCard]:
        return self._reserved_cards
    
    @reseved_cards.setter
    def reseved_cards(self: Self, cards: list[DevelopmentCard]) -> None:
        self._reserved_cards = cards

    @reseved_cards.deleter
    def reseved_cards(self: Self) -> None:
        self._reserved_cards = []
        
    @property
    def noble_tiles(self: Self) -> list[NobleTile]:
        return self._noble_tiles
    
    @noble_tiles.setter
    def noble_tiles(self: Self, noble_tiles: list[NobleTile]) -> None:
        self._noble_tiles = noble_tiles

    @noble_tiles.deleter
    def noble_tiles(self: Self) -> None:
        self._noble_tiles = []

    @property
    def gold(self: Self) -> int:
        return self._gold_count
    
    @gold.setter
    def gold(self: Self, gold: int) -> None:
        self._gold_count = gold

    @gold.deleter
    def gold(self: Self) -> None:
        self._gold_count = 0

    @property
    def points(self: Self) -> int:
        return sum(card.prestige_points for card in self._cards) + sum(noble_tile.prestige_points for noble_tile in self._noble_tiles)

    @property
    def bonuses(self: Self) -> _TokenVector:
        return sum(card.bonus for card in self._cards) 
    
    def _add_card(self: Self, card: DevelopmentCard) -> None:
        self._cards.append(card)

    def _add_noble_tile(self: Self, noble_tile: NobleTile) -> None:
        self._noble_tiles.append(noble_tile)

    def _add_gold(self: Self, gold: int) -> None:
        self._gold_count += gold

    def _subtract_gold(self: Self, gold: int) -> None:
        self._gold_count -= gold

    def _add_tokens(self: Self, tokens: _TokenVector) -> None:
        self._tokens += tokens

    def _subtract_tokens(self: Self, tokens: _TokenVector) -> None:
        self._tokens -= tokens

    def purchase_card(self: Self, card: DevelopmentCard) -> None:
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

    def reserve_card(self: Self, card: DevelopmentCard) -> None:
        if len(self._reserved_cards) >= 3:
            raise ValueError("Can't have more than 3 cards reserved at any time.")
        self._reserved_cards.append(card)


    def receive_noble_tile(self: Self, noble_tile: NobleTile) -> None:
        if self.bonuses < noble_tile.cost:
            raise ValueError("Not enough tokens to receive a noble tile.")
        self._add_noble_tile(noble_tile)

    def move(self: Self):
        move_choice: Literal[1, 2, 3, 4]

        move_choice = input(
            """Choose to perform only one of the following four actions:
    1. Take 3 gem tokens of different colors,
    2. Take 2 gem tokens of the same color (this action is only possible if there are at least 4 tokens of the chosen color left when the player takes them),
    3. Reserve 1 development card and take 1 gold token (joker),
    4. Purchase 1 face-up development card from the middle of the table or a previously reserved one.""")