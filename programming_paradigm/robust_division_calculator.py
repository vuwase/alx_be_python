def safe_divide(numerator, denominator):
    """Performs division with error handling for zero division and invalid inputs."""

    try:
        # Convert inputs to floats (will raise ValueError if invalid)
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

