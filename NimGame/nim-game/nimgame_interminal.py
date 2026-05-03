import random

BOARD_WIDTH = 64
INNER_WIDTH = BOARD_WIDTH - 2
STICK_COLUMNS = 10
BOARD_LINES = 18


def clear_screen():
    print("", end="")


def nim_computer(n):
    take = n % 4
    if take == 0:
        return random.randint(1, min(3, n))
    return min(take, n)


def nim_computer_silly(n):
    return random.randint(1, min(3, n))


def nim_human(n, name):
    while True:
        try:
            move = int(input(f"{name}, enter the number of sticks to take (1-3): "))
            if move in [1, 2, 3] and move <= n:
                return move
            print("Invalid move. You must take between 1 and 3 sticks.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def wrap_text(text, width):
    if len(text) <= width:
        return [text]
    lines = []
    words = text.split()
    current = ""
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def build_stick_rows(n):
    if n <= 0:
        return ["(no sticks left)"]

    columns = min(STICK_COLUMNS, max(1, n))
    cell_width = INNER_WIDTH // columns
    row_lines = []

    for start in range(0, n, columns):
        chunk = min(columns, n - start)
        line = "".join("|".center(cell_width) for _ in range(chunk)).ljust(INNER_WIDTH)
        row_lines.extend([line, line, line])
        if start + chunk < n:
            row_lines.append("".ljust(INNER_WIDTH))

    return row_lines


def render_board(n, title, mode, message=""):
    clear_screen()
    border = "+" + "-" * INNER_WIDTH + "+"
    stick_rows = build_stick_rows(n)

    print(border)
    print(f"|{'NIM GAME'.center(INNER_WIDTH)}|")
    print(f"|{title.center(INNER_WIDTH)}|")
    print(f"|{('Mode: ' + mode).center(INNER_WIDTH)}|")
    print(f"|{('Sticks remaining: ' + str(n)).center(INNER_WIDTH)}|")
    print(f"|{'=' * INNER_WIDTH}|")

    for line in stick_rows:
        if line == "(no sticks left)":
            print(f"|{line.center(INNER_WIDTH)}|")
        else:
            print(f"|{line}|")

    text_lines = []
    if message:
        text_lines.append(message)
    text_lines.append("Take 1, 2, or 3 sticks.")
    text_lines.append("The player who takes the last stick wins.")

    for text in text_lines:
        for wrapped in wrap_text(text, INNER_WIDTH):
            print(f"|{wrapped.center(INNER_WIDTH)}|")

    used_lines = 5 + len(stick_rows) + len(text_lines)
    for _ in range(max(0, BOARD_LINES - used_lines)):
        print(f"|{' ' * INNER_WIDTH}|")
    print(border)


def play_nim():
    print("Welcome to the game of Nim!")
    player_name = str(input("Enter your name: ")).strip() or "Player 1"
    n = int(input(f"Hello {player_name}! Enter the number of sticks to start with: "))

    print(f"There are {n} sticks. You can take 1, 2, or 3 sticks on your turn.")
    print("The player who takes the last stick wins.")
    mode = (
        str(input("Wanna play with a friend or the computer? (F/C): ")).strip().lower()
    )

    if mode == "c":
        computer_strategy = (
            str(input("Choose computer strategy: 'smart' or 'silly' (SM/SI): "))
            .strip()
            .lower()
        )
        computer_move_func = (
            nim_computer if computer_strategy == "sm" else nim_computer_silly
        )
        mode = "Computer"
        player_2_name = "Computer"
    else:
        mode = "f"
        computer_move_func = None
        mode = "Friend"
        player_2_name = str(input("Enter Player 2's name: ")).strip() or "Player 2"

    message = ""
    while n > 0:
        render_board(n, f"Player: {player_name}", mode, message)
        message = ""

        if mode == "c":
            move = nim_human(n, player_name)
            n -= move
            message = f"{player_name} took {move} stick(s)."
            if n <= 0:
                render_board(n, f"Player: {player_name}", mode, message)
                print(f"{player_name} wins! Congratulations!")
                break

            render_board(n, f"Player: {player_name}", mode, message)
            computer_move = computer_move_func(n)
            n -= computer_move
            message = f"Computer took {computer_move} stick(s)."
            if n <= 0:
                render_board(n, f"Player: {player_name}", mode, message)
                print("Computer wins! Better luck next time.")
                break
        else:
            move = nim_human(n, player_name)
            n -= move
            message = f"{player_name} took {move} stick(s)."
            if n <= 0:
                render_board(n, f"Player: {player_name}", mode, message)
                print(f"{player_name} wins! Congratulations!")
                break

            render_board(n, f"Player: {player_2_name}", mode, message)
            move2 = nim_human(n, player_2_name)
            n -= move2
            message = f"{player_2_name} took {move2} stick(s)."
            if n <= 0:
                render_board(n, f"Player: {player_name}", mode, message)
                print(f"{player_2_name} wins! Better luck next time.")
                break


if __name__ == "__main__":
    play_nim()
