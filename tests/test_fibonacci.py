"""Unit tests for fibonacci — TF-003."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.fibonacci import fibonacci_sequence, display_fibonacci


def test_fibonacci_sequence_full_10() -> None:
    """AC-003-1: fibonacci_sequence(10) yields the correct (position, value) pairs.

    Expected sequence (display-before-update algorithm):
    pos 1 -> 0, pos 2 -> 1, pos 3 -> 1, pos 4 -> 2, pos 5 -> 3,
    pos 6 -> 5, pos 7 -> 8, pos 8 -> 13, pos 9 -> 21, pos 10 -> 34
    """
    expected = [
        (1, 0), (2, 1), (3, 1), (4, 2), (5, 3),
        (6, 5), (7, 8), (8, 13), (9, 21), (10, 34),
    ]
    result = list(fibonacci_sequence(10))
    assert result == expected


def test_display_fibonacci_output(capsys) -> None:
    """AC-003-2: display_fibonacci(10, skip=5) prints exactly 5 lines for positions 6-10."""
    display_fibonacci(10, skip=5)
    captured = capsys.readouterr()
    expected = (
        "FIBONACCI 6 : 5\n"
        "FIBONACCI 7 : 8\n"
        "FIBONACCI 8 : 13\n"
        "FIBONACCI 9 : 21\n"
        "FIBONACCI 10 : 34\n"
    )
    assert captured.out == expected


def test_display_fibonacci_does_not_print_skipped_positions(capsys) -> None:
    """AC-003-3: display_fibonacci does not print positions 1-5."""
    display_fibonacci(10, skip=5)
    captured = capsys.readouterr()
    for i in range(1, 6):
        assert f"FIBONACCI {i} :" not in captured.out


def test_fibonacci_sequence_positions_6_to_10_values() -> None:
    """Verify the specific values for the displayed positions."""
    pairs = {pos: val for pos, val in fibonacci_sequence(10)}
    assert pairs[6] == 5
    assert pairs[7] == 8
    assert pairs[8] == 13
    assert pairs[9] == 21
    assert pairs[10] == 34
