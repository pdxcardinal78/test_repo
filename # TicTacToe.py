# TicTacToe
import random
import copy

# Change 1


def print_board(board: list):
    """Prints the tictactoe board.

    Args:
        board (list): List of spaces and current items filling it.
    """
    print("\n\n\n")
    print(board[0], board[1], board[2], sep=" | ")
    print("-" * 10)
    print(board[3], board[4], board[5], sep=" | ")
    print("-" * 10)
    print(board[6], board[7], board[8], sep=" | ")
    print("\n\n\n")


def ai_selection(board: list) -> int:
    """Selects a place to go for the computer.

    Args:
        board (list): List of spaces and current items filling it.

    Returns:
        int: best location for the computer to choose.
    """
    possibleChoice = []

    # Select random location if only 1 x has been placed.
    if board.count("x") == 1:
        board_ai = copy.deepcopy(board)
        board_ai.remove("x")
        val = random.choice(board_ai)
        return val
    if board[0:3].count("x") == 2:
        possibleChoice += [i for i in board[0:3] if i != "x"]
    if board[3:6].count("x") == 2:
        possibleChoice += [i for i in board[3:6] if i != "x"]
    if board[6:10].count("x") == 2:
        possibleChoice += [i for i in board[6:10] if i != "x"]
    if board[0:9:3].count("x") == 2:
        possibleChoice += [i for i in board[0:9:3] if i != "x"]
    if board[1:9:3].count("x") == 2:
        possibleChoice += [i for i in board[1:9:3] if i != "x"]
    if board[2:9:3].count("x") == 2:
        possibleChoice += [i for i in board[2:9:3] if i != "x"]
    if [board[0], board[4], board[8]].count("x") == 2:
        possibleChoice += [i for i in [board[0], board[4], board[8]] if i != "x"]
    if [board[2], board[4], board[6]].count("x") == 2:
        possibleChoice += [i for i in [board[2], board[4], board[6]] if i != "x"]

    print(possibleChoice)
    possibleChoice = [i for i in possibleChoice if i != "o"]
    if possibleChoice != []:
        check_board = copy.deepcopy(board)
        check_board = [i for i in check_board if str(i).isdigit()]
        for i in check_board:
            check_board2 = copy.deepcopy(board)
            update_board(check_board2, i, "o")
            check, _ = check_winner(check_board2)
            if check:
                val = i
                return val
            else:
                pass
        val = random.choice(possibleChoice)
    else:
        otherChoice = [i for i in board if str(i).isdigit()]
        for i in otherChoice:
            check_board2 = copy.deepcopy(board)
            update_board(check_board2, i, "o")
            check, _ = check_winner(check_board2)
            if check:
                val = i
                return val
            else:
                pass
        val = random.choice(otherChoice)

    return val


def update_board(board: list, loc: int, value: str) -> list:
    """updates the board to the new values based on which position was selected.

    Args:
        board (list): List of spaces and current values in them.
        loc (int): Where the player/ai would like to place their mark.
        value (str): The type of mark to place, x or o

    Returns:
        list: the new board layout
    """
    board[loc - 1] = value
    return print_board(board)


def check_winner(board: list) -> bool:
    """checks to see if a winner exists on the board.

    Args:
        board (list): The board and the values it current holds

    Returns:
        bool: True if the a winner is found and who that was. False if no winner is found yet.
    """
    if board[0] == board[1] == board[2]:
        return True, board[0]
    elif board[3] == board[4] == board[5]:
        return True, board[3]
    elif board[6] == board[7] == board[8]:
        return True, board[6]
    elif board[0] == board[3] == board[6]:
        return True, board[0]
    elif board[1] == board[4] == board[7]:
        return True, board[1]
    elif board[2] == board[5] == board[8]:
        return True, board[2]
    elif board[0] == board[4] == board[8]:
        return True, board[0]
    elif board[2] == board[4] == board[6]:
        return True, board[2]
    else:
        return False, ""


def main():
    """main game function"""
    # Create initial board.
    board = [i for i in range(1, 10)]
    player = "x"  # Set inital player to x
    print_board(board)  # Print the board.
    ai = input(
        "Is this a (1 or 2) player game?: "
    )  # Check to see how many players, 1 will cause the computer to play.
    if ai in ["1", "2"]:
        pass
    else:
        print("Error: Incorrect value entered, please pick a value that is 1 or 2")
        exit()
    # Main game loop
    while len([i for i in board if str(i).isdigit() == True]) != 0:
        if player == "x":
            # Update the board with the players choice
            val = int(input("Enter a number from the board: "))
            if val in [i for i in board if str(i).isdigit()]:
                update_board(board, val, player)
                player = "o"
            else:
                print(f"{val} wasn't an available choice")
                exit()
        else:
            if ai == "1":
                # Find a value for the computer to play
                val = ai_selection(board)
                update_board(board, val, player)
            else:
                # Allow a second player to choose a value.
                update_board(
                    board, int(input("Enter a number from the board: ")), player
                )
            player = "x"

        # Check for winner
        winner_value, winner = check_winner(board)
        if winner_value == True:
            print(f"{winner.upper()} has won, congrats")
            exit()
    # If no winner found at the end of the available picks, game ends in tie.
    print("No winner, ended in tie")


if __name__ == "__main__":
    main()
