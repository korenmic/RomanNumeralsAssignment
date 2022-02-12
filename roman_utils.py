"""
roman_utils deals with infrastructure used to convert numbers
from integer values to roman numerals representations, and back to integers
via the roman_encode and roman_decode methods
"""

from typing import Iterator


reversed_pairs = lambda pairs: [tuple(reversed(pair)) for pair in pairs]


ROMAN_TO_DIGITS = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
    }

DIGITS_TO_ROMAN = dict(reversed_pairs(ROMAN_TO_DIGITS.items()))


def _encode_roman_digit(digit: int, power: int) -> str:
    power_value = 10**power
    get_current_power = lambda : DIGITS_TO_ROMAN[power_value]
    get_middle_power = lambda : DIGITS_TO_ROMAN[power_value*5]
    get_next_power = lambda : DIGITS_TO_ROMAN[power_value*10]

    if 0 <= digit < 4:  # pylint: disable=no-else-return
        return get_current_power() * digit
    elif digit == 4:
        return get_current_power() + get_middle_power()
    elif digit == 5:
        return get_middle_power()
    elif 6 <= digit < 9:
        return get_middle_power() + get_current_power()*(digit - 5)
    elif digit == 9:
        return get_current_power() + get_next_power()
    else:
        raise ValueError(f'Digit {digit} has unencodeable value')


def _iter_digit_power(integer: int) -> Iterator[tuple[int, int]]:
    string_integer = str(integer)
    for (index, digit) in enumerate(map(int, string_integer)):
        power = len(string_integer) - index - 1
        yield digit, power


def roman_encode(integer: int) -> str:
    """
    Converts an integer value to a Roman numeral string representation
    """
    encoded_roman_digits = [_encode_roman_digit(digit, power) \
                            for (digit, power) in _iter_digit_power(integer)]
    return ''.join(encoded_roman_digits)


def roman_decode(roman_number: str) -> int:
    """
    Converts a Roman numeral string representation to an integer value
    """
    integer = 0
    index = 0
    while index < len(roman_number):
        current_digit = roman_number[index]
        current_digit_value = ROMAN_TO_DIGITS[current_digit]
        next_digit_value = ROMAN_TO_DIGITS[roman_number[index + 1]] \
            if index + 1 < len(roman_number) else 0

        if next_digit_value > current_digit_value:
            integer += next_digit_value - current_digit_value
            index += 1
        else:
            integer += current_digit_value

        index += 1
    return integer
