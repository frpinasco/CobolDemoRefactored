"""Age Group Classification — F-001.

Classifies an integer age (0-99) into ADULT, TEEN, or CHILD.
"""


def classify_age(age: int) -> str:
    """Classify age into ADULT, TEEN, or CHILD.

    Args:
        age: Integer between 0 and 99 inclusive.

    Returns:
        "ADULT" if age >= 18.
        "TEEN"  if 13 <= age < 18.
        "CHILD" if 0 <= age < 13.

    Raises:
        ValueError: If age is not an integer, or is outside the range [0, 99].
    """
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError(f"Age must be an integer between 0 and 99, got: {age!r}")
    if age < 0 or age > 99:
        raise ValueError(f"Age must be between 0 and 99, got: {age}")
    if age >= 18:
        return "ADULT"
    if age >= 13:
        return "TEEN"
    return "CHILD"
