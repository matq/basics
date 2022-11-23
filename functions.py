import logging
from collections import deque


def gest_form(numbers: list) -> str:
    """
    Input a list of numbers and returns a joined string with converted numbers,
    based on their values.
    """
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
