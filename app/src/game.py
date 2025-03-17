from app.src.player import ACTION, Player


class Game:
    players: list[Player]
    development_cards: CardAggregateByLevel # type: ignore
    noble_tiles: NobleTileAggregate # type: ignore
    gem_tokens: dict[Token, int] # type: ignore
    gold_tokens: tuple[Token, int] # type: ignore
    turn: int

    def __init__(self) -> None:
        players_count: int
        gem_token_count: int
        noble_tiles_count: int
        player: Player
        player_id: int
        player_name: str

        players_count = input("Provide the number of players: ")
        while players_count < 2 or players_count > 4 or not isinstance(input, int):
            players_count = input("The provided number of players is incorrect.\nPlease provide a valid number (2, 3, 4): ")

        noble_tiles_count = players_count + 1
        gem_token_count =   4 if players_count == 2 else \
                            5 if players_count == 3 else \
                            7
        self.players = []
        for i in range(players_count):
            player_id = i+1
            player_name = input(f"Enter Player's {player_id} name: ")
            while not player_name.strip():
                player_name = input(f"The provided player name is incorrect.\nPlease enter a valid name for Player {player_id}: ")

            player = Player(player_id, player_name)
            self.players.append(player)
            
        self.development_cards = CardAggregateByLevel()
        self.noble_tiles = NobleTileAggregate(noble_tiles_count)
        self.gem_tokens = {token: gem_token_count for token in GEM_TOKEN}
        self.gold_tokens = (METAL_TOKEN.GOLD, 5)
        self.turn = 0

    def run(self) -> None:
        
        while not self.is_finished():
            self.next_turn()
        
        self.end()

    def next_turn(self) -> None:
        player_id: int

        player_id = (self.turn + 1) % len(self.players)
        self.request_move(player_id)

    def request_move(self, player_id: int) -> None: # type: ignore
        player_input: str
        action: ACTION
        player: Player 
        
        print(f"Player's {player_id} move.")
        player_input = input("Please enter the move (1, 2, 3, 4): ")
        action = ACTION(int(player_input))
        player = self.players[ player_id ].move()

    def end(self) -> None:
        pass

    def is_finished(self) -> bool:
        return self.players[ self.turn ].prestige_points == 15