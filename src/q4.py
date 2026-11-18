from q2 import prompt_for_1_to_9
from q3 import solve_hanoi


if __name__ == "__main__":
    print("Let's solve the Towers of Hanoi puzzle! How many disks?")
    number_of_disks = prompt_for_1_to_9()
    solution = solve_hanoi(number_of_disks, 1, 3)
    print(solution, end="")