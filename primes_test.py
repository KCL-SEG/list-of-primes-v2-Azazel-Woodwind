"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from primes import primes
import pytest

def test_1_primes():
    actual = primes(1)
    expected = [2]
    assert actual == expected

def test_2_primes():
    actual = primes(2)
    expected = [2, 3]
    assert actual == expected

def test_20_primes():
    actual = primes(20)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                53, 59, 61, 67, 71]
    assert actual == expected

def test_negative_input():
    with pytest.raises(ValueError):
        primes(-1)

def test_zero_input():
    with pytest.raises(ValueError):
        primes(0)
