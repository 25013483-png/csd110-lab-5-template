import pytest
import util
import util_lab_5 as lab5

TYPE_HINT = ("Check the type of the argument before comparing it with a number, and use `and` so that the "
             "comparison only happens when the type is right.")


def solve_hanoi():
  """Return the solve_hanoi function defined in src/q3.py"""
  return util.get_student_function("q3", "solve_hanoi", "Part 3")


def test_solve_hanoi_is_defined():
  solve_hanoi()


def test_solve_hanoi_takes_three_parameters():
  util.check_parameter_count(solve_hanoi(), 3, "the number of disks, the source tower and the target tower")


def test_solve_hanoi_has_a_docstring():
  solve_hanoi()
  util.check_has_docstring("q3", "solve_hanoi")


# The base case
def test_0_disks_is_the_empty_string():
  lab5.check_solution(solve_hanoi(), 0, 1, 3, "")


def test_solve_hanoi_returns_instead_of_printing(capsys):
  util.check_returns_instead_of_printing(capsys, solve_hanoi(), 1, 1, 3)


# Solutions. Each move is on its own line, ending with a period and a newline (\n)
def test_1_disk_from_tower_1_to_3():
  lab5.check_solution(solve_hanoi(), 1, 1, 3, "Move disk 1 from tower 1 to tower 3.\n")


def test_1_disk_from_tower_2_to_1():
  lab5.check_solution(solve_hanoi(), 1, 2, 1, "Move disk 1 from tower 2 to tower 1.\n")


def test_2_disks_from_tower_1_to_3():
  lab5.check_solution(
      solve_hanoi(), 2, 1, 3,
      "Move disk 1 from tower 1 to tower 2.\n"
      "Move disk 2 from tower 1 to tower 3.\n"
      "Move disk 1 from tower 2 to tower 3.\n")


def test_2_disks_from_tower_2_to_3():
  lab5.check_solution(
      solve_hanoi(), 2, 2, 3,
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 2 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n")


def test_2_disks_from_tower_2_to_1():
  lab5.check_solution(
      solve_hanoi(), 2, 2, 1,
      "Move disk 1 from tower 2 to tower 3.\n"
      "Move disk 2 from tower 2 to tower 1.\n"
      "Move disk 1 from tower 3 to tower 1.\n")


def test_3_disks_from_tower_1_to_3():
  lab5.check_solution(
      solve_hanoi(), 3, 1, 3,
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 2 from tower 1 to tower 2.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 3 from tower 1 to tower 3.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 2 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n")


def test_5_disks_from_tower_1_to_3():
  lab5.check_solution(
      solve_hanoi(), 5, 1, 3,
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 2 from tower 1 to tower 2.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 3 from tower 1 to tower 3.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 2 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 4 from tower 1 to tower 2.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 2 from tower 3 to tower 1.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 3 from tower 3 to tower 2.\n"
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 2 from tower 1 to tower 2.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 5 from tower 1 to tower 3.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 2 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 3 from tower 2 to tower 1.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 2 from tower 3 to tower 1.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 4 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n"
      "Move disk 2 from tower 1 to tower 2.\n"
      "Move disk 1 from tower 3 to tower 2.\n"
      "Move disk 3 from tower 1 to tower 3.\n"
      "Move disk 1 from tower 2 to tower 1.\n"
      "Move disk 2 from tower 2 to tower 3.\n"
      "Move disk 1 from tower 1 to tower 3.\n")


def test_solve_hanoi_is_recursive():
  assert util.calls_itself("q3", "solve_hanoi"), (
      "solve_hanoi must call itself (recursion) to solve the smaller puzzles, as described in Part 3 of the README.")


# Invalid arguments must fail an assert statement
def test_negative_number_of_disks_fails_assert():
  for disks in [-1, -5]:
    util.check_raises_assertion_error(solve_hanoi(), (disks, 1, 3), "the number of disks is negative")


def test_number_of_disks_that_is_not_an_int_fails_assert():
  for disks in [1.5, "3", None]:
    util.check_raises_assertion_error(solve_hanoi(), (disks, 1, 3), "the number of disks is not an integer",
                                      hints={TypeError: TYPE_HINT})


def test_invalid_source_tower_fails_assert():
  for source in [0, 4, 3.5, "1"]:
    util.check_raises_assertion_error(solve_hanoi(), (1, source, 3), "the source tower is not 1, 2 or 3")


def test_invalid_target_tower_fails_assert():
  for target in [0, 4, 3.5, "3"]:
    util.check_raises_assertion_error(solve_hanoi(), (1, 1, target), "the target tower is not 1, 2 or 3")


def test_q3_has_no_print_calls():
  lines = util.find_print_calls("q3")
  assert lines == [], (
      f"src/q3.py calls print() on line(s) {', '.join(map(str, lines))}. solve_hanoi should return its solution, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
