# write your code here
def print_board(board):
    print("---------")
    print("| " + board[0][0] + " " + board[0][1] + " " + board[0][2] + " |")
    print("| " + board[1][0] + " " + board[1][1] + " " + board[1][2] + " |")
    print("| " + board[2][0] + " " + board[2][1] + " " + board[2][2] + " |")
    print("---------")

def numbers(move):
    for item in move:
        try:
            value = int(item[1])
        except TypeError:
            return False
        except ValueError:
            return False
    return True

def expected_index(move):
    try:
        value = int(move[0][1])
        value = int(move[1][1])
    except IndexError:
        return False
    return True

def valid_coordinates(move):
    for item in move:
        if 0 >= int(item[1]) or int(item[1]) > 3:
            return False
    return True

def convert_horizontal_position(position):
    if position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return 2

def convert_vertical_position(position):
    if position == 1:
        return 2
    elif position == 2:
        return 1
    else:
        return 0

# Board is oriented top-bottom, left-to-right, and input coordinates are oriented bottom-top, left-to-right
def busy_cell(move, board):
    cell = board[convert_vertical_position(int(move[1][1]))][convert_horizontal_position(int(move[0][1]))]
    if cell == 'X' or cell == 'O':
        return True
    return False

def not_over(board):
    empty_characters = [' ', '_']

    return all([any([any([cell == ' ' for cell in line]) for line in board]),
                not x_wins(board),
                not o_wins(board)])

def impossible(board):
    x = 0
    o = 0
    for line in board:
        for cell in line:
            if cell == 'X':
                x += 1
            if cell == 'O':
                o += 1
    return abs(x - o) >= 2

def vertical_victory(board, sign):
    for x in range(0, 3):
        if board[0][x] == sign and board[1][x] == sign and board[2][x] == sign:
            return True
    return False

def horizontal_victory(board, sign):
    for x in range(0, 3):
        if board[x][0] == sign and board[x][1] == sign and board[x][2] == sign:
            return True
    return False

def cross_victory(board, sign):
    if board[1][1] == sign:
        if (board[0][0] == sign and board[2][2] == sign) or (board[2][0] == sign and board[0][2] == sign):
            return True
    return False

def x_wins(board):
    return vertical_victory(board, 'X') or horizontal_victory(board, 'X') or cross_victory(board, 'X')

def o_wins(board):
    return vertical_victory(board, 'O') or horizontal_victory(board, 'O') or cross_victory(board, 'O')

def insert_move(board, move, current_player):
    print("move current_player ", current_player)
    board[convert_vertical_position(int(move[1][1]))][convert_horizontal_position(int(move[0][1]))] = current_player
    return board

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

# init = input("Enter cells")
board = [[' ' for j in range(3)] for i in range(3)]
print_board(board)

current_player = 'X'
while all([not impossible(board), not_over(board)]):
    invalid_input = True
    while(invalid_input):
        coordinates = [position for position in enumerate(input("Enter the coordinates").split())]
        if not numbers(coordinates):
            print("You should enter numbers!")
        elif not expected_index(coordinates):
            print("Coordinates should be from 1 to 3!")
        elif not valid_coordinates(coordinates):
            print("Coordinates should be from 1 to 3!")
        elif busy_cell(coordinates, board):
            print("This cell is occupied! Choose another one!")
        else:
            invalid_input = False

    board = insert_move(board, coordinates, current_player)
    current_player = switch_player(current_player)
    print_board(board)

if impossible(board):
    print("Impossible")
elif x_wins(board):
    if o_wins(board):
        print("Impossible")
    else:
        print("X wins")
elif o_wins(board):
    print("O wins")
elif not_over(board):
    print("Game not finished")
else:
    print("Draw")
