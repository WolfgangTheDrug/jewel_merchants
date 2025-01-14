from contents.cards.noble_tile import NobleTile
from contents.token.token_enum import Token
from token_collection._token_vector import _TokenVector
from contents.cards.development_card import DevelopmentCard
from util.card import Card

if __name__ == "__main__":
    card1: DevelopmentCard = DevelopmentCard(1, 1, {Token.SAPPHIRE: 1, Token.EMERALD: 2, Token.ONYX: 3}, Token.ONYX)
    print(card1)

    card2: NobleTile = NobleTile(1, {Token.SAPPHIRE: 1, Token.EMERALD: 2, Token.ONYX: 3})
    print(card2)

