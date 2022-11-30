import logging
from collections import deque

from decorators import timeit


def gest_form(numbers: list) -> str:
    """
    Input a list of numbers and returns a joined string with converted numbers,
    based on their values.
    """
    # Improve performance with a deque instead of a list
    result: deque = deque()
    for number in numbers:
        try:
            if number < -1000 or number > 1000:
                logging.error(f"{number} is not accepted")
                raise ValueError
        except TypeError:
            logging.error(f"Wrong type for: {number}")
            raise
        if number % 15 == 0:
            result.append("Gestform")
        elif number % 3 == 0:
            result.append("Geste")
        elif number % 5 == 0:
            result.append("Forme")
        else:
            result.append(str(number))
    return "".join(result)


def binary_gap(number: int) -> int:
    """

    :rtype: object
    """
    try:
        binary_string: str = str(bin(number)[2:])
    except TypeError:
        logging.error(f"Wrong type for: {number}")
        raise TypeError
    max_gap: int = 0
    current_gap: int = 0
    for n in binary_string:
        if int(n) == 1:
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        elif int(n) == 0:
            current_gap += 1
    return max_gap