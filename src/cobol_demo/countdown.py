"""Countdown Loop — F-002.

Counts down from a starting value to 1 with do-while semantics:
the body executes at least once before checking the exit condition,
matching COBOL PERFORM...UNTIL WITH TEST AFTER behaviour.
"""

from typing import Generator


def countdown(start: int = 3) -> Generator[int, None, None]:
    """Yield countdown values from start down to 1 (do-while semantics).

    The body always executes at least once (equivalent to COBOL
    PERFORM WITH TEST AFTER UNTIL counter = 0).

    Args:
        start: Starting value for the countdown (default 3).

    Yields:
        Integer values from start down to 1 inclusive.
    """
    counter = start
    while True:
        yield counter
        counter -= 1
        if counter == 0:
            break


def display_countdown(start: int = 3) -> None:
    """Print 'Counting down ... N' for each value in countdown(start).

    Args:
        start: Starting value for the countdown (default 3).
    """
    for n in countdown(start):
        print(f"Counting down ... {n}")
