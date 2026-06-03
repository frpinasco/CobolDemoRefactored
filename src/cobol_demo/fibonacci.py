"""Fibonacci Sequence — F-003.

Generates the Fibonacci sequence for positions 1-10 and displays
only positions 6-10, matching the COBOL analysis report expected output:
  FIBONACCI 6 : 5
  FIBONACCI 7 : 8
  FIBONACCI 8 : 13
  FIBONACCI 9 : 21
  FIBONACCI 10 : 34

Algorithm: display-before-update, matching the COBOL expected output
(analysis report section 4.3 and BR-003 acceptance criteria).
"""

from typing import Generator


def fibonacci_sequence(count: int = 10) -> Generator[tuple[int, int], None, None]:
    """Yield (position, value) pairs for Fibonacci positions 1..count.

    Uses display-before-update semantics to match the COBOL program's
    expected output. The value yielded at each position is the Fibonacci
    number BEFORE the update step for that iteration.

    Full sequence for count=10:
        (1,0), (2,1), (3,1), (4,2), (5,3),
        (6,5), (7,8), (8,13), (9,21), (10,34)

    Args:
        count: Number of positions to generate (default 10).

    Yields:
        Tuples of (position, fibonacci_value).
    """
    nr, last = 0, 1
    for i in range(1, count + 1):
        yield i, nr          # yield BEFORE updating (matches COBOL expected output)
        temp = nr
        nr = nr + last
        last = temp


def display_fibonacci(count: int = 10, skip: int = 5) -> None:
    """Print 'FIBONACCI N : value' for positions greater than skip.

    Args:
        count: Total number of Fibonacci positions to generate (default 10).
        skip: Only print positions where position > skip (default 5).
    """
    for pos, val in fibonacci_sequence(count):
        if pos > skip:
            print(f"FIBONACCI {pos} : {val}")
