from typing import Any

from app.src.components.tokens.exceptions import InsufficientTokensError, TokenMismatchError
from app.src.components.tokens.token_pile import TokenPile, TokenType
from hypothesis import given, strategies as st
import pytest

from app.src.config import TOKEN_INSUFFICIENCY_LIMIT, TOTAL_GEM_TOKEN_COUNT

SCALING_FOR_EDGE_CASES: int = 2
TOKEN_UNDERVALUE_EDGE: int = -SCALING_FOR_EDGE_CASES*TOTAL_GEM_TOKEN_COUNT
TOKEN_OVERVALUE_EDGE: int = SCALING_FOR_EDGE_CASES*TOTAL_GEM_TOKEN_COUNT

@given(
    token_type=st.sampled_from(TokenType),
    count=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_init_stores_valid_data(token_type, count):
    """Verify standard initialization works perfectly."""
    
    if count < TOKEN_INSUFFICIENCY_LIMIT:
        pile = TokenPile(token_type, count, _bypass_count_validation = True)
        assert pile.type == token_type
        assert pile.count == count

        with pytest.raises(InsufficientTokensError):
            _ = TokenPile(token_type, count)

    pile = TokenPile(token_type, count)
    assert pile.type == token_type
    assert pile.count == count

@given(
    count_a=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE),
    type_a=st.sampled_from(TokenType),
    count_b=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE),
    type_b=st.sampled_from(TokenType),
)
def test_token_pile_addition(type_a: TokenType, count_a: int, type_b: TokenType, count_b: int):
    pile_a: TokenPile
    pile_b: TokenPile
    pile_sum: TokenPile
    count_sum: int

    pile_a = TokenPile(type_a, count_a, _bypass_count_validation = True)
    pile_b = TokenPile(type_b, count_b, _bypass_count_validation = True)
    if type_a != type_b or count_a - count_b < TOKEN_INSUFFICIENCY_LIMIT:
        with pytest.raises((TokenMismatchError, InsufficientTokensError)):
            _ = pile_a + pile_b

    count_sum = count_a + count_b
    pile_sum = pile_a + pile_b

    assert pile_sum.type == type_a == type_b
    assert pile_sum.count == count_sum