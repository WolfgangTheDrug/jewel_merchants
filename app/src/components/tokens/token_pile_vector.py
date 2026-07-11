from app.src.components.tokens.token_pile import TokenPile, TokenType


class TokenVector:
    """Represents a multi-set collection of tokens (e.g., a price, a wallet, or a bank)."""
    _gem_tokens: list[TokenPile]
    _gold_tokens: TokenPile

    def __init__(self) -> None:
        *self._gem_tokens, self._gold_tokens = [TokenPile(token_type) for token_type in TokenType]

    @classmethod
    def fromDict(cls, gems_counts: dict[TokenType, int], gold_count: int = 0):
        c = cls()
        c._gem_tokens = [TokenPile(token_type, gems_counts.get(token_type, 0)) for token_type in TokenType]
        c._gold_tokens = TokenPile(TokenType.GOLD, gold_count)
        return c