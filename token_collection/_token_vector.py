from token_collection._token import _Token
from typing import Self

class _TokenVector:
    """
    TokenVector class representing a collection of tokens.
    This collection is able to be added and subtracted item-wise from another of its type.
    It's also able to be multiplied by a scalar.
    It's can also be compared to another of its type (partial order).
    """
    _tokens: dict[_Token, int]

    def __init__(self: Self):
        self._tokens = dict()

    @property
    def tokens(self: Self) -> dict[_Token, int]:
        return self._tokens
    
    @tokens.setter
    def tokens(self: Self, tokens: dict[_Token, int]):
        self._tokens = tokens

    @tokens.deleter
    def tokens(self: Self):
        self._tokens = dict()

    @classmethod
    def from_tokens(cls: type[Self], tokens: dict[_Token, int]) -> Self:
        result = cls()
        result.tokens = tokens
        return result
    
    def __neg__(self: Self) -> Self:
        result = _TokenVector()
        result.tokens = { token: -count for token, count in self.tokens.items() }
        return result

    def __add__(self: Self, other: Self) -> Self:
        result = _TokenVector()
        result.tokens = self.tokens
        for token, count in other.tokens.items():
            if token in result.tokens:
                result.tokens[token] += count
            else:
                result.tokens[token] = count
        return result

    def __sub__(self: Self, other: Self) -> Self:
        return self + (-other)
    
    def __mul__(self: Self, scalar: int) -> Self:
        result = _TokenVector()
        result.tokens = { token: count * scalar for token, count in self.tokens.items() }
        return result
    
    def magnitude(self: Self) -> int:
        return sum(self.tokens.values())
    
    def __eq__(self: Self, other: Self) -> bool:
        return self.tokens == other.tokens
    
    def __le__(self: Self, other: Self) -> bool:
        if any(token not in other.tokens for token in self.tokens.keys()):
            return False
        
        return all(self.tokens[token] <= other.tokens[token] for token in self.tokens.keys())
    
    def __ge__(self: Self, other: Self) -> bool:
        return other <= self
    
    def __str__(self: Self) -> str:
        if len(self.tokens) == 0 or all(count == 0 for count in self.tokens.values()):
            return 'No tokens'
        
        return '; '.join([
            f'{ token.__str__() }: { count }' 
            for token, count in self.tokens.items() 
            if count > 0
        ])
    
    def __repr__(self: Self) -> str:
        return ';\n'.join([f'{ token.__repr__() }' for token in self.tokens ])
    
