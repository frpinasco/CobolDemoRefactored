"""Unit tests for countdown — TF-002."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.countdown import countdown, display_countdown


def test_countdown_default_yields_3_2_1() -> None:
    """AC-002-1: countdown(3) yields [3, 2, 1]."""
    result = list(countdown(3))
    assert result == [3, 2, 1]


def test_countdown_single_iteration_do_while() -> None:
    """AC-002-2: countdown(1) yields [1] — do-while executes body at least once."""
    result = list(countdown(1))
    assert result == [1]


def test_countdown_terminates_after_correct_iterations() -> None:
    """AC-002-4: countdown(3) terminates after exactly 3 iterations."""
    values = list(countdown(3))
    assert len(values) == 3


def test_display_countdown_output(capsys) -> None:
    """AC-002-3: display_countdown(3) prints the correct three lines."""
    display_countdown(3)
    captured = capsys.readouterr()
    assert captured.out == "Counting down ... 3\nCounting down ... 2\nCounting down ... 1\n"


def test_countdown_start_5() -> None:
    """countdown(5) yields [5, 4, 3, 2, 1]."""
    result = list(countdown(5))
    assert result == [5, 4, 3, 2, 1]
