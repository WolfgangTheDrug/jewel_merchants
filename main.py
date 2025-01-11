from contents.token.token_enum import Token
from token_collection._token_vector import _TokenVector
if __name__ == "__main__":
    token_vector = _TokenVector()
    token_vector.tokens = { Token.SAPPHIRE: 1, Token.EMERALD: 2, Token.ONYX: 3 }

    token_vector2 = _TokenVector()
    token_vector2.tokens = { Token.SAPPHIRE: 2, Token.EMERALD: 2 }
    
    print(f'{token_vector}\n')
    print(f'{token_vector2}\n')
    print(f'{token_vector <= token_vector2}')
