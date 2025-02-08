from typing import Self
from board.board import Board
from contents.cards.development_card import DevelopmentCard
from contents.cards.noble_tile import NobleTile
from player.player import Player
from token_collection._token_vector import _TokenVector


class Game:
    _board: Board
    _players: list[Player]
    _turn_count: int

    def __init__(self: Self, noble_tiles: list[NobleTile], development_cards: dict[int, list[DevelopmentCard]], players: list[Player]) -> None:
        self._board = Board(noble_tiles, development_cards, len(players))
        self._players = players
        self._turn_count = 0
        
    def start():
        pass

    def next_player():
        pass

    def is_over():
        pass
    
    

        
