from contents.token.token_enum import Token
from token_collection._token_vector import _TokenVector
if __name__ == "__main__":
    token_vector = _TokenVector()
    token_vector.tokens = { Token.SAPPHIRE: 1, Token.EMERALD: 2 }

    token_vector2 = _TokenVector()
    token_vector2.tokens = { Token.SAPPHIRE: 3, Token.ONYX: 1 }
    
    print(f'{token_vector}\n')
    print(f'{token_vector2}\n')
    print(f'{token_vector + token_vector2}\n')
    print(f'{-token_vector}\n')
    print(f'{token_vector * 2}\n')
    print(f'{token_vector * -2}\n')
    print(f'{token_vector * 0}\n')
    print(f'{token_vector * 1}')
