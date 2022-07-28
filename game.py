BOARD_WIDTH = 3
BOARD_HEIGHT = 3
TURN_NUMBER = 2
p = 0

def new_board():
    board = []
    for i in range(0, BOARD_WIDTH):
        column = []
        for i in range(BOARD_HEIGHT):
            column.append(None)
        board.append(column)
    return board


def render(game):
    format_b = [[spot if spot is not None else "-" for spot in nested] for nested in game]
    for row in format_b:
        for col in row:
            print(col + " ", end=" ")
        print()


def is_board_full(board):
    for row in board:
        for sq in row:
            if sq == None:
                return False
    return True


def get_input():
    row = int(input("Enter a row (0 - 2): "))
    col = int(input("Enter a column (0 - 2): "))
    return row, col


def make_move(board, coordinates, player):
    if board[coordinates[0]][coordinates[1]] != None:
        raise Exception("You can't move there")

    board[coordinates[0]][coordinates[1]] = player
    return board


def determine_player(turn):
    player_1 = 'X'
    player_2 = 'O'
    if turn % 2 == 0:
        return player_1
    else:
        return player_2


def returnf():
    return False


def horiz_win(board, player):
    for i in board:
        if i[0] == player and i[1] == player and i[2] == player:
            return True


def vert_win(board, player):
    for i in range(len(board)):
        if board[p][i] == player and board[p + 1][i] == player and board[p + 2][i] == player:
            return True


def diagnol_win(board, player):
    for i in range(len(board)):
        if board[p][0] == player and board[p + 1][1] == player and board[p + 2][2] == player:
            return True
        elif board[p][2] == player and board[p + 1][1] == player and board[p + 2][0] == player:
            return True

board = new_board()
render(board)
print()
def play_game():
    global TURN_NUMBER

    while True:
        player = determine_player(TURN_NUMBER)
        valid = True
        while valid:
            try:
                print(f"Player {player}'s turn.")
                make_move(board, get_input(), player)
                break
            except (IndexError, Exception):
                print("Out of range, enter number in range")

        render(board)
        TURN_NUMBER += 1

        if vert_win(board, player) == True:
            print(f"Player {player} has won.")
            break

        if horiz_win(board, player) == True:
            print(f"Player {player} has won.")
            break

        if diagnol_win(board, player) == True:
            print(f"Player {player} has won.")
            break

        if is_board_full(board) == True:
            print("It's a draw.")
            break

play_game()