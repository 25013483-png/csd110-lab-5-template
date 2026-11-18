from q1 import is_1_to_9


def prompt_for_1_to_9():
    """Prompt until the user enters an integer from 1 through 9."""
    user_input = input("Enter an integer from 1 to 9: ")

    # Base case: stop recursion and return an integer when the input is valid.
    # Recursive case: print an error and call this function again for invalid input.
    if is_1_to_9(user_input):
        return int(user_input)

    print("Invalid input.")
    # Returning the recursive result passes the valid integer back through every call.
    return prompt_for_1_to_9()