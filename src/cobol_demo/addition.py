"""Two-Integer Addition with Validation — F-004.

Accepts two integers (0-99 each), validates them, adds them, and
displays the result. Adds input validation that was missing in the
original COBOL program (Enhancement BR-004a).
"""


def validate_integer(value: str, label: str) -> int:
    """Parse and validate a user-supplied string as an integer in [0, 99].

    Args:
        value: The raw string input from the user.
        label: A label for error messages (e.g., "Input 1").

    Returns:
        The validated integer value.

    Raises:
        ValueError: If value is non-numeric, less than 0, or greater than 99.
    """
    try:
        parsed = int(value)
    except (ValueError, TypeError):
        raise ValueError(
            f"{label}: '{value}' is not a valid integer. Must be numeric."
        )
    if parsed < 0:
        raise ValueError(
            f"{label}: {parsed} is below the minimum allowed value of 0."
        )
    if parsed > 99:
        raise ValueError(
            f"{label}: {parsed} exceeds the maximum allowed value of 99."
        )
    return parsed


def add_two_integers(val1: int, val2: int) -> int:
    """Return the sum of val1 and val2.

    Args:
        val1: First integer operand.
        val2: Second integer operand.

    Returns:
        The integer sum.
    """
    return val1 + val2


def format_result(val1: int, val2: int) -> str:
    """Format the addition result as 'RESULT: val1 + val2 = sum'.

    Args:
        val1: First integer operand.
        val2: Second integer operand.

    Returns:
        Formatted result string, e.g., 'RESULT: 25 + 17 = 42'.
    """
    total = add_two_integers(val1, val2)
    return f"RESULT: {val1} + {val2} = {total}"


def run_addition() -> None:
    """Interactively prompt for two integers and print the result.

    Prompts the user for two integers (0-99 each), validates input,
    computes the sum, and prints the formatted result.
    """
    raw1 = input("INPUT Nr.1! Max is 99: ")
    val1 = validate_integer(raw1, "Input 1")
    raw2 = input("INPUT Nr.2! Max is 99: ")
    val2 = validate_integer(raw2, "Input 2")
    print(format_result(val1, val2))
