import random
import sys

# Global variables (2 Players)
game_still_going = True
current_player = "X"
winner = None
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Global variables(Computer AI)
ai_turn = "X"


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def play_game():
    which_mode = input("""1. 2 Players
2. Computer(AI)
: """)

    if which_mode == "1":
        display_board()

        while game_still_going:
            handle_turn(current_player)
            check_if_game_over()
            flip_player()

        if winner == "X" or winner == "O":
            print(f"{winner} won")
        elif winner is None:
            print("Tie")

    elif which_mode == "2":
        display_board()

        while game_still_going:
            ai(ai_turn)
            check_if_game_over()
            flip_ai_player()

        if winner == "X" or winner == "O":
            print(f"{winner} won")
        elif winner is None:
            print("Tie")


def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid_human = False
    while not valid_human:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, Choose a position from 1-9: ")

        position = int(position) - 1
        if board[position] == "-":
            valid_human = True
        else:
            print("You can't go here, Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False


def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# Computer(AI)
def ai(player_ai):
    if ai_turn == "X":
        print(player_ai + "'s turn")
        position = input("Choose a position from 1-9: ")

        valid_ai = False
        while not valid_ai:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8",
                                   "9"]:
                position = input("Invalid input, Choose a position from 1-9: ")

            position = int(position) - 1
            if board[position] == "-":
                valid_ai = True
            else:
                print("You can't go here, Go again")

        board[position] = player_ai

    if ai_turn == "Computer":
        while True:
            move = random.randint(1, 8)
            if board[move] == "-":
                board[move] = "O"
                break

    display_board()


def flip_ai_player():
    global ai_turn

    if ai_turn == "X":
        ai_turn = "Computer"
    elif ai_turn == "Computer":
        ai_turn = "X"


play_again = True
if __name__ == "__main__":
    while play_again:
        game_still_going = True
        current_player = "X"
        winner = None
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        play_game()

        valid = False
        while not valid:
            if game_still_going is False:
                play_again = input("Play again. [Y/n]: ")
                if play_again == "n":
                    sys.exit(0)
                elif play_again == "Y":
                    valid = True
