from typing import Any

from app.src.components.tokens.exceptions import InsufficientTokensError, TokenMismatchError
from app.src.components.tokens.token_pile import TokenPile, TokenType
from hypothesis import assume, given, strategies as st
import pytest

from app.src.config import TOKEN_INSUFFICIENCY_LIMIT, TOTAL_GEM_TOKEN_COUNT

SCALING_FOR_EDGE_CASES: int = 2
TOKEN_UNDERVALUE_EDGE: int = -SCALING_FOR_EDGE_CASES*TOTAL_GEM_TOKEN_COUNT
TOKEN_OVERVALUE_EDGE: int = SCALING_FOR_EDGE_CASES*TOTAL_GEM_TOKEN_COUNT

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_init_stores_valid_data(type_a, count_a):
    """Verify standard initialization works perfectly."""
    
    if count_a < TOKEN_INSUFFICIENCY_LIMIT:
        pile = TokenPile(type_a, count_a, _bypass_count_validation = True)
        assert pile.token_type == type_a
        assert pile.count == count_a

        with pytest.raises(InsufficientTokensError):
            _ = TokenPile(type_a, count_a)
        return

    pile = TokenPile(type_a, count_a)
    assert pile.token_type == type_a
    assert pile.count == count_a

def test_single_token_creation():
    type_a: TokenType
    count_a: int
    pile_a: TokenPile

    count_a = 1
    for type_a in TokenType:
        pile_a = TokenPile.single(type_a)
        assert pile_a.token_type == type_a
        assert pile_a.count == count_a

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE),
    type_b=st.sampled_from(TokenType),
    count_b=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_token_pile_addition(type_a: TokenType, count_a: int, type_b: TokenType, count_b: int):
    pile_a: TokenPile
    pile_b: TokenPile
    pile_sum: TokenPile
    count_sum: int

    pile_a = TokenPile(type_a, count_a, _bypass_count_validation = True)
    pile_b = TokenPile(type_b, count_b, _bypass_count_validation = True)
    if type_a != type_b or count_a + count_b < TOKEN_INSUFFICIENCY_LIMIT:
        with pytest.raises((TokenMismatchError, InsufficientTokensError)):
            _ = pile_a + pile_b
        return
    
    count_sum = count_a + count_b
    pile_sum = pile_a + pile_b

    assert pile_sum.token_type == type_a == type_b
    assert pile_sum.count == count_sum

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE),
    type_b=st.sampled_from(TokenType),
    count_b=st.integers(min_value=TOKEN_UNDERVALUE_EDGE, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_token_pile_subtraction(type_a: TokenType, count_a: int, type_b: TokenType, count_b: int):
    pile_a: TokenPile
    pile_b: TokenPile
    pile_sum: TokenPile
    count_sum: int

    pile_a = TokenPile(type_a, count_a, _bypass_count_validation = True)
    pile_b = TokenPile(type_b, count_b, _bypass_count_validation = True)
    if type_a != type_b or count_a - count_b < TOKEN_INSUFFICIENCY_LIMIT:
        with pytest.raises((TokenMismatchError, InsufficientTokensError)):
            _ = pile_a - pile_b
        return
    
    count_sum = count_a - count_b
    pile_sum = pile_a - pile_b

    assert pile_sum.token_type == type_a == type_b
    assert pile_sum.count == count_sum

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_INSUFFICIENCY_LIMIT, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_token_pile_negetion(type_a: TokenType, count_a: int):
    pile_a: TokenPile
    pile_b: TokenPile

    pile_a = TokenPile(type_a, count_a)
    pile_b = -pile_a

    assert pile_b.count == -count_a
    assert pile_b.token_type == type_a

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_INSUFFICIENCY_LIMIT, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_eq_identical_piles(type_a, count_a):
    """Two different instances with identical data must be equal."""
    pile_a = TokenPile(type_a, count_a)
    pile_a_ = TokenPile(type_a, count_a)
    
    assert pile_a == pile_a_

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_INSUFFICIENCY_LIMIT, max_value=TOKEN_OVERVALUE_EDGE),
    count_b=st.integers(min_value=TOKEN_INSUFFICIENCY_LIMIT, max_value=TOKEN_OVERVALUE_EDGE)
)
def test_eq_different_counts(type_a, count_a, count_b):
    """Piles with different counts must not be equal."""
    assume(count_a != count_b)

    pile_a = TokenPile(type_a, count_a)
    pile_a_ = TokenPile(type_a, count_b)
    
    assert pile_a != pile_a_

@given(
    type_a=st.sampled_from(TokenType),
    count_a=st.integers(min_value=TOKEN_INSUFFICIENCY_LIMIT, max_value=TOKEN_OVERVALUE_EDGE),
    # Generate random strings, ints, floats, lists, or None
    wrong_object=st.one_of(
        st.text(), 
        st.integers(), 
        st.floats(), 
        st.lists(st.integers()),
        st.none()
    )
)
def test_eq_against_arbitrary_objects(type_a, count_a, wrong_object):
    """A TokenPile compared to any completely different type must safely return False."""
    pile_a = TokenPile(type_a, count_a)
    
    assert (pile_a == wrong_object) is False