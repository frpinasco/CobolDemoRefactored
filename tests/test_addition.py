"""Unit tests for addition — TF-004."""

import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.addition import validate_integer, add_two_integers, format_result, run_addition


# ---------------------------------------------------------------------------
# validate_integer — happy path
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("raw, expected", [
    ("0", 0),
    ("1", 1),
    ("50", 50),
    ("99", 99),
])
def test_validate_integer_valid(raw: str, expected: int) -> None:
    """AC-004-7: validate_integer returns correct int for valid inputs."""
    assert validate_integer(raw, "test") == expected


# ---------------------------------------------------------------------------
# validate_integer — error path
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("bad_input", [
    "abc",     # AC-004-4: non-numeric
    "",        # empty string
    "1.5",     # float string
    " ",       # whitespace
])
def test_validate_integer_non_numeric_raises(bad_input: str) -> None:
    """AC-004-4: validate_integer raises ValueError for non-numeric input."""
    with pytest.raises(ValueError):
        validate_integer(bad_input, "test")


@pytest.mark.parametrize("bad_input", [
    "-1",   # AC-004-5: below range
    "-99",
])
def test_validate_integer_below_range_raises(bad_input: str) -> None:
    """AC-004-5: validate_integer raises ValueError for values below 0."""
    with pytest.raises(ValueError):
        validate_integer(bad_input, "test")


@pytest.mark.parametrize("bad_input", [
    "100",  # AC-004-6: above range
    "999",
])
def test_validate_integer_above_range_raises(bad_input: str) -> None:
    """AC-004-6: validate_integer raises ValueError for values above 99."""
    with pytest.raises(ValueError):
        validate_integer(bad_input, "test")


# ---------------------------------------------------------------------------
# add_two_integers
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (25, 17, 42),
    (99, 99, 198),
    (1, 1, 2),
])
def test_add_two_integers(a: int, b: int, expected: int) -> None:
    """add_two_integers returns the correct sum."""
    assert add_two_integers(a, b) == expected


# ---------------------------------------------------------------------------
# format_result
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("val1, val2, expected", [
    (25, 17, "RESULT: 25 + 17 = 42"),   # AC-004-1
    (0, 0, "RESULT: 0 + 0 = 0"),        # AC-004-2
    (99, 99, "RESULT: 99 + 99 = 198"),  # AC-004-3
])
def test_format_result(val1: int, val2: int, expected: str) -> None:
    """format_result returns the correctly formatted string."""
    assert format_result(val1, val2) == expected


# ---------------------------------------------------------------------------
# run_addition — integration via monkeypatch
# ---------------------------------------------------------------------------

def test_run_addition_interactive(monkeypatch, capsys) -> None:
    """run_addition prompts, reads two integers, and prints the result."""
    inputs = iter(["25", "17"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run_addition()
    captured = capsys.readouterr()
    assert "RESULT: 25 + 17 = 42" in captured.out
