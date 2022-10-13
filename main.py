import copy
from pieces import pieces as pcs
from pieces import score
from pieces import en_passant_check as passant
from pieces import castling_check as castle

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
board_pieces[7][4] += "K"
board_pieces[0][4] += "Q"
board_pieces[7][3] += "Q"

for i in range(8):
    board_pieces[1][i] += "P"
    board_pieces[6][i] += "P"

for i in range(8):
    board_pieces[2][i] += "-__"
    board_pieces[3][i] += "-__"
    board_pieces[4][i] += "-__"
    board_pieces[5][i] += "-__"

#     board_pieces[6][i] += "-__"
#
# board_pieces[7][1] += "-__" #"N"
# board_pieces[7][6] += "-__" #"N"
# board_pieces[7][3] += "-__" #"Q"
# board_pieces[7][2] += "-__" #"B"
# board_pieces[7][5] += "-__" #"B"


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


def player_two_cpu_turn():
    pass


def player_two_turn():
    # >>> select piece to move or exit
    print("Player Two's turn")
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
            player_two_turn()

    # >>> checks logic for move, looking at Y
    for i in list_numbers:
        if piece_move[0] in list_alphabet and piece_move[1] in list_numbers:
            if piece_move[1] == i:
                y = list_numbers.index(i)
        else:
            print("Invalid input")
            player_two_turn()

    if "B" not in board_pieces[x][y]:
        print("You can't move that piece")
        player_two_turn()

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
            player_two_turn()

    # >>> checks logic for move, looking at Y2
    for i in list_numbers:
        if piece_going[0] in list_alphabet and piece_going[1] in list_numbers:
            if piece_going[1] == i:
                y2 = list_numbers.index(i)
        else:
            print("Invalid input")
            player_two_turn()

    if "B" in board_pieces[x2][y2]:
        print("You can't move onto your own piece")
        player_two_turn()

    piece = board_pieces[x][y]
    piece_piece = piece[3:5]
    piece = piece[-1]
    piece_space = board_pieces[x][y]
    piece_space = piece_space[0:2]

    taken_piece = board_pieces[x2][y2]
    taken_piece_color = taken_piece[3]
    taken_piece_piece = taken_piece[3:5]
    taken_piece_char = taken_piece[-1]
    taken_piece_space = board_pieces[x2][y2]
    taken_piece_space = taken_piece_space[0:2]

    # >>> checks to see if jumping is allowed and if jumping is involved
    if not pcs[piece]["jump"]:
        amount_x = x2 - x
        amount_y = y2 - y
        if amount_x == amount_y:  # diagonal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x + i][y + i]:
                    print("You can't move through pieces")
                    player_two_turn()
        elif amount_x == 0:  # straight horizontal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x][y + i]:
                    print("You can't move through pieces")
                    player_two_turn()
        elif amount_y == 0:  # straight vertical move
            for i in range(1, amount_x):
                if "-__" not in board_pieces[x + i][y]:
                    print("You can't move through pieces")
                    player_two_turn()

    absolute_x = abs(x2 - x)
    absolute_y = abs(y2 - y)

    # print("X", x, "y", y)
    # print("X2", x2, "y2", y2)
    # print("y2 + 1", y2 + 1)
    # print(board_pieces[x2][y2 + 1])
    # print("y2 - 1", y2 - 1)
    # print(board_pieces[x2][y2 - 1])

    # >>> pawn logic
    if piece == "P":
        pawn_number = board_pieces[x][y][1]
        for i in pcs["P"]["first_move_taken_White"]:
            if pawn_number == i and pcs["P"]["first_move_taken_Black"][i] == False:
                if absolute_x == 2 and absolute_y == 0:
                    pcs["P"]["first_move_taken_Black"][pawn_number] = True
                    if y2 == 0:
                        if "WP" in board_pieces[x2][y2 + 1]:
                            passant["en_passant"] = True
                    elif y2 == 7:
                        if "WP" in board_pieces[x2][y2 - 1]:
                            passant["en_passant"] = True
                    else:
                        if "WP" in board_pieces[x2][y2 + 1] or "WP" in board_pieces[x2][y2 - 1]:
                            passant["en_passant"] = True
                elif absolute_x == 1 and absolute_y == 0:
                    pcs["P"]["first_move_taken_Black"][pawn_number] = True
                    passant["en_passant"] = False
                else:
                    print("Invalid move, the pawn cannot move like that")
                    player_two_turn()
            elif pawn_number == i and pcs["P"]["first_move_taken_Black"][i] == True:
                if absolute_x == 1 and absolute_y == 0:
                    passant["en_passant"] = False
                    pass
                elif passant["en_passant"] and absolute_x == 1 and absolute_y == 1:
                    if y2 == 0:
                        if "-__" in taken_piece and "WP" in board_pieces[x2+1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                            board_pieces[x2 + 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            player_one_turn()
                    elif y2 == 7:
                        if "-__" in taken_piece and "WP" in board_pieces[x2+1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                            board_pieces[x2 + 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            player_one_turn()
                    elif "-__" in taken_piece and "WP" in board_pieces[x2+1][y2]:
                        passant["en_passant"] = False
                        print("nothing personal kid *en passant*")
                        board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                        board_pieces[x2 + 1][y2] += "-__"
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        player_one_turn()
                elif absolute_x == 1 and absolute_y == 1:
                    if taken_piece_color == "W":
                        passant["en_passant"] = False
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        player_two_turn()
                else:
                    print("Invalid move, the pawn cannot move like that")
                    player_two_turn()

    # >>> rook logic
    if piece == "R":
        if absolute_x == 0 and absolute_y != 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        else:
            print("Invalid move, the rook cannot move like that")
            player_two_turn()

    # >>> knight logic
    if piece == "N":
        if absolute_x == 2 and absolute_y == 1:
            passant["en_passant"] = False
            pass
        elif absolute_x == 1 and absolute_y == 2:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the knight cannot move like that")
            player_two_turn()

    # >>> bishop logic
    if piece == "B":
        if absolute_x == absolute_y:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the bishop cannot move like that")
            player_two_turn()

    # >>> queen logic
    if piece == "Q":
        if absolute_x == absolute_y:
            passant["en_passant"] = False
            pass
        elif absolute_x == 0 and absolute_y != 0:
            passant["en_passant"] = False
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the queen cannot move like that")
            player_two_turn()

    # >>> king logic
    if piece == "K":
        if absolute_x == 1 and absolute_y == 1:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 1 and absolute_y == 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 0 and absolute_y == 1:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 0 and absolute_y == 2:
            if board_pieces[x][y] == "H5-BK" and board_pieces[x2][y2] == "H7-__" and castle["castling"]:
                if "-__" in board_pieces[x][y+1] and "BR" in board_pieces[x][y+3]:
                    board_pieces[x][y+1] = board_pieces[x][y+3]
                    board_pieces[x][y+3] = board[x][y+3]
                    board_pieces[x][y+3] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    player_one_turn()
            elif board_pieces[x][y] == "H5-BK" and board_pieces[x2][y2] == "H3-__" and castle["castling"]:
                if "-__" in board_pieces[x][y - 1] and "-__" in board_pieces[x][y - 3] and "BR" in board_pieces[x][y-4]:
                    board_pieces[x][y - 1] = board_pieces[x][y - 4]
                    board_pieces[x][y - 4] = board[x][y - 4]
                    board_pieces[x][y - 4] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    player_one_turn()
            else:
                print("Invalid move, the king cannot move like that")
                player_one_turn()
        else:
            print("Invalid move, the king cannot move like that")
            player_two_turn()

    print("\n")

    # >>> tells you what piece you moved
    for i in pcs:
        if piece == i:
            print(pcs[i]["name"], "on square", piece_space, "is moving to square", board_pieces[x2][y2][0:2])

    # >>> tells you, if you are attacking, what piece you are attacking
    if "W" in taken_piece:
        for i in pcs:
            if taken_piece_char == i:
                print("Black", pcs[piece]["name"], "takes", "White", pcs[i]["name"])
                score["player_two"] += pcs[i]["value"]

    board_pieces[x2][y2] = board_pieces[x2][y2].replace(taken_piece_piece, piece_piece)
    board_pieces[x][y] = board[x][y]
    board_pieces[x][y] += "-__"

    # >>> pawn logic expanded // pawn promotion
    if piece == "P":
        if x2 == 0:
            print("You have reached the end of the board, you can now promote your pawn")
            pawn_pp_choice = input("What piece would you like to promote your pawn to? (R, N, B, Q): ")
            pawn_pp_choice = pawn_pp_choice.upper()
            if pawn_pp_choice == "R":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "R")
                print("Your pawn has been promoted to a rook")
            elif pawn_pp_choice == "N":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "N")
                print("Your pawn has been promoted to a knight")
            elif pawn_pp_choice == "B":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "B")
                print("Your pawn has been promoted to a bishop")
            elif pawn_pp_choice == "Q":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "Q")
                print("Your pawn has been promoted to a queen")
            else:
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "Q")
                print("Invalid choice, your pawn has defaulted into a queen")

    print("\n")
    print_board()
    print("\n")

    if score["player_two"] >= 100:
        print("You Win, Player Two! Congratulations!")
        print("Player 2's score:", score["player_two"])
        print("Player 1's score:", score["player_one"])
        exit()
    elif score["player_one"] >= 100:
        print("Player one Wins!")
        print("Player 1's score:", score["player_one"])
        print("Player 2's score:", score["player_two"])
        exit()
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

    # print("X", x, "Y", y)

    # >>> checks to see if jumping is allowed and if jumping is involved
    if not pcs[piece]["jump"]:
        amount_x = x2 - x
        amount_y = y2 - y
        # print(amount_x, amount_y)
        if amount_x == amount_y:  # diagonal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x + i][y + i]:
                    print("You can't move through pieces")
                    player_one_turn()
        elif amount_x == 0:  # straight horizontal move
            for i in range(1, amount_y):
                if "-__" not in board_pieces[x][y + i]:
                    print("You can't move through pieces")
                    player_one_turn()
        elif amount_y == 0:  # straight vertical move
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

    # print("X", x, "y", y)
    # print("X2", x2, "y2", y2)
    # print("y2 + 1", y2 + 1)
    # print(board_pieces[x2][y2 + 1])
    # print("y2 - 1", y2 - 1)
    # print(board_pieces[x2][y2 - 1])

    # print("board_pieces[x2][y2]", board_pieces[x2][y2])
    # print("board_pieces[x2-1][y2]", board_pieces[x2-1][y2])
    # print("en passant", passant["en_passant"])

    # >>> pawn logic
    if piece == "P":
        pawn_number = board_pieces[x][y][1]
        for i in pcs["P"]["first_move_taken_White"]:
            if pawn_number == i and pcs["P"]["first_move_taken_White"][i] == False:
                if absolute_x == 2 and absolute_y == 0:
                    pcs["P"]["first_move_taken_White"][pawn_number] = True
                    # passant["en_passant"] = False
                    if y2 == 0:
                        if "BP" in board_pieces[x2][y2 + 1]:
                            passant["en_passant"] = True
                            # print("en passant is now true")
                    elif y2 == 7:
                        if "BP" in board_pieces[x2][y2 - 1]:
                            passant["en_passant"] = True
                            # print("en passant is now true")
                    else:
                        if "BP" in board_pieces[x2][y2 + 1] or "BP" in board_pieces[x2][y2 - 1]:
                            passant["en_passant"] = True
                            # print("en passant is now true")
                elif absolute_x == 1 and absolute_y == 0:
                    pcs["P"]["first_move_taken_White"][pawn_number] = True
                    passant["en_passant"] = False
                else:
                    print("Invalid move, the pawn cannot move like that")
                    # print("Test 1")
                    player_one_turn()
            elif pawn_number == i and pcs["P"]["first_move_taken_White"][i] == True:
                if absolute_x == 1 and absolute_y == 0:
                    passant["en_passant"] = False
                    pass
                elif passant["en_passant"] and absolute_x == 1 and absolute_y == 1:
                    if y2 == 0:
                        if "-__" in taken_piece and "BP" in board_pieces[x2-1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 - 1][y2] = board[x2 - 1][y2]
                            board_pieces[x2 - 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            # print("Test 3")
                            player_one_turn()
                    elif y2 == 7:
                        if "-__" in taken_piece and "BP" in board_pieces[x2-1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 - 1][y2] = board[x2 - 1][y2]
                            board_pieces[x2 - 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            # print("Test 4")
                            player_one_turn()
                    elif "-__" in taken_piece and "BP" in board_pieces[x2-1][y2]:
                        passant["en_passant"] = False
                        print("nothing personal kid *en passant*")
                        board_pieces[x2 - 1][y2] = board[x2 - 1][y2]
                        board_pieces[x2 - 1][y2] += "-__"
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        # print("Test 5")
                        player_one_turn()
                elif absolute_x == 1 and absolute_y == 1:
                    if taken_piece_color == "B":
                        passant["en_passant"] = False
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        # print("Test 2")
                        player_one_turn()
                else:
                    print("Invalid move, the pawn cannot move like that")
                    # print("Test 6")
                    player_one_turn()

    # >>> rook logic
    if piece == "R":
        if absolute_x == 0 and absolute_y != 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        else:
            print("Invalid move, the rook cannot move like that")
            player_one_turn()

    # >>> knight logic
    if piece == "N":
        if absolute_x == 2 and absolute_y == 1:
            passant["en_passant"] = False
            pass
        elif absolute_x == 1 and absolute_y == 2:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the knight cannot move like that")
            player_one_turn()

    # >>> bishop logic
    if piece == "B":
        if absolute_x == absolute_y:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the bishop cannot move like that")
            player_one_turn()

    # >>> queen logic
    if piece == "Q":
        if absolute_x == absolute_y:
            passant["en_passant"] = False
            pass
        elif absolute_x == 0 and absolute_y != 0:
            passant["en_passant"] = False
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
            pass
        else:
            print("Invalid move, the queen cannot move like that")
            player_one_turn()

    # print("board_pieces[x][y]", board_pieces[x][y], "selected space")
    # print("board_pieces[x2][y2]", board_pieces[x2][y2], "target space")
    # print("castling", castle["castling"])
    # print("check empty space", board_pieces[x][y-1])
    # print("check rook position", board_pieces[x][y-3])
    # print("piece", piece)

    # >>> king logic
    if piece == "K":
        if absolute_x == 1 and absolute_y == 1:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 1 and absolute_y == 0:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 0 and absolute_y == 1:
            passant["en_passant"] = False
            castle["castling"] = False
            pass
        elif absolute_x == 0 and absolute_y == 2:
            if board_pieces[x][y] == "A4-WK" and board_pieces[x2][y2] == "A2-__" and castle["castling"]:
                if "-__" in board_pieces[x][y-1] and "WR" in board_pieces[x][y-3]:
                    board_pieces[x][y-1] = board_pieces[x][y-3]
                    board_pieces[x][y-3] = board[x][y-3]
                    board_pieces[x][y-3] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    # print("Test 4")
                    player_one_turn()
            elif board_pieces[x][y] == "A4-WK" and board_pieces[x2][y2] == "A6-__" and castle["castling"]:
                if "-__" in board_pieces[x][y + 1] and "-__" in board_pieces[x][y + 3] and "WR" in board_pieces[x][y+4]:
                    board_pieces[x][y + 1] = board_pieces[x][y + 4]
                    board_pieces[x][y + 4] = board[x][y + 4]
                    board_pieces[x][y + 4] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    # print("Test 3")
                    player_one_turn()
            else:
                print("Invalid move, the king cannot move like that")
                # print("Test 2")
                player_one_turn()
        else:
            print("Invalid move, the king cannot move like that")
            # print("test 1")
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

    # >>> pawn logic expanded // pawn promotion
    if piece == "P":
        if x2 == 7:
            print("You have reached the end of the board, you can now promote your pawn")
            pawn_pp_choice = input("What piece would you like to promote your pawn to? (R, N, B, Q): ")
            pawn_pp_choice = pawn_pp_choice.upper()
            if pawn_pp_choice == "R":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "R")
                print("Your pawn has been promoted to a rook")
            elif pawn_pp_choice == "N":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "N")
                print("Your pawn has been promoted to a knight")
            elif pawn_pp_choice == "B":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "B")
                print("Your pawn has been promoted to a bishop")
            elif pawn_pp_choice == "Q":
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "Q")
                print("Your pawn has been promoted to a queen")
            else:
                board_pieces[x2][y2] = board_pieces[x2][y2].replace("P", "Q")
                print("Invalid choice, your pawn has defaulted into a queen")

    print("\n")
    print_board()
    print("\n")
    # print("Player 1's score:", score["player_one"])
    if score["player_one"] >= 100:
        print("You Win, Player One! Congratulations!")
        print("Player 1's score:", score["player_one"])
        print("Player 2's score:", score["player_two"])
        exit()
    elif score["player_two"] >= 100:
        print("Player Two Wins!")
        print("Player 2's score:", score["player_two"])
        print("Player 1's score:", score["player_one"])
        exit()
    player_two_turn()

# print(board_pieces[0][0])
# print(board_pieces[0][1])
# print(board_pieces[1][0])
# print(board_pieces[1][1])

player_one_turn()
