import pytest
from src.url_replacer import replacer

"""test_url_replacer is a test suite responsible for checking the validity of a students
code submission. This suite is responsible for testing using pytest to run unit tests on the given
function in url_replacer.py
"""


def test_sse_replace():
    """test_sse_replace(): is a test that is responsible for testing to see if
    the spaces that are in 'Society of Software Engineers' are replaced with the following
    character sequence '%20'. This function will assert if the output of the function matches.
    """
    input_str = "Society of Software Engineers"
    output_str = "Society%20of%20Software%20Engineers"
    output = replacer(input_str)
    assert output == output_str
