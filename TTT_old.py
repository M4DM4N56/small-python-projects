# slow bot speed
import time
t = 2
continuing = True
piece = "X"
opposition = "O"


def ttt_solo():
    global continuing
    global piece
    # board and rows
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    def show_board():
        print("[" + board[0] + "][" + board[1] + "][" + board[2] + "]")
        print("[" + board[3] + "][" + board[4] + "][" + board[5] + "]")
        print("[" + board[6] + "][" + board[7] + "][" + board[8] + "]")
        print("\n")

    # player input
    def player_input():
        global piece
        print("Your turn!")
        turn = input("Pick a number from 1-9: ")
        while turn not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            turn = input("Pick a number from 1-9: ")
        placement = int(turn) - 1
        if board[0 + placement] == "-":
            board[0 + placement] = piece
        else:
            print("Sorry, That spot is taken...")
            player_input()
        show_board()

    # bot input
    def ai_input():
        global opposition
        print("My turn!")
        time.sleep(1)
        if board[2] == "-":
            board[2] = opposition
        elif board[8] == "-":
            board[8] = opposition
        elif board[0] == "-":
            board[0] = opposition
        elif board[4] == "-":
            board[4] = opposition
        elif board[1] == "-":
            board[1] = opposition
        elif board[5] == "-":
            board[5] = opposition
        elif board[3] == "-":
            board[3] = opposition
        elif board[6] == "-":
            board[6] = opposition
        elif board[7] == "-":
            board[7] = opposition
        show_board()

    # win check
    def horizontal_win():
        global continuing
        if board[0] == board[1] == board[2] == piece:
            print("You win!")
            continuing = False
        elif board[3] == board[4] == board[5] == piece:
            print("You win!")
            continuing = False
        elif board[6] == board[7] == board[8] == piece:
            print("You win!")
            continuing = False

    def vertical_win():
        global continuing
        if board[0] == board[3] == board[6] == piece:
            print("You win!")
            continuing = False
        elif board[1] == board[4] == board[7] == piece:
            print("You win!")
            continuing = False
        elif board[2] == board[5] == board[8] == piece:
            print("You win!")
            continuing = False

    def diagonal_win():
        global continuing
        if board[0] == board[4] == board[8] == piece:
            print("You win!")
            continuing = False
        elif board[2] == board[4] == board[6] == piece:
            print("You win!")
            continuing = False

    # lose check
    def horizontal_loss():
        global continuing
        if board[0] == board[1] == board[2] == opposition:
            print("You lose!")
            continuing = False
        elif board[3] == board[4] == board[5] == opposition:
            print("You lose!")
            continuing = False
        elif board[6] == board[7] == board[8] == opposition:
            print("You lose!")
            continuing = False

    def vertical_loss():
        global continuing
        if board[0] == board[3] == board[6] == opposition:
            print("You lose!")
            continuing = False
        elif board[1] == board[4] == board[7] == opposition:
            print("You lose!")
            continuing = False
        elif board[2] == board[5] == board[8] == opposition:
            print("You lose!")
            continuing = False

    def diagonal_loss():
        global continuing
        if board[0] == board[4] == board[8] == opposition:
            print("You lose!")
            continuing = False
        elif board[2] == board[4] == board[6] == opposition:
            print("You lose!")
            continuing = False

    # tie check
    def tie():
        global continuing
        if "-" not in board:
            print("It's a tie!")
            continuing = False

    # turn alternator and win/loss checker
    while continuing:
        show_board()
        player_input()
        horizontal_win()
        vertical_win()
        diagonal_win()
        tie()
        if continuing:
            ai_input()
            horizontal_loss()
            vertical_loss()
            diagonal_loss()
            tie()


# ttt multi player
def ttt_doubles():
    global continuing
    # board and rows
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    def show_board_multi():
        print("[" + board[0] + "][" + board[1] + "][" + board[2] + "]")
        print("[" + board[3] + "][" + board[4] + "][" + board[5] + "]")
        print("[" + board[6] + "][" + board[7] + "][" + board[8] + "]")
        print("\n")

    # player 1 input
    def first_player_input():
        print("Player 1!")
        turn = input("Pick a number from 1-9: ")
        while turn not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            turn = input("Pick a number from 1-9: ")
        placement = int(turn) - 1
        if board[0 + placement] == "-":
            board[0 + placement] = "X"
        else:
            print("Sorry, That spot is taken...")
            first_player_input()
        show_board_multi()

    # player 2 input
    def second_player_input():
        print("Player 2!")
        turn = input("Pick a number from 1-9: ")
        while turn not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            turn = input("Pick a number from 1-9: ")
        placement = int(turn) - 1
        if board[0 + placement] == "-":
            board[0 + placement] = "O"
        else:
            print("Sorry, That spot is taken...")
            second_player_input()
        show_board_multi()

    # player 1 win check
    def horizontal_first_win():
        global continuing
        if board[0] == board[1] == board[2] == "X":
            print("X wins!")
            continuing = False
        elif board[3] == board[4] == board[5] == "X":
            print("X wins!")
            continuing = False
        elif board[6] == board[7] == board[8] == "X":
            print("X wins!")
            continuing = False

    def vertical_first_win():
        global continuing
        if board[0] == board[3] == board[6] == "X":
            print("X wins!")
            continuing = False
        elif board[1] == board[4] == board[7] == "X":
            print("X wins!")
            continuing = False
        elif board[2] == board[5] == board[8] == "X":
            print("X wins!")
            continuing = False

    def diagonal_first_win():
        global continuing
        if board[0] == board[4] == board[8] == "X":
            print("X wins!")
            continuing = False
        elif board[2] == board[4] == board[6] == "X":
            print("X wins!")
            continuing = False

    # player 2 win check
    def horizontal_second_win():
        global continuing
        if board[0] == board[1] == board[2] == "O":
            print("O wins!")
            continuing = False
        elif board[3] == board[4] == board[5] == "O":
            print("O wins!")
            continuing = False
        elif board[6] == board[7] == board[8] == "O":
            print("O wins!")
            continuing = False

    def vertical_second_win():
        global continuing
        if board[0] == board[3] == board[6] == "O":
            print("O wins!")
            continuing = False
        elif board[1] == board[4] == board[7] == "O":
            print("O wins!")
            continuing = False
        elif board[2] == board[5] == board[8] == "O":
            print("O wins!")
            continuing = False

    def diagonal_second_win():
        global continuing
        if board[0] == board[4] == board[8] == "O":
            print("O wins!")
            continuing = False
        elif board[2] == board[4] == board[6] == "O":
            print("O wins!")
            continuing = False

    # tie check
    def tie():
        global continuing
        if "-" not in board:
            print("It's a tie!")
            continuing = False

    # turn alternator and win/loss checker
    while continuing:
        show_board_multi()
        first_player_input()
        horizontal_first_win()
        vertical_first_win()
        diagonal_first_win()
        tie()
        if continuing:
            second_player_input()
            horizontal_second_win()
            vertical_second_win()
            diagonal_second_win()
            tie()


# Main menu
def main_menu():
    global piece
    global opposition
    global continuing
    print("TIC TAC TOE")
    print("\n")
    game_choose = input("Enter 0 for a tutorial, 1 for a single player game and 2 for a two-player game: ")
    while game_choose not in ["0", "1", "2"]:
        game_choose = input("Enter 0 for a tutorial, 1 for a single player game and 2 for a two-player game: ")
    print("\n")
    if game_choose in ["0", "1", "2"]:
        game_choose = int(game_choose)

    # tutorial
    if game_choose == 0:
        print("\n")
        print("The goal of the game is to get three in a row of your piece (X or O).")
        print("\n")
        print("[1][2][3]")
        print("[4][5][6]")
        print("[7][8][9]")
        print("\n")
        print("Entering a number from 1 - 9 will place your piece in that spot if it is open.")
        print("\n")
        main_menu()

    # single player settings
    if game_choose == 1:
        ttt_solo()
        continuing = True

    # multi player settings
    elif game_choose == 2:
        print("X goes first.")
        continuing = True
        ttt_doubles()


main_menu()
