import pytest
import util

TYPE_HINT = ("Check the type of the value (e.g. `type(value) == int`) before comparing it with numbers, "
             "and use `and` so that the comparison only happens when the type is right.")
INT_HINT = ("int() converts more strings than just '1' to '9' (and crashes on others). Instead of converting "
            "the string, check whether it is one of the strings '1' to '9'.")


def is_1_to_9(value):
  """Call the is_1_to_9 function defined in src/q1.py"""
  function = util.get_student_function("q1", "is_1_to_9", "Part 1")
  return util.call(function, value, hints={TypeError: TYPE_HINT, ValueError: INT_HINT})


def check(values, expected, reason):
  for value in values:
    util.check_returned(f"is_1_to_9({value!r})", is_1_to_9(value), expected, reason)


def test_is_1_to_9_is_defined():
  util.get_student_function("q1", "is_1_to_9", "Part 1")


def test_is_1_to_9_takes_one_parameter():
  function = util.get_student_function("q1", "is_1_to_9", "Part 1")
  util.check_parameter_count(function, 1, "the value to check")


def test_is_1_to_9_has_a_docstring():
  util.get_student_function("q1", "is_1_to_9", "Part 1")
  util.check_has_docstring("q1", "is_1_to_9")


def test_is_1_to_9_returns_instead_of_printing(capsys):
  function = util.get_student_function("q1", "is_1_to_9", "Part 1")
  util.check_returns_instead_of_printing(capsys, function, 5)


def test_is_1_to_9_returns_a_boolean():
  for value in [5, 0]:
    result = is_1_to_9(value)
    assert isinstance(result, bool), (
        f"is_1_to_9({value!r}) returned {result!r} ({util.a_or_an(type(result).__name__)}). It must return True or False "
        f"(a bool, without quotes).")


# Integers
def test_integers_1_to_9_are_valid():
  check([1, 5, 9, 2, 3, 4, 6, 7, 8], True, "The integers 1 to 9 are valid.")


def test_other_integers_are_not_valid():
  check([0, 10, -1, -5, 100], False, "Only the integers 1 to 9 are valid.")


# Strings
def test_strings_1_to_9_are_valid():
  check(["1", "5", "9", "2", "3", "4", "6", "7", "8"], True, "The strings '1' to '9' are valid.")


def test_other_number_strings_are_not_valid():
  check(["0", "10", "-1", "1.0"], False, "Only the strings '1' to '9' are valid.")


def test_strings_that_are_not_numbers_are_not_valid():
  check(["a", "", "123abc", "five"], False, "Only the strings '1' to '9' are valid.")


def test_number_strings_with_extra_characters_are_not_valid():
  check([" 5", "5 ", "05", "+5"], False, "Only the strings '1' to '9' are valid; extra characters are not allowed.\n"
        "HINT: " + INT_HINT)


def test_unusual_digit_characters_are_not_valid():
  check(["²", "①", "𝟡"], False,
        "These characters count as digits for Python's isdigit() and isnumeric() methods, but they are not one "
        "of the strings '1' to '9', so they are not valid.\n"
        "HINT: compare the value with the strings '1' to '9' instead of using isdigit() or isnumeric().")


# Other types
def test_floats_are_not_valid():
  check([5.0, 1.0, 9.0, 5.5], False,
        "Only integers and strings are valid, so floats like 5.0 are not.\n"
        "HINT: In Python, 5.0 == 5 is True (and so is `5.0 in range(1, 10)`), so checking the value is not enough: "
        "also check its type (e.g. `type(value) == int`).")


def test_other_types_are_not_valid():
  check([None, [5], ["5"]], False, "Only integers and strings are valid.")


def test_q1_has_no_print_calls():
  lines = util.find_print_calls("q1")
  assert lines == [], (
      f"src/q1.py calls print() on line(s) {', '.join(map(str, lines))}. is_1_to_9 should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
