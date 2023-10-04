# Author: Leonel Garay
# Date: 11/14/2019
# Description: TicTacToe game with a list of lists that represent a 3x3 board and current state.


class TicTacToe:
    """Class with two private data members: board and current state."""

    def __init__(self):
        """Initialize the board to a list of 3 list each with 3 empty strings and the current state to Unfinished"""
        self._board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self._current_state = "UNFINISHED"
        self.moves = 0

    def get_current_state(self):
        """Returns the Current State of the Game"""
        return self._current_state

    def make_move(self, row, col, player):
        """Decides what to do with each movement."""
        if 0 <= row <= 2 and 0 <= col <= 2 and player in "XO":
            if self._board[row][0] == player and self._board[row][1] == player and self._board[row][2] == player:
                self._current_state = str(player) + "_WON"
            if self._board[0][col] == player and self._board[1][col] == player and self._board[2][col] == player:
                self._current_state = str(player) + "_WON"
            return False
        if self.moves == 9:
            self._current_state = "DRAW"
            return False
        if 0 > row > 2 or 0 > col > 2:
            return False
        if self._current_state == "UNFINISHED":
            self._board[row][col] = player
            self.moves += 1
            return True
