import copy
from pieces import pieces as pcs
from pieces import score

board = [[]]
list_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
memory_board = [[]]

for i in range(8):
    board.append([])
    for h in range(8):
        board[i].append(" ")
        board[i][h] = (list_alphabet[i] + list_numbers[h])

board.pop(8)

board_pieces = copy.deepcopy(board)

for i in range(2):
    for h in range(8):
        board_pieces[i][h] += "-W"

for i in range(6, 8):
    for h in range(8):
        board_pieces[i][h] += "-B"

board_pieces[0][0] += "R"
board_pieces[0][7] += "R"
board_pieces[7][0] += "R"
board_pieces[7][7] += "R"

board_pieces[0][1] += "N"
board_pieces[0][6] += "N"
board_pieces[7][1] += "N"
board_pieces[7][6] += "N"

board_pieces[0][2] += "B"
board_pieces[0][5] += "B"
board_pieces[7][2] += "B"
board_pieces[7][5] += "B"

board_pieces[0][3] += "K"
board_pieces[0][4] += "Q"
board_pieces[7][3] += "Q"
board_pieces[7][4] += "K"

for i in range(8):
    board_pieces[1][i] += "P"
    board_pieces[6][i] += "P"

for i in range(8):
    board_pieces[2][i] += "-__"
    board_pieces[3][i] += "-__"
    board_pieces[4][i] += "-__"
    board_pieces[5][i] += "-__"


def print_board():
    for i in board_pieces:
        print(i)

print_board()

print("\n")

memory_board = copy.deepcopy(board_pieces)

def test():
    print("this is a test")
    print("test...")
    print("test complete")

def player_two_turn():
    print("Player Two Turn")
    print_board()
    print("\n")
    player_one_turn()


def player_one_turn():
    # >>> select piece to move or exit
    print("Player 1's turn")
    piece_move = input("Enter the name of the square the piece you want to move is on: ")
    piece_move = piece_move.upper()
    if piece_move == "QUIT" or piece_move == "EXIT":
        quit()
    piece_move = [*piece_move]

    # >>> checks logic for move, looking at X
    for i in list_alphabet:
        if piece_move[0] in list_alphabet and piece_move[1] in list_numbers:
            if piece_move[0] == i:
                x = list_alphabet.index(i)
        else:
            print("Invalid input")
            player_one_turn()

    # >>> checks logic for move, looking at Y
    for i in list_numbers:
        if piece_move[0] in list_alphabet and piece_move[1] in list_numbers:
            if piece_move[1] == i:
                y = list_numbers.index(i)
        else:
            print("Invalid input")
            player_one_turn()

    # print(x, y)

    if "W" not in board_pieces[x][y]:
        print("You can't move that piece")
        player_one_turn()

    # >>> select location to move piece to
    piece_going = input("Enter the name of the square you want to move your piece to: ")
    piece_going = piece_going.upper()
    piece_going = [*piece_going]

    # >>> checks logic for move, looking at X2
    for i in list_alphabet:
        if piece_going[0] in list_alphabet and piece_going[1] in list_numbers:
            if piece_going[0] == i:
                x2 = list_alphabet.index(i)
        else:
            print("Invalid input")
            player_one_turn()

    # >>> checks logic for move, looking at Y2
    for i in list_numbers:
        if piece_going[0] in list_alphabet and piece_going[1] in list_numbers:
            if piece_going[1] == i:
                y2 = list_numbers.index(i)
        else:
            print("Invalid input")
            player_one_turn()

    if "W" in board_pieces[x2][y2]:
        print("You can't move onto your own piece")
        player_one_turn()

    piece = board_pieces[x][y]
    piece_piece = piece[3:5]
    # print("piece piece", piece_piece)
    piece = piece[-1]
    piece_space = board_pieces[x][y]
    piece_space = piece_space[0:2]
    # print(piece_space)
    # print(piece)

    taken_piece = board_pieces[x2][y2]
    taken_piece_color = taken_piece[3]
    taken_piece_piece = taken_piece[3:5]
    # print("taken piece piece", taken_piece_piece)
    taken_piece_char = taken_piece[-1]
    taken_piece_space = board_pieces[x2][y2]
    taken_piece_space = taken_piece_space[0:2]
    # print(taken_piece_space)

    # >>> checks to see if jumping is allowed and if jumping is involved
    if not pcs[piece]["jump"]:
        amount_x = x2 - x
        amount_y = y2 - y
        # print(amount_x, amount_y)
        if amount_x == amount_y: # diagonal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x + i][y + i]:
                    print("You can't move through pieces")
                    player_one_turn()
        elif amount_x == 0: # straight horizontal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x][y + i]:
                    print("You can't move through pieces")
                    player_one_turn()
        elif amount_y == 0: # straight vertical move
            for i in range(1, amount_x):
                if "-__" not in board_pieces[x + i][y]:
                    print("You can't move through pieces")
                    player_one_turn()

    # test()
    absolute_x = abs(x2 - x)
    absolute_y = abs(y2 - y)

    # print("absolute x", absolute_x)
    # print("absolute y", absolute_y)
    # print(taken_piece_color)

    # >>> pawn logic
    if piece == "P":
        pawn_number = board_pieces[x][y][1]
        for i in pcs["P"]["first_move_taken_White"]:
            if pawn_number == i and pcs["P"]["first_move_taken_White"][i] == False:
                if absolute_x == 2 and absolute_y == 0:
                        pcs["P"]["first_move_taken_White"][pawn_number] = True
                elif absolute_x == 1 and absolute_y == 0:
                    pcs["P"]["first_move_taken_White"][pawn_number] = True
                else:
                    print("Invalid move, the pawn cannot move like that")
                    player_one_turn()
            elif pawn_number == i and pcs["P"]["first_move_taken_White"][i] == True:
                if absolute_x == 1 and absolute_y == 0:
                    pass
                elif absolute_x == 1 and absolute_y == 1:
                    if taken_piece_color == "B":
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        player_one_turn()
                else:
                    print("Invalid move, the pawn cannot move like that, this this")
                    player_one_turn()

    # >>> rook logic
    if piece == "R":
        if absolute_x == 0 and absolute_y != 0:
            pass
        elif absolute_x != 0 and absolute_y == 0:
            pass
        else:
            print("Invalid move, the rook cannot move like that")
            player_one_turn()

    # >>> knight logic
    if piece == "N":
        if absolute_x == 2 and absolute_y == 1:
            pass
        elif absolute_x == 1 and absolute_y == 2:
            pass
        else:
            print("Invalid move, the knight cannot move like that")
            player_one_turn()

    # >>> bishop logic
    if piece == "B":
        if absolute_x == absolute_y:
            pass
        else:
            print("Invalid move, the bishop cannot move like that")
            player_one_turn()

    # >>> queen logic
    if piece == "Q":
        if absolute_x == absolute_y:
            pass
        elif absolute_x == 0 and absolute_y != 0:
            pass
        elif absolute_x != 0 and absolute_y == 0:
            pass
        else:
            print("Invalid move, the queen cannot move like that")
            player_one_turn()

    # >>> king logic
    if piece == "K":
        if absolute_x == 1 and absolute_y == 1:
            pass
        elif absolute_x == 1 and absolute_y == 0:
            pass
        elif absolute_x == 0 and absolute_y == 1:
            pass
        else:
            print("Invalid move, the king cannot move like that")
            player_one_turn()

    # print(x2, y2)

    print("\n")

    # >>> tells you what piece you moved
    for i in pcs:
        if piece == i:
            print(pcs[i]["name"], "on square", piece_space, "is moving to square", board_pieces[x2][y2][0:2])

    # >>> tells you, if you are attacking, what piece you are attacking
    if "B" in taken_piece:
        for i in pcs:
            if taken_piece_char == i:
                # print("Black", pcs[i]["name"], "on space", taken_piece_space, "has been taken by", "White",
                #       pcs[piece]["name"])
                print("White", pcs[piece]["name"], "takes", "Black", pcs[i]["name"])
                score["player_one"] += pcs[i]["value"]

    board_pieces[x2][y2] = board_pieces[x2][y2].replace(taken_piece_piece, piece_piece)
    board_pieces[x][y] = board[x][y]
    board_pieces[x][y] += "-__"

    print("\n")
    print_board()
    print("\n")
    # print("Player 1's score:", score["player_one"])
    if score["player_one"] >= 100:
        print("You Wins!")
        exit()
    elif score["player_two"] >= 100:
        print("Player Two Wins!")
        exit()
    print("\n")
    player_two_turn()


player_one_turn()

