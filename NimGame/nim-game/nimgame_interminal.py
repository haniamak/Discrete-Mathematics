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


def display_sticks(n):
    print("\n" + "=" * 40)
    for i in range(n):
        print(" # ", end="")
    if n > 0:
        print()
    print(f"Sticks remaining: {n}")
    print("=" * 40 + "\n")


def play_nim():
    print("Welcome to the game of Nim!")
    name = str(input("Enter your name: "))
    n = int(input(f"Hello {name}! Enter the number of sticks to start with: "))
    print(f"There are {n} sticks. You can take 1, 2, or 3 sticks on your turn.")
    print("The player who takes the last stick wins.")
    name = str(input("Wanna play with a friend or the computer? (F/C): "))
    if name.lower() == "computer":
        computer_strategy = str(
            input("Choose computer strategy: 'smart' or 'silly': ")
        ).lower()
        if computer_strategy == "smart":
            nim_computer_func = nim_computer()
        else:
            nim_computer_func = nim_computer_silly()

    while n > 0:
        for i in range(n):
            print(" # ", end="")
        print()

        if name.lower() == "c":
            move = nim_human(n)
            n -= move
            display_sticks(n)
            if n <= 0:
                print("Congratulations! You win!")
                break

            computer_move = nim_computer_func(n)
            n -= computer_move
            print(f"Computer took {computer_move} stick(s).")
            display_sticks(n)

            if n <= 0:
                print("Computer wins! Better luck next time.")
                break
        else:
            move = nim_human(n)
            n -= move
            print(f"{name} took {move} stick(s).")
            display_sticks(n)

            if n <= 0:
                print(f"{name} wins! Congratulations!")
                break

            move2 = nim_human(n)
            n -= move2
            print(f"Player 2 took {move2} stick(s).")
            display_sticks(n)

            if n <= 0:
                print("Player 2 wins! Better luck next time.")
                break


if __name__ == "__main__":
    play_nim()
