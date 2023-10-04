# Author: Leonel Garay
# Date: 11/19/2019
# Description: Game where X is trying to get to row 7 and O is trying to make it so X doesn't have any legal moves.


class FBoard:
    """Game where X is trying to get to row 7 and O is trying to make it so X doesn't have any legal moves."""

    def __init__(self):
        """Initializes the list (8*8), game state, position of x, and the positions 3 o and 1 x."""
        self._board = [["", "", "", "X", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["O", "", "O", "", "O", "", "O", ""]]
        self._game_state = "UNFINISHED"  # State of game at the beginning.
        self._x_pos_row = 0  # Row position for X.
        self._x_pos_col = 3  # Column position for X.

    def get_game_state(self):
        """Returns the current state of the game"""
        return self._game_state

    def move_x(self, row, col):
        """Decides what to do with movement by X Player"""
        if self._game_state == "X_WON" or self._game_state == "Y_WON":  # If game has been won, game ends.
            return False
        if self._board[row][col] != "":  # If cell is not empty, cannot move there.
            return False
        if 0 > row > 7 or 0 > col > 7 or row > self._x_pos_row + 1 or row == self._x_pos_row or \
                col > self._x_pos_col + 1 or row < self._x_pos_row - 1 or col < self._x_pos_col - 1:  # Allowed X moves.
            return False
        else:
            self._board[self._x_pos_row][self._x_pos_col] = ""  # Makes the previous position for X an empty cell.
            self._x_pos_row = row
            self._x_pos_col = col
            self._board[row][col] = "X"  # Places X in the new position.
            if "X" in self._board[7]:  # If X is found in [7:x] then X_WON.
                self._game_state = "X_WON"
            return True

    def move_o(self, cur_row, cur_col, row, col):
        """Decides what to do with movement by O Player"""
        if self._game_state == "X_WON" or self._game_state == "O_WON":  # If game has been won, game ends.
            return False
        if self._board[row][col] != "":  # If cell is not empty, cannot move there.
            return False
        if 0 > row > 7 or 0 > col > 7 or row > cur_row or \
                col > cur_col + 1 or row < cur_row - 1 or col < cur_col - 1:  # Allowed O moves.
            return False
        else:
            self._board[cur_row][cur_col] = ""  # Makes the previous position for O an empty cell.
            self._board[row][col] = "O"  # Places O in the new position.
            if (self._board[row - 1][col] == "X" and self._board[row - 1][col + 1] == "O" and self._board[row - 1][col - 1] == "O" and self._board[row - 2][col] == "O") or \
                    (self._board[row][col - 1] == "X" and self._board[row + 1][col - 1] == "O" and (self._board[row][col - 2] == "O" or self._board[row][col - 2] is None) and self._board[row - 1][col - 1] == "O"):
                self._game_state = "O_WON"
            return True
