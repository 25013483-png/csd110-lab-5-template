import pytest
import util
import util_lab_5 as lab5

CONVERT_HINT = ("Check that the user's input is valid (with your is_1_to_9 function) *before* converting it "
                "with int(); int() crashes if the input isn't a number.")


def run_prompt(monkeypatch, capsys, answers):
  """Call prompt_for_1_to_9 as if the user typed each of answers in turn.
     Returns (the value returned, everything printed, the prompts given to input())"""
  function = util.get_student_function("q2", "prompt_for_1_to_9", "Part 2")
  valid_answer = answers[-1]
  prompts = util.mock_input(
      monkeypatch, answers,
      f"prompt_for_1_to_9 asked for input again after the user entered {valid_answer!r}, which is valid. "
      f"When the input is valid, return it (as an int) instead of asking again.")
  result = util.call(function, hints={ValueError: CONVERT_HINT})
  return result, capsys.readouterr().out, prompts


def test_prompt_for_1_to_9_is_defined():
  util.get_student_function("q2", "prompt_for_1_to_9", "Part 2")


def test_prompt_for_1_to_9_takes_no_parameters():
  function = util.get_student_function("q2", "prompt_for_1_to_9", "Part 2")
  util.check_parameter_count(function, 0, "it asks the user for the number instead")


def test_prompt_for_1_to_9_has_a_docstring():
  util.get_student_function("q2", "prompt_for_1_to_9", "Part 2")
  util.check_has_docstring("q2", "prompt_for_1_to_9")


def test_prompt_is_correct(monkeypatch, capsys):
  result, output, prompts = run_prompt(monkeypatch, capsys, ["5"])
  assert prompts, "prompt_for_1_to_9 should ask the user for input using input()"
  if prompts[0] != lab5.PROMPT:
    pytest.fail("prompt_for_1_to_9 asks for input with the wrong prompt.\n" +
                util.compare_strings(lab5.PROMPT, prompts[0], "Your prompt") +
                "\nHINT: the prompt is the text you give to input(), e.g. input(\"...\")", pytrace=False)


# Valid input
def test_valid_input_is_returned_as_an_int(monkeypatch, capsys):
  result, output, prompts = run_prompt(monkeypatch, capsys, ["5"])
  util.check_returned(
      "prompt_for_1_to_9() (when the user enters '5')", result, 5,
      "HINT: input() always gives you a string (e.g. '5'). Convert it to an int with int() before returning it.")


def test_1_and_9_are_valid_input(monkeypatch, capsys):
  for answer in ["1", "9"]:
    result, output, prompts = run_prompt(monkeypatch, capsys, [answer])
    util.check_returned(f"prompt_for_1_to_9() (when the user enters {answer!r})", result, int(answer))


# Invalid input
def test_asks_again_after_invalid_input(monkeypatch, capsys):
  result, output, prompts = run_prompt(monkeypatch, capsys, ["0", "5"])
  assert len(prompts) == 2, (
      f"When the user enters '0' (which is not valid), prompt_for_1_to_9 should ask again by calling itself, "
      f"but it returned {result!r} without asking again.")
  assert result is not None, (
      "After the user entered '0' and then '5', prompt_for_1_to_9 returned None instead of 5.\n"
      "HINT: when your function calls itself, it must `return` the value that the recursive call returns.")
  util.check_returned("prompt_for_1_to_9() (when the user enters '0', then '5')", result, 5)


def test_prints_invalid_input_message(monkeypatch, capsys):
  result, output, prompts = run_prompt(monkeypatch, capsys, ["a", "5"])
  lines = output.splitlines()
  if lab5.INVALID_MESSAGE not in lines:
    # The line printed after the first prompt is the closest thing to the message
    printed = lines[1] if len(lines) > 1 else ""
    pytest.fail(
        f"When the user enters 'a' (which is not valid), prompt_for_1_to_9 should print {lab5.INVALID_MESSAGE!r} "
        f"on its own line before asking again.\n" + util.compare_strings(lab5.INVALID_MESSAGE, printed, "Printed"),
        pytrace=False)


def test_several_invalid_inputs(monkeypatch, capsys):
  answers = ["0", "a", "4a", "10", "𝟡", "5"]
  result, output, prompts = run_prompt(monkeypatch, capsys, answers)
  util.check_returned(f"prompt_for_1_to_9() (when the user enters {', '.join(answers)})", result, 5)


def test_output_is_correct(monkeypatch, capsys):
  result, output, prompts = run_prompt(monkeypatch, capsys, ["0", "a", "4a", "5"])
  expected = (f"{lab5.PROMPT}0\n{lab5.INVALID_MESSAGE}\n"
              f"{lab5.PROMPT}a\n{lab5.INVALID_MESSAGE}\n"
              f"{lab5.PROMPT}4a\n{lab5.INVALID_MESSAGE}\n"
              f"{lab5.PROMPT}5\n")
  if output != expected:
    pytest.fail(
        "When the user enters 0, a, 4a and then 5, prompt_for_1_to_9 does not display the right text. "
        "(The text after each prompt is what the user typed.)\n" + util.compare_text(expected, output, "Printed"),
        pytrace=False)


def test_prompt_for_1_to_9_is_recursive():
  assert util.calls_itself("q2", "prompt_for_1_to_9"), (
      "prompt_for_1_to_9 must ask again by calling itself (recursion), as described in Part 2 of the README. "
      "Don't use a loop.")


def test_q2_imports_is_1_to_9_from_q1():
  assert "is_1_to_9" not in util.defined_function_names("q2"), (
      "src/q2.py should not contain its own definition of is_1_to_9. Delete it and import is_1_to_9 from q1 instead!")
  assert "q1" in util.imported_modules("q2"), (
      "src/q2.py must import q1 (e.g. `import q1` or `from q1 import is_1_to_9`) so it can reuse is_1_to_9, "
      "as described in Part 2 of the README.")


def test_prompt_for_1_to_9_calls_is_1_to_9():
  definition = util.find_function_def("q2", "prompt_for_1_to_9")
  assert definition is not None, "Define a function named prompt_for_1_to_9 in src/q2.py, as described in Part 2 of the README."
  assert util.find_calls(definition, "is_1_to_9") != [], (
      "prompt_for_1_to_9 should check whether the user's input is valid by calling your is_1_to_9 function (from q1), "
      "instead of checking the input another way. Think about what is_1_to_9 does, and how that applies to the "
      "text the user enters.")
