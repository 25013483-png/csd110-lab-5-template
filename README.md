# Lab 5 - Computing with Functions

## Setup

1. Click the "**Use this template**" button near the top of this repository on GitHub
2. Set the following properties on the GitHub repository, then click "Create repository":
    - **Owner**: your GitHub username (NOT the course organization)
    - **Name**: csd110-26f-lab-5
    - **Visibility**: Private
3. In your new repository, go to Settings -> Collaborators, and add your instructor as a collaborator.
4. Create a branch named `lab-5` on which to do your lab work
5. Create a Codespace on that branch, and open it (give it a few minutes to initialize)
6. In your Codespace terminal, verify your setup using `gh lab setup-check`

### Required Reading 

It is assumed that you have watched all lecture videos and completed readings and practice exercises up to the end of Chapter 6 (not including Chapter 4) in the course textbook.  If you have not done so yet, you should! 

### Reflections

As you are working on your lab, help yourself remember important things by taking notes in `reflections.md`. Record notes about anything you think important to remember, any problems you encountered and how you resolved them, and any remaining questions you may still have.

> **NOTE**: `reflections.md` is a 'markdown' file.  Markdown is a markup language that has simple syntax for adding formatting to plain text documents. See [this documentation on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to learn how to format text in a markdown file.

### AI Use

> **IMPORTANT**: ***Failure to include an accurate AI Use Statement as described below may result in a lab grade deduction of up to 100% depending on your instructor's evaluation of how well you understand the code you submit***

You MAY use AI as a LEARNING AID to help you understand topics you are needing extra help with.
You may NOT use AI to do your work for you or to avoid having to think and learn on your own.

#### AI Use Statement

**Whether or not you use AI**, you MUST include an AI Use Statement in your `reflections.md` document that indicates clearly:

- Which specific AI tools you used in the completion of this lab (or an explicit statement that you did not use any AI tools).
- Links to or copies of **ALL** AI chats you had related to this assignment. 

> **IMPORTANT:** if sharing a link, do NOT simply copy the URL from your browser; you MUST click the **Share** button and create a public link.

Examples:
- I used ChatGPT to help me better understand the lab requirements.  Below are links to my ChatGPT chats.
- I used Claude to give me examples of statements vs expressions in Python.  Below are links to my conversation.
- I did not use any AI tools to complete this lab.

### Running your code

#### From the terminal

1. Open the terminal (View -> Terminal)
2. Enter a command like the following `python path/to/script.py`.  For example, to run the `q1.py` script in the `src` folder, run `python src/q1.py`.

#### Using the debugger

1. Open the Python file you want to run
2. Open the 'Run and Debug' panel (right side, right-arrow icon with bug in lower left corner). 
3. Make sure the "Python Debugger: Current File" configuration is selected in the dropdown at the top of the panel.
4. Click the green arrow button to run the currently opened Python file

### Testing your code

A set of tests have been prepared for this lab that will help you determine if your code is correct or not.

#### Running tests 

| Task | Command | Example |
|------|---------|---------|
| Run all tests | `pytest` | `pytest` |
| Stop at the first failing test while working | `pytest -x` | `pytest -x` |
| Run one test file | `pytest <path_to_file>` | `pytest test/test_q1.py` |
| Run one test function | `pytest <path_to_file>::<function_name>` | `pytest test/test_q1.py::test_floats_are_not_valid` | 

While working, use `pytest -x` to focus on one failure at a time. Fix that issue and run the same command again to continue through the tests. Once the tests are passing this way, run `pytest` to check the entire lab.

#### Reading test output

The output of the tests will give you an indication of which tests passed or failed. For any failed tests, you will also see messages that should help you determine why the test failed.

Here are some tips for dealing with failing tests:

1. The name of the test itself usually gives a clue as to what the test is checking (e.g. `test_floats_are_not_valid`).
2. Read the message under the test name. It usually says which function call was tested, what your function returned, what it should have returned, and why.
3. When a string is wrong, the message shows the "Expected" and "Returned" values one above the other, with a `^` under the first character that is different.
4. If a line starting with `src/` appears in the output, it shows the line in **your** code where the problem happened.
5. The tests for each part are in order, starting with the simplest. Fix the first failing test before worrying about later ones. Often fixing one test fixes other failing tests as well.
6. When working on a failing test, run just that test (see above) so you can focus on its output without having to wade through the output of all the other tests.

#### Passing tests does not guarantee correctness

If all the tests passed, you can be reasonably sure that your code is correct, **BUT PASSING ALL TESTS DOES NOT NECESSARILY MEAN YOU WILL GET 100%** because some grades are assigned to non-coding tasks, and it is sometimes possible to create incorrect programs that do pass the tests.

## Instructions

### Overview 

In this lab you will create functions using recursion, docstrings for documentation, and appropriate guardian statements. You will use an incremental approach to work toward a program that can solve the classic puzzle game [Towers of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi). Skim the linked Wikipedia article to familiarize yourself with the game, and pay specific attention to the "Recursive Solution" section.

> **IMPORTANT**: In any place where you are asked to name functions or variables, you MUST use meaningful names. You must also include appropriate docstrings for any non-trivial functions you create. Failing to do either will result in a lower grade.

### Part 1 - A function with a docstring

Your eventual program will need to ask the user to enter a number from 1 to 9. You will need your program to confirm whether the user did so correctly or not. That's a simple piece of functionality to start with!


1. In `q1.py` define a **PURE** function named `is_1_to_9`

    1. The function has a single parameter
    2. If the given parameter is an integer from 1 to 9, return `True`
    3. If the given parameter is any of the strings from `"1"` to `"9"`,  return `True`
    4. If the given parameter is **any other value** (including 1.0, "²", "𝟡", etc), return `False`

### Part 2 - Use recursion to repeatedly prompt the user

You can now check if a given value is 1 to 9, but your program will also need to actually ask the user for their input. In this part, you will make a **recursive** function that prompts the user for a number from 1 to 9 and **continues to do** so until the user enters a valid value. Once the user enters a valid value (which you must check by **reusing the `is_1_to_9` function you made in q1**; think about how what it does applies here), that integer is returned from the function.  Later, this function will be used to obtain the number of disks the user wants to solve for in the Towers of Hanoi puzzle.


1. In `q2.py` define a function named `prompt_for_1_to_9`

    1. **NOTE**: Since this function recieves user input and prints text to the user, it is NOT a pure function
    2. The function has no parameters.
    3. It asks the user for input with the prompt `Enter an integer from 1 to 9: ` (including the colon and the space at the end)
    4. It checks whether the user's input is valid by calling your `is_1_to_9` function from `q1.py` (imported, **NOT copied**)
    5. If the user enters one of the integers from 1 to 9, return that value **as an integer**
    6. If the user does not enter a valid value, print the message `Invalid input.` and return the value from a **RECURSIVE** call to `prompt_for_1_to_9`
    7. In a comment, state the base case and the recursive case of this function. I.e., under which conditions does recursion stop? (The base case.) Under which conditions does recursion occur? (The recursive case.)
    8. In another comment, explain why it is necessary to **return** the result of the recursive call. (If you're not sure, try calling the function **without** returning the result. What happens? Why? Use a debugger to investigate.)

### Part 3 - Write a Towers of Hanoi solver

As you read in the Wikipedia article linked in the Overview, there is an elegant algorithm that solves the Towers of Hanoi puzzle for any number of disks.  The algorithm can be stated as follows:

> Given a number of disks, `n`, a source tower number (1, 2, or 3), and a target tower number (1, 2, or 3)...
> 1. If n = 0 do nothing (base case), otherwise...
> 1. Repeat this algorithm using n-1 disks, keep the **same source tower**, but the use the current spare as the new target
> 1. Move the last disk n from the source tower to the target tower
> 1. Repeat the algorithm again using n-1 disks, but this time keep the **same target tower** but the use new current spare tower as the new source

Stated in plain English, the steps are

1. move all but the last disk to the spare tower
2. move the last disk to the target
3. move the disks on the spare tower to the target tower

but both steps 1 & 3 are recursive. That is, you repeat the same sequence of steps, but this time with a different number of disks, and a different source, spare, and target tower. It may be surprising, but this simple algorithm works for any number of disks!

In this part you will write a Python implementation of this algorithm. It will be a pure, recursive function that takes as its inputs the number of disks, the source tower number, and the target tower number, and it returns a string that contains instructions for moving n disks from the source tower to the target tower by the rules of the game.

1. In `q3.py` define a **PURE** function named `solve_hanoi`
    1. The function has three parameters: the number of disks, the source tower number, and the target tower number
    2. Use an `assert` statement to ensure that the number of disks is a **non-negative** integer (i.e. 0 or more; 0 disks is the base case below)
    3. Use `assert` statements to ensure that the source and target tower numbers are one of 1, 2, or 3
    4. If the number of disks is 0 return the empty string
    5. Otherwise...
         1. Store in a variable the string returned when you call `solve_hanoi` using one less disk, the original source, and the spare tower as the **target**
          
            **HINT:** The spare tower number can be calculated using the following expression: `6 - S - T` where S is the source tower number and T is the target tower number.  This works because the sum of the three tower numbers will always be 1+2+3=6, so subracting the source and target tower numbers gives you the spare tower number.
            
         2. Store in a second variable the string `Move disk N from tower S to tower T.` followed by a newline (`\n`), where N, S, and T are the number of disks, the source tower number, and the target tower number, respectively.  (I.e. replace N, S, and T with the actual values, and note the period at the end)
         3. Store in a third variable the string returned when you call `solve_hanoi` using one less disk, the spare tower as the **source**, and the original target
         4. Combine all three of these strings into one and return it. (Don't add any more `\n` characters: each move already ends with one, and the solution for 0 disks is the empty string.)
     6. **DEBUGGING:** Set a breakpoint in your `solve_hanoi` function and run your function using the Debugger panel. Step through your code and observe how the number of disks change as you enter the recursive calls. Also observe the strings as they are generated. 
     7. Take a screenshot of your code paused at your breakpoint when it is **multiple levels** deep into the recursion. The call stack showing multiple recursive calls of `solve_hanoi` must be visible.

### Part 4 - Put it all together!

You now have all the pieces you need to create a program that can help a user solve the Towers of Hanoi game for any number of disks

In `q4.py` write code to do the following:

1. Greet the user with a message like `Let's solve the Towers of Hanoi puzzle! How many disks?`
2. Use your `prompt_for_1_to_9` function to obtain from the user the number of disks they want to solve for
3. Use your `solve_hanoi` function to generate the solution string, and print this string to the user
4. **IMPORTANT**: Use a `__name__ == "__main__"` guardian to ensure that your code only runs when the script is executed directly, and not when it is imported as a module.
    
## Reflect

Did you take notes in `reflections.md` as you worked? (See the [Reflections](#reflections) instructions above.) You should!

Did you document your AI usage adequately? (See the [AI Use](#ai-use) instructions above.) You must!

## Submission

1. **Test** your code to verify that it is working as expected (see the [Testing your code](#testing-your-code) section above).
1. **Commit** all changes in your lab files with meaningful commit messages.
2. **Push** your commits to GitHub
3. **Verify** that the code on GitHub is correct
4. Create a **Pull request** using your lab branch as the 'compare' branch and the main branch as the 'base'
5. Navigate to the "Files Changed" tab of your pull request, and **copy the URL** to this page into the lab folder on the LMS.

## Rubric

See the rubric attached to this lab in the LMS

### Automatic limits:

Your grade will be limited to a maximum of 79% for any of the following:
- Missing / inadequate [AI Use Statement](#ai-use)
- Missing / inadequate [Reflections](#reflections)
- Incorrect lab [Setup](#setup)

