"""
This module deals with testing some of the functions in the snake_view
module.
"""
import pytest
from snake_view import * #Change this to have functions

FUNCTION_1_CASES = [
    ("",""),
    ("",""),
]

@pytest.mark.parametrize("test_input,expected", FUNCTION_1_CASES)
def test_function_1(test_input, expected):
    """
    """
    #assert function1(test_input) == expected