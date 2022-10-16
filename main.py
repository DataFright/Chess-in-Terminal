import copy
from pieces import pieces as pcs
from pieces import score
from pieces import en_passant_check as passant
from pieces import castling_check as castle
from pieces import player_turn as turn

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

# board_pieces[3][3] += "-WK"

def print_board():
    for i in board_pieces:
        print(i)


print_board()

print("\n")

memory_board = copy.deepcopy(board_pieces)


def check_check():
    empty_space = "-__"
    if turn["player_one"]:  # <<< player ones turn
        my_color = "White"
        my_king = "-WK"
        my_king_space = "A4-WK"
        enemy_color = "Black"
        enemy_piece_space = "G1-BP"

        # finding my king
        for i in board_pieces:
            for h in i:
                if h.endswith(my_king):
                    my_king_space = h
                    break

        # print(my_king_space, "test")

        # >>> looking at X for king
        for i in list_alphabet:
            if my_king_space[0] in list_alphabet:
                if my_king_space[0] == i:
                    x2 = list_alphabet.index(i)

        # >>> looking at Y for king
        for i in list_numbers:
            if my_king_space[1] in list_numbers:
                if my_king_space[1] == i:
                    y2 = list_numbers.index(i)

        for i in board_pieces:
            for h in i:
                # >>> looking at X for enemy piece
                for k in list_alphabet:
                    if h[0] in list_alphabet:
                        if h[0] == k:
                            x = list_alphabet.index(k)

                # >>> looking at Y for enemy piece
                for k in list_numbers:
                    if h[1] in list_numbers:
                        if h[1] == k:
                            y = list_numbers.index(k)

                amount_x = x2 - x
                amount_y = y2 - y
                absolute_amount_x = abs(amount_x)
                absolute_amount_y = abs(amount_y)

                # print(x, y)
                # print(x2, y2)
                # print(amount_x, amount_y)
                # print(absolute_amount_x, absolute_amount_y)

                if "BP" in h:
                    if amount_x == -1 and absolute_amount_y == 1:
                        # if amount_x == 1 and absolute_amount_y == 1:      // for player two
                        print(f"The {enemy_color} Pawn on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                elif "BN" in h:
                    if absolute_amount_x == 1 and absolute_amount_y == 2:
                        print(f"The {enemy_color} Knight on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                    elif absolute_amount_x == 2 and absolute_amount_y == 1:
                        print(f"The {enemy_color} Knight on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                elif "BB" in h:
                    if absolute_amount_x == absolute_amount_y:  # diagonal move
                        if y < y2 and x < x2:  # top left
                            # print("the this add x add y")
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y + g] and not "-WK" in board_pieces[x + g][
                                    y + g] and not \
                                        "-BB" in board_pieces[x + g][y + g]:
                                    # print(x, y + g)
                                    # print("You can't move through pieces 4", board_pieces[x + g][y + g])
                                    break
                                else:
                                    if y + g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                        elif y < y2 and x > x2:  # bottom left
                            # print("the this sub x add y")
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y + g] and not "-WK" in board_pieces[x - g][
                                    y + g] and not \
                                        "-BB" in board_pieces[x - g][y + g]:
                                    # print(x, y + g)
                                    # print("You can't move through pieces 4", board_pieces[x - g][y + g])
                                    break
                                else:
                                    if y + g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                        elif y > y2 and x < x2:  # top right
                            # print("the this add x sub y")
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y - g] and not "-WK" in board_pieces[x + g][
                                    y - g] and not \
                                        "-BB" in board_pieces[x + g][y - g]:
                                    # print("You can't move through pieces 4", board_pieces[x + g][y - g])
                                    break
                                else:
                                    if y - g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                        elif y > y2 and x > x2:  # bottom right
                            # print("the this minus x minus y")
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y - g] and not "-WK" in board_pieces[x - g][
                                    y - g] and not \
                                        "-BB" in board_pieces[x - g][y - g]:
                                    # print("You can't move through pieces 4", board_pieces[x - g][y - g])
                                    break
                                else:
                                    if y - g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                elif "BQ" in h:
                    if amount_x == 0:  # straight horizontal move
                        if y < y2:
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y + g] and not "-WK" in board_pieces[x][y + g] and not \
                                        "-BQ" in board_pieces[x][y + g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                        else:
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y - g] and not "-WK" in board_pieces[x][y - g] and not \
                                        "-BQ" in board_pieces[x][y - g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                    elif amount_y == 0:  # straight vertical move
                        if x < x2:
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x + g][y] and not "-WK" in board_pieces[x + g][y] and not \
                                        "-BQ" in board_pieces[x + g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                        else:
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x - g][y] and not "-WK" in board_pieces[x - g][y] and not \
                                        "-BQ" in board_pieces[x - g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                    elif absolute_amount_x == absolute_amount_y:  # diagonal move
                        if y < y2 and x < x2:  # top left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y + g] and not "-WK" in board_pieces[x + g][
                                    y + g] and not \
                                        "-BQ" in board_pieces[x + g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                        elif y < y2 and x > x2:  # bottom left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y + g] and not "-WK" in board_pieces[x - g][
                                    y + g] and not \
                                        "-BQ" in board_pieces[x - g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                        elif y > y2 and x < x2:  # top right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y - g] and not "-WK" in board_pieces[x + g][
                                    y - g] and not \
                                        "-BQ" in board_pieces[x + g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                        elif y > y2 and x > x2:  # bottom right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y - g] and not "-WK" in board_pieces[x - g][
                                    y - g] and not \
                                        "-BQ" in board_pieces[x - g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                elif "BK" in h:
                    if absolute_amount_x == 1 and absolute_amount_y == 1:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                    elif absolute_amount_x == 1 and absolute_amount_y == 0:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                    elif absolute_amount_x == 0 and absolute_amount_y == 1:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_one_check"] = True
                elif "BR" in h:
                    if amount_x == 0:  # straight horizontal move
                        # print("Rook on same row as king")
                        if y < y2:  # positive y
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y + g] and not "-WK" in board_pieces[x][y + g] and not \
                                        "-BR" in board_pieces[x][y + g]:
                                    # print(x, y + g)
                                    # print("You can't move through pieces 4", board_pieces[x][y + g])
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the that")
                        else:  # negative y
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y - g] and not "-WK" in board_pieces[x][y - g] and not \
                                        "-BR" in board_pieces[x][y - g]:
                                    # print(x, y - g)
                                    # print("You can't move through pieces 3", board_pieces[x][y - g])
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this")
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the that")
                    elif amount_y == 0:  # straight vertical move
                        # print("\n")
                        # print("h", h, "i", i)
                        # print("Rook on same column as king")
                        if x < x2:  # positive x
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x + g][y] and not "-WK" in board_pieces[x + g][y] and not \
                                        "-BR" in board_pieces[x + g][y]:
                                    # print(x + g, y)
                                    # print("You can't move through pieces 2", board_pieces[x + g][y])
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this, add")
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the that, add")
                        else:  # negative x
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x - g][y] and not "-WK" in board_pieces[x - g][y] and not \
                                        "-BR" in board_pieces[x - g][y]:
                                    # print(x - g, y)
                                    # print("You can't move through pieces 1", board_pieces[x - g][y])
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the this, minus")
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_one_check"] = True
                                        # print("the that, minus")
    else:  # <<< player twos turn
        my_color = "Black"
        my_king = "-BK"
        my_king_space = "H5-BK"
        enemy_color = "White"
        enemy_piece_space = "B1-WP"

        # finding my king
        for i in board_pieces:
            for h in i:
                if h.endswith(my_king):
                    my_king_space = h
                    break

        # print(my_king_space, "test")

        # >>> looking at X for king
        for i in list_alphabet:
            if my_king_space[0] in list_alphabet:
                if my_king_space[0] == i:
                    x2 = list_alphabet.index(i)

        # >>> looking at Y for king
        for i in list_numbers:
            if my_king_space[1] in list_numbers:
                if my_king_space[1] == i:
                    y2 = list_numbers.index(i)

        for i in board_pieces:
            for h in i:
                # >>> looking at X for enemy piece
                for k in list_alphabet:
                    if h[0] in list_alphabet:
                        if h[0] == k:
                            x = list_alphabet.index(k)

                # >>> looking at Y for enemy piece
                for k in list_numbers:
                    if h[1] in list_numbers:
                        if h[1] == k:
                            y = list_numbers.index(k)

                amount_x = x2 - x
                amount_y = y2 - y
                absolute_amount_x = abs(amount_x)
                absolute_amount_y = abs(amount_y)

                if "WP" in h:
                    if amount_x == 1 and absolute_amount_y == 1:
                        print(f"The {enemy_color} Pawn on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                elif "WN" in h:
                    if absolute_amount_x == 1 and absolute_amount_y == 2:
                        print(f"The {enemy_color} Knight on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                    elif absolute_amount_x == 2 and absolute_amount_y == 1:
                        print(f"The {enemy_color} Knight on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                elif "WB" in h:
                    if absolute_amount_x == absolute_amount_y:  # diagonal move
                        if y < y2 and x < x2:  # top left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y + g] and not "-BK" in board_pieces[x + g][
                                    y + g] and not \
                                        "-WB" in board_pieces[x + g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y < y2 and x > x2:  # bottom left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y + g] and not "-BK" in board_pieces[x - g][
                                    y + g] and not \
                                        "-WB" in board_pieces[x - g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y > y2 and x < x2:  # top right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y - g] and not "-BK" in board_pieces[x + g][
                                    y - g] and not \
                                        "-WB" in board_pieces[x + g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y > y2 and x > x2:  # bottom right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y - g] and not "-BK" in board_pieces[x - g][
                                    y - g] and not \
                                        "-WB" in board_pieces[x - g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Bishop on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                elif "WQ" in h:
                    if amount_x == 0:  # straight horizontal move
                        if y < y2:
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y + g] and not "-BK" in board_pieces[x][y + g] and not \
                                        "-WQ" in board_pieces[x][y + g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        else:
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y - g] and not "-BK" in board_pieces[x][y - g] and not \
                                        "-WQ" in board_pieces[x][y - g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                    elif amount_y == 0:  # straight vertical move
                        if x < x2:
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x + g][y] and not "-BK" in board_pieces[x + g][y] and not \
                                        "-WQ" in board_pieces[x + g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        else:
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x - g][y] and not "-BK" in board_pieces[x - g][y] and not \
                                        "-WQ" in board_pieces[x - g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                    elif absolute_amount_x == absolute_amount_y:  # diagonal move
                        if y < y2 and x < x2:  # top left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y + g] and not "-BK" in board_pieces[x + g][
                                    y + g] and not \
                                        "-WQ" in board_pieces[x + g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y < y2 and x > x2:  # bottom left
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y + g] and not "-BK" in board_pieces[x - g][
                                    y + g] and not \
                                        "-WQ" in board_pieces[x - g][y + g]:
                                    break
                                else:
                                    if y + g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y > y2 and x < x2:  # top right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x + g][y - g] and not "-BK" in board_pieces[x + g][
                                    y - g] and not \
                                        "-WQ" in board_pieces[x + g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x + g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        elif y > y2 and x > x2:  # bottom right
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x - g][y - g] and not "-BK" in board_pieces[x - g][
                                    y - g] and not \
                                        "-WQ" in board_pieces[x - g][y - g]:
                                    break
                                else:
                                    if y - g == y2 and x - g == x2:
                                        print(f"The {enemy_color} Queen on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                elif "WK" in h:
                    if absolute_amount_x == 1 and absolute_amount_y == 1:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                    elif absolute_amount_x == 1 and absolute_amount_y == 0:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                    elif absolute_amount_x == 0 and absolute_amount_y == 1:
                        print(f"The {enemy_color} King on {h[0:2]} puts the {my_color} King on "
                              f"{my_king_space[0:2]} in Check")
                        turn["player_two_check"] = True
                elif "WR" in h:
                    if amount_x == 0:  # straight horizontal move
                        if y < y2:  # positive y
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y + g] and not "-BK" in board_pieces[x][y + g] and not \
                                        "-WR" in board_pieces[x][y + g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        else:  # negative y
                            for g in range(1, absolute_amount_y + 1):
                                if "-__" not in board_pieces[x][y - g] and not "-BK" in board_pieces[x][y - g] and not \
                                        "-WR" in board_pieces[x][y - g]:
                                    break
                                else:
                                    if y + g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif y - g == y2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                    elif amount_y == 0:  # straight vertical move
                        if x < x2:  # positive x
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x + g][y] and not "-BK" in board_pieces[x + g][y] and not \
                                        "-WR" in board_pieces[x + g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                        else:  # negative x
                            for g in range(1, absolute_amount_x + 1):
                                if "-__" not in board_pieces[x - g][y] and not "-BK" in board_pieces[x - g][y] and not \
                                        "-WR" in board_pieces[x - g][y]:
                                    break
                                else:
                                    if x + g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True
                                    elif x - g == x2:
                                        print(f"The {enemy_color} Rook on {h[0:2]} puts the {my_color} King on "
                                              f"{my_king_space[0:2]} in Check")
                                        turn["player_two_check"] = True



def player_two_cpu_turn():
    pass


def player_two_turn():
    global board_pieces
    turn["player_one"] = False
    check_check()
    if turn["player_two_check"]:
        print("You are in Check!")
    turn["memory"] = copy.deepcopy(board_pieces)
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

    if "-B" in board_pieces[x2][y2]:
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
        amount_x = abs(x2 - x)
        amount_y = abs(y2 - y)
        if amount_x == amount_y:  # diagonal move
            if x2 > x and y2 > y:  # positive x and y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x + i][y + i]:
                        print("You can't move through pieces")
                        player_two_turn()
            else:  # negative x and y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x - i][y - i]:
                        print("You can't move through pieces")
                        player_two_turn()
        elif amount_x == 0:  # straight horizontal move
            if y2 > y:  # positive y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x][y + i]:
                        print("You can't move through pieces")
                        player_two_turn()
            else:  # negative y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x][y - i]:
                        print("You can't move through pieces")
                        player_two_turn()
        elif amount_y == 0:  # straight vertical move
            if x2 > x:  # positive x
                for i in range(1, amount_x + 1):
                    if "-__" not in board_pieces[x + i][y]:
                        print("You can't move through pieces")
                        player_two_turn()
            else:  # negative x
                for i in range(1, amount_x + 1):
                    if "-__" not in board_pieces[x - i][y]:
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
                        if "-__" in taken_piece and "WP" in board_pieces[x2 + 1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                            board_pieces[x2 + 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            player_two_turn()
                    elif y2 == 7:
                        if "-__" in taken_piece and "WP" in board_pieces[x2 + 1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                            board_pieces[x2 + 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            player_two_turn()
                    elif "-__" in taken_piece and "WP" in board_pieces[x2 + 1][y2]:
                        passant["en_passant"] = False
                        print("nothing personal kid *en passant*")
                        board_pieces[x2 + 1][y2] = board[x2 + 1][y2]
                        board_pieces[x2 + 1][y2] += "-__"
                        pass
                    else:
                        print("Invalid move, the pawn cannot move like that")
                        player_two_turn()
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
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
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
                if "-__" in board_pieces[x][y + 1] and "BR" in board_pieces[x][y + 3]:
                    board_pieces[x][y + 1] = board_pieces[x][y + 3]
                    board_pieces[x][y + 3] = board[x][y + 3]
                    board_pieces[x][y + 3] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    player_two_turn()
            elif board_pieces[x][y] == "H5-BK" and board_pieces[x2][y2] == "H3-__" and castle["castling"]:
                if "-__" in board_pieces[x][y - 1] and "-__" in board_pieces[x][y - 3] and "BR" in board_pieces[x][
                    y - 4]:
                    board_pieces[x][y - 1] = board_pieces[x][y - 4]
                    board_pieces[x][y - 4] = board[x][y - 4]
                    board_pieces[x][y - 4] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    player_two_turn()
            else:
                print("Invalid move, the king cannot move like that")
                player_two_turn()
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

    # >>> advanced rook logic // for castling
    if board_pieces[0][7] != "H1-BR":
        castle["castling"] = False
    if board_pieces[7][7] != "H8-BR":
        castle["castling"] = False

    # >>> if in check
    check_check()
    if turn["player_two_check"]:
        print("You are in Check!")
        board_pieces = copy.deepcopy(turn["memory"])
        player_two_turn()

    print("\n")
    print_board()
    print("\n")

    if score["player_two"] >= 100:
        print("You Win, Player Two! Congratulations!")
        print("Player 2's score:", score["player_two"])
        print("Player 1's score:", score["player_one"])
        print("The game took,", turn["count"], "turns")
        print("Thanks for playing!")
        exit()
    elif score["player_one"] >= 100:
        print("Player one Wins!")
        print("Player 1's score:", score["player_one"])
        print("Player 2's score:", score["player_two"])
        print("The game took,", turn["count"], "turns")
        print("Thanks for playing!")
        exit()
    player_one_turn()


def player_one_turn():
    global board_pieces
    # turn["check"] = True
    turn["player_one"] = True
    turn["count"] += 1
    check_check()
    if turn["player_one_check"]:
        print("You are in Check!")
    turn["memory"] = copy.deepcopy(board_pieces)
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
        amount_x = abs(x2 - x)
        amount_y = abs(y2 - y)
        if amount_x == amount_y:  # diagonal move
            if x2 > x and y2 > y:  # positive x and y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x + i][y + i]:
                        print("You can't move through pieces")
                        player_one_turn()
            else:  # negative x and y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x - i][y - i]:
                        print("You can't move through pieces")
                        player_one_turn()
        elif amount_x == 0:  # straight horizontal move
            if y2 > y:  # positive y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x][y + i]:
                        print("You can't move through pieces")
                        player_one_turn()
            else:  # negative y
                for i in range(1, amount_y + 1):
                    if "-__" not in board_pieces[x][y - i]:
                        print("You can't move through pieces")
                        player_one_turn()
        elif amount_y == 0:  # straight vertical move
            if x2 > x:  # positive x
                for i in range(1, amount_x + 1):
                    if "-__" not in board_pieces[x + i][y]:
                        print("You can't move through pieces")
                        player_one_turn()
            else:  # negative x
                for i in range(1, amount_x + 1):
                    if "-__" not in board_pieces[x - i][y]:
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
                        if "-__" in taken_piece and "BP" in board_pieces[x2 - 1][y2]:
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
                        if "-__" in taken_piece and "BP" in board_pieces[x2 - 1][y2]:
                            passant["en_passant"] = False
                            print("nothing personal kid *en passant*")
                            board_pieces[x2 - 1][y2] = board[x2 - 1][y2]
                            board_pieces[x2 - 1][y2] += "-__"
                            pass
                        else:
                            print("Invalid move, the pawn cannot move like that")
                            # print("Test 4")
                            player_one_turn()
                    elif "-__" in taken_piece and "BP" in board_pieces[x2 - 1][y2]:
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
            pass
        elif absolute_x != 0 and absolute_y == 0:
            passant["en_passant"] = False
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
                if "-__" in board_pieces[x][y - 1] and "WR" in board_pieces[x][y - 3]:
                    board_pieces[x][y - 1] = board_pieces[x][y - 3]
                    board_pieces[x][y - 3] = board[x][y - 3]
                    board_pieces[x][y - 3] += "-__"
                    castle["castling"] = False
                else:
                    print("Invalid move, the king cannot move like that")
                    # print("Test 4")
                    player_one_turn()
            elif board_pieces[x][y] == "A4-WK" and board_pieces[x2][y2] == "A6-__" and castle["castling"]:
                if "-__" in board_pieces[x][y + 1] and "-__" in board_pieces[x][y + 3] and "WR" in board_pieces[x][
                    y + 4]:
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

    # >>> advanced rook logic // for castling
    if board_pieces[0][0] != "A1-WR":
        castle["castling"] = False
    if board_pieces[0][7] != "A8-WR":
        castle["castling"] = False

    # turn["check"] = True

    # >>> if in check
    check_check()
    if turn["player_one_check"]:
        print("You are in Check!")
        board_pieces = copy.deepcopy(turn["memory"])
        player_one_turn()

    print("\n")
    print_board()
    print("\n")
    # print("Player 1's score:", score["player_one"])
    if score["player_one"] >= 100:
        print("You Win, Player One! Congratulations!")
        print("Player 1's score:", score["player_one"])
        print("Player 2's score:", score["player_two"])
        print("The game took,", turn["count"], "turns")
        print("Thanks for playing!")
        exit()
    elif score["player_two"] >= 100:
        print("Player Two Wins!")
        print("Player 2's score:", score["player_two"])
        print("Player 1's score:", score["player_one"])
        print("The game took,", turn["count"], "turns")
        print("Thanks for playing!")
        exit()
    player_two_turn()


# print(board_pieces[0][0])
# print(board_pieces[0][1])
# print(board_pieces[1][0])
# print(board_pieces[1][1])

player_one_turn()
