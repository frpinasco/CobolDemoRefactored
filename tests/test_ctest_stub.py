"""Unit tests for ctest_stub — TF-005."""

import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.ctest_stub import ctest


@pytest.mark.parametrize("value, expected_output", [
    (1337, "ctest called with: 1337\n"),  # AC-005-1: original COBOL argument
    (0,    "ctest called with: 0\n"),     # AC-005-2: zero
    (42,   "ctest called with: 42\n"),    # AC-005-3: arbitrary value
])
def test_ctest_prints_confirmation(capsys, value: int, expected_output: str) -> None:
    """ctest prints 'ctest called with: {value}' to stdout."""
    ctest(value)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_ctest_returns_none() -> None:
    """ctest returns None (void function matching COBOL CALL semantics)."""
    result = ctest(1337)
    assert result is None
