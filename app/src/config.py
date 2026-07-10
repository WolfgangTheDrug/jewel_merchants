from typing import Dict

# Components counts
TOTAL_NOBLE_TILE_COUNT: int = 10
TOTAL_DEVELOPMENT_CARDS_COUNT: int = 90
TOTAL_DEVELOPMENT_CARDS_LVL1_COUNT: int = 40
TOTAL_DEVELOPMENT_CARDS_LVL2_COUNT: int = 30
TOTAL_DEVELOPMENT_CARDS_LVL3_COUNT: int = 20
TOTAL_TOKEN_COUNT: int = 40
TOTAL_GOLD_TOKEN_COUNT: int = 5
TOTAL_GEM_TOKEN_COUNT: int = 7

# No object can have the token count below this threshold unless explicitly forced to
TOKEN_INSUFFICIENCY_LIMIT: int = 0

# The absolute limit a single player's inventory can hold at the end of a turn
PLAYER_TOKEN_LIMIT: int = 10

# Bank token counts vary dynamically by player count according to the game's rules
BANK_LIMITS: Dict[int, Dict[str, int]] = {
    2: {"standard": 4, "gold": 5},
    3: {"standard": 5, "gold": 5},
    4: {"standard": 7, "gold": 5},
}