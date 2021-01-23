import numpy as np


def assist_push_left(board, row, column):
    """Moves board to the left"""
    if row == 4:
        return
    elif column == 3:
        row = row + 1
        column = 0
        assist_push_left(board, row, column)
    elif board[row][column + 1] != 0 and board[row][column] == 0:
        board[row][column] = board[row][column + 1]
        board[row][column + 1] = 0
        if column < 1:
            assist_push_left(board, row, column + 1)
        else:
            assist_push_left(board, row, column - 1)
    elif board[row][column] == board[row][column + 1] and board[row][column] != 0:
        temp = board[row][column]
        board[row][column] = temp * 2
        board[row][column + 1] = 0
        assist_push_left(board, row, column + 1)
    elif board[row][column] != board[row][column + 1]:
        assist_push_left(board, row, column + 1)
    elif board[row][column] == 0 and board[row][column + 1] == 0:
        assist_push_left(board, row, column + 1)


def assist_push_up(board, row, column):
    """Moves board up"""
    if column == 4:
        return
    elif row == 3:
        column = column + 1
        row = 0
        assist_push_up(board, row, column)
    elif board[row + 1][column] != 0 and board[row][column] == 0:
        board[row][column] = board[row + 1][column]
        board[row + 1][column] = 0
        if row < 1:
            assist_push_up(board, row + 1, column)
        else:
            assist_push_up(board, row - 1, column)
    elif board[row][column] == board[row + 1][column] and board[row][column] != 0:
        temp = board[row][column]
        board[row + 1][column] = 0
        board[row][column] = temp * 2
        assist_push_up(board, row + 1, column)
    elif board[row][column] != board[row + 1][column]:
        assist_push_up(board, row + 1, column)
    elif board[row][column] == 0 and board[row + 1][column] == 0:
        assist_push_up(board, row + 1, column)


def assist_push_right(board, row, column):
    """Moves board to the right"""
    if column == 0 and row == 3:
        return
    elif column == 0:
        row = row + 1
        column = 3
        assist_push_right(board, row, column)
    elif board[row][column - 1] != 0 and board[row][column] == 0:
        board[row][column] = board[row][column - 1]
        board[row][column - 1] = 0
        if column < 3:
            assist_push_right(board, row, column + 1)
        else:
            assist_push_right(board, row, column - 1)
    elif board[row][column] == board[row][column - 1] and board[row][column] != 0:
        temp = board[row][column]
        board[row][column] = temp * 2
        board[row][column - 1] = 0
        assist_push_right(board, row, column - 1)
    elif board[row][column] != board[row][column - 1]:
        assist_push_right(board, row, column - 1)
    elif board[row][column] == 0 and board[row][column - 1] == 0:
        assist_push_right(board, row, column - 1)


def assist_push_down(board, row, column):
    """Moves board upt"""
    if column == 4:
        return
    elif row == 0:
        column = column + 1
        row = 3
        assist_push_down(board, row, column)
    elif board[row - 1][column] != 0 and board[row][column] == 0:
        board[row][column] = board[row - 1][column]
        board[row - 1][column] = 0
        if row < 3:
            assist_push_down(board, row + 1, column)
        else:
            assist_push_down(board, row - 1, column)
    elif board[row][column] == board[row - 1][column] and board[row][column] != 0:
        temp = board[row][column]
        board[row][column] = temp * 2
        board[row - 1][column] = 0
        assist_push_down(board, row - 1, column)
    elif board[row][column] != board[row - 1][column]:
        assist_push_down(board, row - 1, column)
    elif board[row][column] == 0 and board[row - 1][column] == 0:
        assist_push_down(board, row - 1, column)


class Board:
    """Board class which has its own functions to manipulate board"""

    def __init__(self):
        """Initializes it self with only the board"""
        self.board = np.zeros((4, 4))

    def to_string(self):
        print(self.board)

    def edit_board(self, column, row, value):
        self.board[row, column] = value

    def get_value(self, row, column):
        return self.board[row, column]

    def push_entire_board_left(self):
        assist_push_left(self.board, 0, 0)

    def push_entire_board_right(self):
        assist_push_right(self.board, 0, 3)

    def push_entire_board_up(self):
        assist_push_up(self.board, 0, 0)

    def push_entire_board_down(self):
        assist_push_down(self.board, 3, 0)

    def check_down(self):
        check_board = []
        count = 0
        for element in np.nditer(self.board):
            check_board.append(element)
        for items in check_board:
            if count <= 11:
                if ((int(items) == int(check_board[count + 4]) or int(check_board[count + 4]) == 0)
                        and check_board[count] != 0):
                    return True
            count = count + 1
        return False

    def check_up(self):
        check_board = []
        count = 0
        for element in np.nditer(self.board):
            check_board.append(element)
        for items in check_board:
            if count >= 4:
                if ((int(items) == int(check_board[count - 4]) or int(check_board[count - 4]) == 0)
                        and check_board[count] != 0):
                    return True
            count = count + 1
        return False

    def check_right(self):
        check_board = []
        count = 0
        for element in np.nditer(self.board):
            check_board.append(element)
        for items in check_board:
            if count != 3 and count != 7 and count != 11 and count != 15:
                if ((int(items) == int(check_board[count + 1]) or int(check_board[count + 1]) == 0)
                        and check_board[count] != 0):
                    return True
            count = count + 1
        return False

    def check_left(self):
        check_board = []
        count = 0
        for element in np.nditer(self.board):
            check_board.append(element)
        for items in check_board:
            if count != 0 and count != 4 and count != 8 and count != 12:
                if ((int(items) == int(check_board[count - 1]) or int(check_board[count - 1]) == 0)
                        and check_board[count] != 0):
                    return True
            count = count + 1
        return False

    def iterate(self):
        counter = 0
        for cell in np.nditer(self.board):
            if cell == 0:
                counter = counter + 1
        return counter

    def check_board(self):
        if (self.check_left() == False and self.check_right() == False
                and self.check_up() == False and self.check_down() == False):
            return False
        else:
            return True
