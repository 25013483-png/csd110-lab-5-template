def is_1_to_9(value):
    """Return True when value is an integer or string from 1 to 9."""
    if type(value) is int:
        return 1 <= value <= 9
    if type(value) is str:
        return value in ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    return False