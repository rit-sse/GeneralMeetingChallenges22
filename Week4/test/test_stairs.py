import pytest
from src.stairs import stairs

"""test_stairs() is responsible for running testcases to test the validity
of students code for the challenge submission.
"""


def test_n_equals_one():
    assert stairs(1) == [[1]]


def test_n_equals_two():
    assert stairs(2) == [[1, 1], [2]]


def test_n_equals_three():
    assert stairs(3) == [[1, 2], [1, 1, 1], [2, 1]]


def test_n_equals_four():
    assert stairs(4) == [[1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1]]
