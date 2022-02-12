"""
This module contains pytest tests of the roman_utils methods
roman_encode and roman_deocde
Tests will use each one in passing scenarios and failing scenarios
as well as using them both together in an encoding-decoding scenario
"""

import pytest

from roman_utils import DIGITS_TO_ROMAN, reversed_pairs, roman_encode, roman_decode


VALID_INTEGERS = range(min(DIGITS_TO_ROMAN.keys()), max(DIGITS_TO_ROMAN.keys()))

ENCODING_EXAMPLES = tuple(DIGITS_TO_ROMAN.items()) + ((1954, 'MCMLIV'), (1990, 'MCMXC'))
DECODING_EXAMPLES = reversed_pairs(ENCODING_EXAMPLES)


@pytest.mark.parametrize('integer,expected_encoding', ENCODING_EXAMPLES)
def test_sanity_encode(integer: int, expected_encoding: str):
    """ Test roman encoding, conversion from integer values to Roman numerals values """
    actual_encoding = roman_encode(integer)
    assert actual_encoding == expected_encoding, \
        'Failed encoding as expected, with values: ' \
        f'{integer=}, {expected_encoding=}, {actual_encoding=}'


@pytest.mark.parametrize('integer,expected_decoding', DECODING_EXAMPLES)
def test_sanity_decode(integer: int, expected_decoding: str):
    """ Test roman decoding scenarios, conversion from Roman numerals values to integer values """
    actual_decoding = roman_decode(integer)
    assert actual_decoding == expected_decoding, \
        'Failed decoding as expected, with values: ' \
        f'{integer=}, {expected_decoding=}, {actual_decoding=}'


def test_unsupported_normal():
    """ Test unsupported normal value encoding failure """
    try:
        roman_encode(max(VALID_INTEGERS) + 1)
    except KeyError:
        pass


def test_unsupported_negative():
    """ Test unsupported negative value encoding failure """
    try:
        roman_encode(-1)
    except ValueError:
        pass


@pytest.mark.parametrize('illegal_roman_strings', ('a', 'IV9', 'CM<'))
def test_illegal_decode(illegal_roman_strings):
    """ Test illegal values for decoding failures """
    try:
        roman_decode(illegal_roman_strings)
    except KeyError:
        pass


def test_sanity_all():
    """ Test all supported roman encoding and decoding values """
    for integer in VALID_INTEGERS:
        encoded_value = roman_encode(integer)
        decoded_value = roman_decode(encoded_value)
        assert decoded_value == integer, \
            'Failed expected encoding->decoding with values: ' \
            f'{integer=}, {encoded_value=}, {decoded_value=}'
