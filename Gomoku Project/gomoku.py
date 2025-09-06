"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""

def is_empty(board):
    for row in board:
        if any(cell != ' ' for cell in row):
            return False
    for column in board:
        if any(cell != ' ' for cell in column):
            return False

    return True


# This function analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED" if the sequence is closed.
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    bound = ''
    sequence = True
    temp_y = y_end + d_y
    temp_x = x_end + d_x
    all_squares = False
    if temp_x<= -1 or temp_x <= -1 or temp_x >=8 or temp_y >= 8 or board[temp_y][temp_x] != ' ':
        for i in range(length+1):
            if y_end <= -1 or x_end <=  -1 or y_end >= 8 or x_end >= 8:
                bound = 'CLOSED'
                break
            elif i < (length-1):
                if sequence == True:
                    if board[y_end][x_end] != ' ':
                        y_end -= d_y
                        x_end -= d_x
                        sequence = True
                    else:
                        sequence = False
                else:
                    break
            elif i == (length-1):
                if sequence == True:
                    y_end -= d_y
                    x_end -= d_x
                    if board [y_end][x_end] != ' ':
                        bound = 'CLOSED'
                    else:
                        bound = 'SEMIOPEN'
    else:
        for i in range(length+1):
            if y_end <= -1 or x_end <=  -1 or y_end >= 8 or x_end >= 8:
                bound = 'SEMIOPEN'
                break
            elif i < (length-1):
                if sequence == True:
                    if board[y_end][x_end] != ' ':
                        y_end -= d_y
                        x_end -= d_x
                        sequence = True
                    else:
                        sequence = False
                else:
                    break
            elif i == (length-1):
                if sequence == True:
                    y_end -= d_y
                    x_end -= d_x
                    if board [y_end][x_end] == ' ':
                        bound = 'OPEN'
                    else:
                        bound = 'SEMIOPEN'
    if sequence == False:
        for i in range(length+1):
            if i < (length-1):
                if board[y_end][x_end] == ' ':
                    y_end -= d_y
                    x_end -= d_x
                    if x_end <= -1 and y_end <=-1:
                        bound = 'SEMIOPEN'
                    else:
                        all_squares = True
                else:
                    bound = 'SEMIOPEN'
            elif i == (length-1):
                y_end -= d_y
                x_end -= d_x
                if board [y_end][x_end] == ' ' and all_squares == True:
                    bound = 'OPEN'
            else:
                bound = 'SEMIOPEN'

    return bound


def detect_row(board, col, y_start, x_start, length, d_y, d_x):

    open_seq_count, semi_open_seq_count = 0, 0
    maybe_semi = False
    count = 0

    #for the vertical rows
    if d_y == 1 and d_x == 0:
        for i in range(len(board) - 1):
            if board[i][x_start] == col:
                if i > 0 and board[i - d_y][x_start - d_x] == ' ':
                    maybe_semi = True

                if count == length - 1:
                    if board[y_start + d_y][i + d_x] == col:
                        count = 0
                        maybe_semi = False
                        continue

                    elif board[i + d_y][x_start + d_x] == ' ':
                        if maybe_semi == True:
                            open_seq_count += 1
                            maybe_semi = False
                        elif board[y_start + d_y][x_start + d_x] == col:
                            pass
                        else:
                            semi_open_seq_count += 1

                else:
                    count += 1
            else:
                maybe_semi = False
                count = 0


            x_start += d_x
            y_start += d_y  #keep checking along the row

    #for the horizontal rows
    elif d_y == 0 and d_x == 1:
        for i in range(len(board) - 1):
            if board[y_start][i] == col:
                if i > 0 and board[y_start - d_y][i - d_x] == ' ':
                    maybe_semi = True

                if count == length - 1:
                    if board[y_start + d_y][i + d_x] == col:
                        count = 0
                        maybe_semi = False
                        continue
                    elif board[y_start + d_y][i + d_x] == ' ':
                        if maybe_semi == True:
                            open_seq_count += 1
                            maybe_semi = False
                        elif board[y_start + d_y][x_start + d_x] == col:
                            pass
                        else:
                            semi_open_seq_count += 1

                else:
                    count += 1
            elif y_start + length - 1 > 7:
                break
            elif x_start + length - 1 > 7:
                break

            else:
                maybe_semi = False
                count = 0


            x_start += d_x
            y_start += d_y  #keep checking along the row

    #for diagonal (lefty)

    elif d_y == 1 and d_x == 1:
        num_diagonal = min(8 - x_start, 8 - y_start)

        for i in range(num_diagonal):
            if board[y_start][x_start] == col:
                count += 1
                if i > 0 and board[y_start - d_y][x_start - d_x] == ' ':
                    maybe_semi = True
                if y_start == 7 and x_start == 7 and board[7][7] == col:
                    if maybe_semi == True:
                        semi_open_seq_count += 1
                elif y_start == 7 or x_start == 7:
                    if maybe_semi == True and length == count:
                        semi_open_seq_count += 1


            else:
                if count == length:
                    if board[y_start][x_start] == col:
                        count = 0
                        maybe_semi = False
                        continue
                    elif board[y_start][x_start] == ' ':
                        if maybe_semi == True:
                            open_seq_count += 1
                            maybe_semi = False
                        else:
                            semi_open_seq_count += 1
                    else:
                        if maybe_semi == True:
                            semi_open_seq_count += 1
                        else:
                            count = 0
                            maybe_semi = False
                            continue


                maybe_semi = False
                count = 0

            y_start += 1
            x_start += 1  #keep checking along the row

    #for diagonal (RIGHTY)

    elif d_y == 1 and d_x == -1:
        num_diagonal = min(x_start + 1, 8 - y_start)

        for i in range(num_diagonal):
            if board[y_start][x_start] == col:
                count += 1
                if i > 0 and board[y_start - d_y][x_start - d_x] == ' ':
                    maybe_semi = True



            else:
                if count == length:
                    if board[y_start][x_start] == col:
                        count = 0
                        maybe_semi = False
                        continue
                    elif board[y_start][x_start] == ' ':
                        if maybe_semi == True:
                            open_seq_count += 1
                            maybe_semi = False

                        else:
                            semi_open_seq_count += 1

                        count = 0
                    else:
                        count = 0
                else:
                    count = 0
                    maybe_semi = False


            y_start += 1
            x_start -= 1
            #keep checking along the row


    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count_final, semi_open_sequence_final = 0, 0

    for i in range(len(board)):
        # detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count_final += detect_row(board, col, i, 0, length, 0, 1)[0]
        semi_open_sequence_final += detect_row(board, col, i, 0, length, 0, 1)[1]

    for i in range(len(board)):
        # detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count_final += detect_row(board, col, 0, i, length, 1, 0)[0]
        semi_open_sequence_final += detect_row(board, col, 0, i, length, 1, 0)[1]

    for i in range(len(board)):
        # detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count_final += detect_row(board, col, 0, i, length, 1, 1)[0]
        semi_open_sequence_final += detect_row(board, col, 0, i, length, 1, 1)[1]

    for i in range(1, len(board)):
        # detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count_final += detect_row(board, col, i, 0, length, 1, 1)[0]
        semi_open_sequence_final += detect_row(board, col, i, 0, length, 1, 1)[1]

    for i in range(len(board)):
        # detect_row(board, col, 0, i, length, 1, -1)
        open_seq_count_final += detect_row(board, col, 0, i, length, 1, -1)[0]
        semi_open_sequence_final += detect_row(board, col, 0, i, length, 1, -1)[1]

    for i in range(1, len(board)):
        # detect_row(board, col, i, len(board) - 1, length, 1, -1)
        open_seq_count_final += detect_row(board, col, i, len(board) - 1, length, 1, -1)[0]
        semi_open_sequence_final += detect_row(board, col, i, len(board) - 1, length, 1, -1)[1]

    return open_seq_count_final, semi_open_sequence_final



def search_max(board):
    max_score = -1
    max_position = 0, 0

    for i in range (len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                board[i][j] = 'b'
                if score(board) > max_score:
                    max_position = i,j
                    max_score = score(board)
                    board[i][j] = ' '
                else:
                    board[i][j] = ' '

    return max_position

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    count = 0
    status = ' '
    index_i = 0
    index_j = 0
    game_state = ' '
    for i in range (len(board)):
        if count == 5:
            break
        for j in range(len(board[i])):
            if count == 5:
                break
            if board[i][j] != ' ':
                index_i = 0
                index_j = 0
                if i!= 7 and j!=7:
                    if board[i][j] == board[i+1][j+1]:
                        index_i += i+1
                        index_j += j+1
                        if index_i < 7 and index_j <7:
                            if board[i][j] == board[i+2][j+2]:
                                index_i += 1
                                index_j += 1
                                if index_i < 7 and index_j <7:
                                    if board[i][j] == board[i+3][j+3]:
                                        index_i += 1
                                        index_j += 1
                                        if index_i < 7 and index_j <7:
                                            if board[i][j] == board[i+4][j+4]:
                                                count += 5
                                                col = board[i][j]
                    elif board[i][j] == board[i][j+1]:
                        index_j += j+1
                        if index_j < 7:
                            if board[i][j] == board[i][j+2]:
                                index_j += 1
                                if index_j < 7:
                                    if board[i][j] == board[i][j+3]:
                                        index_j += 1
                                        if index_j < 7:
                                            if board[i][j] == board[i][j+4]:
                                                count = 5
                                                col = board[i][j]

                    elif board[i][j] == board[i+1][j]:
                        index_i += i+1
                        if index_i < 7:
                            if board[i][j] == board[i+2][j]:
                                index_i += 1
                                if index_i < 7:
                                    if board[i][j] == board[i+3][j]:
                                        index_i += 1
                                        if index_i < 7:
                                            if board[i][j] == board[i+4][j]:
                                                count = 5
                                                col = board[i][j]
    if count == 5:
        if col == 'b':
            game_state = "Black Won"
        elif col == 'w':
            game_state = "White Won"
    else:
        for i in range (len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    status = 'empty_square'
                elif status != 'empty_square' and board[i][j] != ' ':
                    status = 'no_empty_square'
        if status == 'empty_square':
            game_state = "Continue Playing"
        elif status == 'no_empty_square':
            game_state = "Draw"

    return game_state


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    print(detect_row(board, "w", 0,x,length,d_y,d_x))
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    test_detect_rows()
    # #test_detect_row()
    board = make_empty_board(8)
    #put_seq_on_board(board, 1, 0, 0, 1, 1, 'w')
    #put_seq_on_board(board, 1, 2, 0, 1, 1, 'w')
    put_seq_on_board(board, 1, 1, 1, 1, 2, 'w')
    #put_seq_on_board(board, 2, 2, 1, 1, 2, 'w')
    put_seq_on_board(board, 3, 3, 1, 0, 2, 'b')
    #put_seq_on_board(board, 0, 4, 0, 0, 1, 'b')
    print_board(board)
    print(detect_row(board, 'w', 0, 0, 2, 1, 1))
    # #test_detect_rows()

