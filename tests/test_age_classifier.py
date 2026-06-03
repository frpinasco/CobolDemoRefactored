"""Unit tests for age_classifier — TF-001."""

import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.age_classifier import classify_age


# ---------------------------------------------------------------------------
# Valid inputs — happy path
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("age, expected", [
    (18, "ADULT"),   # AC-001-1: adult boundary
    (25, "ADULT"),   # AC-001-2: mid-range adult
    (99, "ADULT"),   # upper boundary
    (13, "TEEN"),    # AC-001-3: teen boundary
    (16, "TEEN"),    # AC-001-4: mid-range teen
    (17, "TEEN"),    # teen upper boundary
    (12, "CHILD"),   # AC-001-5: child boundary
    (5,  "CHILD"),   # AC-001-6: mid-range child
    (0,  "CHILD"),   # lower boundary
])
def test_classify_age_valid(age: int, expected: str) -> None:
    """classify_age returns the correct group for valid ages."""
    assert classify_age(age) == expected


# ---------------------------------------------------------------------------
# Invalid inputs — error path
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("bad_age", [
    -1,       # AC-001-7: below range
    100,      # AC-001-8: above range
    "abc",    # AC-001-9: non-integer string
    3.5,      # float
    None,     # None type
    True,     # bool (subclass of int — must be rejected)
])
def test_classify_age_invalid_raises_value_error(bad_age) -> None:
    """classify_age raises ValueError for invalid inputs."""
    with pytest.raises(ValueError):
        classify_age(bad_age)
