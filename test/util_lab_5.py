"""Helpers specific to lab 5 (Towers of Hanoi)"""

import pytest
import util

PROMPT = "Enter an integer from 1 to 9: "
INVALID_MESSAGE = "Invalid input."

ZERO_DISKS_HINT = (
    "solve_hanoi must accept 0 disks: that is the base case, and every recursive call eventually "
    "asks for 0 disks. Check that your assert statement allows the number of disks to be 0 "
    "(e.g. `n >= 0` rather than `n > 0`).")


def solve_hanoi(disks, source, target):
  """Return the correct solution text (used to check student programs that may
     choose any source and target tower)"""
  if disks == 0:
    return ""
  spare = 6 - source - target
  return (solve_hanoi(disks - 1, source, spare) + f"Move disk {disks} from tower {source} to tower {target}.\n" +
          solve_hanoi(disks - 1, spare, target))


def newline_hints(actual):
  """Return hints about common mistakes with \\n and . in a student's solution text"""
  hints = []
  if actual.startswith("\n") or "\n\n" in actual:
    hints.append(
        "Your solution has blank lines in it. Put \\n at the end of each 'Move disk...' line, rather than "
        "between the three parts of your solution. (The solution for 0 disks is the empty string, so adding "
        "\\n between the parts adds extra blank lines.)")
  elif actual != "" and not actual.endswith("\n"):
    hints.append("Every 'Move disk...' line must end with a newline (\\n), including the last one.")
  if actual != "" and ".\n" not in actual and "." not in actual:
    hints.append("Every 'Move disk...' line ends with a period (.) before the newline.")
  return "".join(f"\nHINT: {hint}" for hint in hints)


def moves_hint(disks, actual, expected):
  """Return a hint about the towers used in the recursive calls, if the solution is
     formatted correctly but has the wrong moves"""
  if disks < 2 or len(actual.splitlines()) != len(expected.splitlines()) or newline_hints(actual):
    return ""
  return ("\nHINT: check the towers you use in your two recursive calls. The first call moves n-1 disks from the "
          "source tower to the spare tower; the second moves them from the spare tower to the target tower. "
          "(The spare tower is 6 - source - target.)")


def check_solution(solve, disks, source, target, expected):
  """Check that the student's solve_hanoi function gives the expected solution text"""
  call_text = util.describe_call(solve, disks, source, target)
  actual = util.call(solve, disks, source, target, hints={AssertionError: ZERO_DISKS_HINT})
  if actual is None:
    pytest.fail(util.none_returned_hint(call_text), pytrace=False)
  if not isinstance(actual, str):
    pytest.fail(f"{call_text} returned {actual!r} ({util.a_or_an(type(actual).__name__)}), but it should return a string.",
                pytrace=False)
  if actual != expected:
    pytest.fail(
        f"{call_text} returned the wrong solution.\n" + util.compare_text(expected, actual) + newline_hints(actual) +
        moves_hint(disks, actual, expected),
        pytrace=False)
