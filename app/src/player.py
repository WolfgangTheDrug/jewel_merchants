from enum import IntEnum


class Player:
    id: int
    name: str
    development_cards: CardAggregateByColor # type: ignore
    reserved_development_cards: list[DevelopmentCard] #type: ignore
    noble_tiles: NobleTileAggregate # type: ignore
    gem_tokens: dict[Token, int] # type: ignore
    gold_tokens: tuple[Token, int] # type: ignore

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.development_cards = CardAggregateByColor() # type: ignore
        self.reserved_development_cards = []
        self.noble_tiles = NobleTileAggregate() # type: ignore
        self.gem_tokens = {token: 0 for token in GEM_TOKEN}} # type: ignore
        self.gold_tokens = (METAL_TOKEN.GOLD, 0) # type: ignore
        
    def move(self, action: ACTION) -> None: # type: ignore
        pass

class ACTION(IntEnum):
    TAKE_3_GEM_TOKENS_OF_DIFFERENT_COLORS = 1
    TAKE_2_GEM_TOKENS_OF_THE_SAME_COLOR = 2
    RESERVE_1_DEVELOPMENT_CARD_AND_TAKE_1_GOLD_TOKEN = 3
    PURCHASE_1_FACE_UP_DEVELOPMENT_CARD_FROM_THE_TABLE = 4
    PURCHASE_1_PREVIOUSLY_RESERVED_DEVELOPMENT_CARD = 5
