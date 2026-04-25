import random


def nim_computer(n):
    if n % 4 == 0:
        return random.randint(1, 3)
    else:
        return n % 4


def nim_computer_silly(n):
    while True:
        move = random.randint(1, 3)
        if move <= n:
            return move
        else:
            continue


def nim_human(n):
    while True:
        try:
            move = int(input("Enter the number of sticks to take (1-3): "))
            if move in [1, 2, 3] and move <= n:
                return move
            else:
                print(
                    f"Invalid move. You must take between 1 and 3 sticks, and no more than {n}."
                )
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def play_nim():
    print("Welcome to the game of Nim!")
    n = int(input("Enter the number of sticks to start with: "))
    print(f"There are {n} sticks. You can take 1, 2, or 3 sticks on your turn.")
    print("The player who takes the last stick wins.")

    while n > 0:
        # Human's turn
        move = nim_human(n)
        n -= move
        print(f"You took {move} stick(s). {n} stick(s) remaining.")

        if n <= 0:
            print("Congratulations! You win!")
            break

        # Computer's turn
        move = nim_computer(n)
        n -= move
        print(f"Computer took {move} stick(s). {n} stick(s) remaining.")

        if n <= 0:
            print("Computer wins! Better luck next time.")
            break
