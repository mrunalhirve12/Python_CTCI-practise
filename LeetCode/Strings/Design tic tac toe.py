"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.symb_dic = {1: "X", 2: "O"}
        self.board = [[""] * n for _ in range(n)]
        self.dic_row = [{} for _ in range(n)]
        self.dic_col = [{} for _ in range(n)]
        self.dic_diag = [{} for _ in range(2)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        symbol = self.symb_dic[player]

        self.board[row][col] = symbol
        if symbol in self.dic_row[row]:
            self.dic_row[row][symbol] += 1
            if self.dic_row[row][symbol] == self.size:
                return player
        else:
            self.dic_row[row][symbol] = 1
        if symbol in self.dic_col[col]:
            self.dic_col[col][symbol] += 1
            if self.dic_col[col][symbol] == self.size:
                return player
        else:
            self.dic_col[col][symbol] = 1
        if row == col:
            if symbol in self.dic_diag[0]:
                self.dic_diag[0][symbol] += 1
                if self.dic_diag[0][symbol] == self.size:
                    return player
            else:
                self.dic_diag[0][symbol] = 1
        if self.size - 1 - row == col:
            if symbol in self.dic_diag[1]:
                self.dic_diag[1][symbol] += 1
                if self.dic_diag[1][symbol] == self.size:
                    return player
            else:
                self.dic_diag[1][symbol] = 1
        return 0