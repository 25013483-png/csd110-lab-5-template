import itertools
import sys
import pytest
import util
import util_lab_5 as lab5


def run_q4(monkeypatch, capsys, answers):
    """Run src/q4.py as a program, as if the user typed each of answers in turn.
       Returns everything the program printed"""
    output, prompts = util.run_script(
        "q4", monkeypatch, capsys, answers,
        f"src/q4.py asked for input more times than expected (the user's answers were {answers}). "
        f"Your program should only ask for the number of disks, using prompt_for_1_to_9.")
    assert "<function" not in output, (
        f"Your program printed a function instead of the value it returns:\n{output}\n"
        f"HINT: to call a function you need parentheses (and arguments, if it has parameters), "
        f"e.g. prompt_for_1_to_9(), not prompt_for_1_to_9")
    return output


def check_solution_printed(output, disks, answers):
    """Fail unless output contains the solution for disks disks (from any tower to any other tower)"""
    for source, target in itertools.permutations([1, 2, 3], 2):
        if lab5.solve_hanoi(disks, source, target) in output:
            return
    pytest.fail(
        f"When the user enters {', '.join(answers)}, your program should print the solution for {disks} disks "
        f"(the string returned by solve_hanoi). Your program printed:\n{output}",
        pytrace=False)


def test_q4_imports_q2_and_q3():
    imported = util.imported_modules("q4")
    missing = [name for name in ["q2", "q3"] if name not in imported]
    assert missing == [], (
        f"src/q4.py must import the functions you wrote in the other files, but it does not import: {', '.join(missing)}")


def test_q4_does_not_copy_functions():
    copied = [name for name in ["is_1_to_9", "prompt_for_1_to_9", "solve_hanoi"] if name in util.defined_function_names("q4")]
    assert copied == [], (
        f"src/q4.py should not contain its own definition of {', '.join(copied)}. "
        f"Delete it and import the function from the file where you wrote it instead!")


def test_q4_has_main_guard():
    assert util.has_main_guard("q4"), (
        "src/q4.py must use a main guard (`if __name__ == \"__main__\":`) and put the program's code inside it, "
        "as described in Part 4 of the README.")


def test_importing_q4_does_not_run_the_program(capsys):
    sys.modules.pop("q4", None)
    util.import_student_module(
        "q4", input_advice="Put the code that runs the program inside your `if __name__ == \"__main__\":` block.")
    printed = capsys.readouterr().out
    assert printed == "", (
        f"When src/q4.py is imported it should not run the program, but it printed:\n{printed}\n"
        f"Put the code that runs the program inside your `if __name__ == \"__main__\":` block.")


def test_q4_does_not_call_input_directly():
    lines = util.find_calls(util.parse_source("q4"), "input")
    assert lines == [], (
        f"src/q4.py calls input() on line(s) {', '.join(map(str, lines))}. Use your prompt_for_1_to_9 function to "
        f"ask for the number of disks instead. (To greet the user, use print().)")


def test_q4_greets_the_user(monkeypatch, capsys):
    output = run_q4(monkeypatch, capsys, ["3"])
    greeting = output.split(lab5.PROMPT)[0]
    assert greeting.strip() != "", (
        f"Your program should greet the user (e.g. \"Let's solve the Towers of Hanoi puzzle! How many disks?\") "
        f"before asking for the number of disks. Your program printed:\n{output}")


def test_q4_prints_the_solution(monkeypatch, capsys):
    output = run_q4(monkeypatch, capsys, ["3"])
    check_solution_printed(output, 3, ["3"])


def test_q4_asks_again_after_invalid_input(monkeypatch, capsys):
    answers = ["0", "a", "2"]
    output = run_q4(monkeypatch, capsys, answers)
    assert lab5.INVALID_MESSAGE in output, (
        f"When the user enters invalid input, your program should print {lab5.INVALID_MESSAGE!r} and ask again "
        f"(use prompt_for_1_to_9 to ask for the number of disks). Your program printed:\n{output}")
    check_solution_printed(output, 2, answers)
