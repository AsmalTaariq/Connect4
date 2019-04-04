import numpy as np


class Connect4:
    def __init__(self, rows=6, cols=7, win=4):
        self.rows = rows
        self.cols = cols
        self.win = win
        self.board = np.zeros((rows,cols))

    def remaining_spaces(self):
        return self.rows * self.cols - np.count_nonzero(self.board)

    def check_win(self):
        if self.vertical_check() != 0:
            return self.vertical_check()

        if self.horizontal_check() != 0:
            return self.horizontal_check()

        if self.diagonal_check() != 0:
            return self.diagonal_check()

        return 0

    def vertical_check(self):
        for col in range(0, self.cols - self.win + 1):
            current_row = 0
            in_a_row = 1
            while current_row < self.rows:
                if self.board[current_row][col] == 0:
                    break
                if self.board[current_row][col] == self.board[current_row - 1][col]:
                    in_a_row += 1
                else:
                    in_a_row = 1

                if in_a_row == self.win:
                    return self.board[current_row][col]
                current_row += 1
        return 0

    def horizontal_check(self):
        for row in range(0, self.rows - self.win + 1):
            current_col = 0
            in_a_row = 1
            while current_col < self.cols:
                if self.board[row][current_col] == 0:
                    in_a_row = 1
                elif self.board[row][current_col] == self.board[row][current_col - 1]:
                    in_a_row += 1
                else:
                    in_a_row = 1

                if in_a_row == self.win:
                    return self.board[row][current_col]

                if in_a_row + (self.cols - current_col) < self.win:
                    break
                current_col += 1
        return 0

    def diagonal_check(self):
        #positive diagonals
        for start_row in range(1, self.rows - self.win + 1):
            for start_col in range(1, self.cols - self.win + 1):
                in_a_row = 1
                for offset in range(self.win):
                    if self.board[start_row + offset][start_col + offset] == 0:
                        break
                    elif self.board[start_row + offset][start_col + offset] != self.board[start_row + offset - 1][start_col + offset - 1]:
                        break
                    else:
                        in_a_row += 1
                    if in_a_row == self.win:
                        return self.board[start_row + offset][start_col + offset]

        # negative diagonals
        for start_row in range(self.rows - 2, self.win, -1):
            for start_col in range(1, self.cols - self.win + 1):
                in_a_row = 1
                for offset in range(self.win):
                    if self.board[start_row - offset][start_col + offset] == 0:
                        break
                    elif self.board[start_row - offset][start_col + offset] != self.board[start_row - offset + 1][start_col + offset - 1]:
                        break
                    else:
                        in_a_row += 1
                    if in_a_row == self.win:
                        return self.board[start_row + offset][start_col + offset]

        return 0

    def get_free_row(self, col):
        for row in range(self.rows):
            if self.board[row][col] == 0:
                return row
        return -1

    def make_move(self, col, player):
        if self.board[self.rows-1][col] == 0:
            free_row = self.get_free_row(col)
            self.board[free_row][col] = player
        return self.check_win() == player

    def get_board_for_training(self):
        return np.array([self.board])

    def __str__(self):
        return str(np.flip(self.board,0))
#
#
# game = Connect4()
# NUM_PLAYERS = 2
# player = 0
# while game.remaining_spaces() != 0:
#     print("BOARD:")
#     print(game)
#     col = int(input("Player " + str(player + 1) + " enter a column (zero index):"))
#     if game.make_move(col,player + 1):
#         print("Player ", player + 1, "has won")
#         break
#     player = (player + 1) % 2
#
# if game.remaining_spaces() == 0:
#     print("Drawn Game")
# print("!!!GAME OVER!!!")
# print(game)
