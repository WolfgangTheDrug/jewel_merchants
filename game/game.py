from typing import Literal, Self
from board.board import Board
from contents.cards.development_card import DevelopmentCard
from contents.cards.noble_tile import NobleTile
from player.player import Player
from token_collection._token_vector import _TokenVector


class Game:
    _board: Board
    _players: list[Player]
    _players_count: Literal[1, 2, 3, 4]
    _current_player_idx: Literal[1, 2, 3, 4]

    def __init__(self: Self, noble_tiles: list[NobleTile], development_cards: dict[int, list[DevelopmentCard]], players: list[Player]) -> None:
        self._board = Board(noble_tiles, development_cards, len(players))
        self._players = players
        self._players_count = len(players)
        self._current_player_idx = 0
        

    def play(self: Self) -> None:
        while True:
            self._players[self._current_player_idx].move()
            if self.is_over(): break
            self.next_player()
        
        self.end()

    def next_player(self: Self) -> None:
        self._current_player_idx = (self._current_player_idx + 1) % self._players_count

    def is_over(self: Self) -> bool:
        return self._players[self._current_player_idx]
    
    def end(self: Self) -> None:
        print(f'Player {self._current_player_idx} won!')
    

        
