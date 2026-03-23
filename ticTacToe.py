from tkinter import *
import numpy as np

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 8
symbol_X_color = "#EE4035"
symbol_O_color = "#0492CF"
Green_color = "#7BC043"


def print_welcome():
    """Print welcome message and game instructions"""
    print("=" * 70)
    print("🎮 WELCOME TO TIC TAC TOE! 🎮".center(70))
    print("=" * 70)
    print()
    print("📋 GAME DESCRIPTION:")
    print("   Tic Tac Toe is a classic two-player strategy game.")
    print("   Players take turns placing their symbols (X or O) on a 3x3 grid.")
    print("   The first player to get 3 in a row (horizontally, vertically,")
    print("   or diagonally) wins the game!")
    print()
    print("🎯 HOW TO PLAY:")
    print("   1. Player 1 is X (Red) and plays first")
    print("   2. Player 2 is O (Blue)")
    print("   3. Click on any empty cell to place your symbol")
    print("   4. Players alternate turns")
    print("   5. First to get 3 in a row wins!")
    print("   6. If all 9 cells are filled with no winner, it's a TIE")
    print()
    print("🏆 WINNING POSITIONS:")
    print("   ✓ Three in a row horizontally (left to right)")
    print("   ✓ Three in a column vertically (top to bottom)")
    print("   ✓ Three in a diagonal (corner to corner)")
    print()
    print("🎮 GAME RULES:")
    print("   • You cannot place a symbol in an already occupied cell")
    print("   • Players must alternate turns")
    print("   • Game continues until someone wins or all cells are filled")
    print("   • After each game, click to play again!")
    print("   • Scores are tracked across multiple games")
    print()
    print("💡 TIPS:")
    print("   • Try to get 3 in a row before your opponent")
    print("   • Block your opponent's winning moves")
    print("   • Control the center and corners for better positions")
    print()
    print("=" * 70)
    print()


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.game_over = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line(
                (i + 1) * size_of_board / 3,
                0,
                (i + 1) * size_of_board / 3,
                size_of_board,
            )

        for i in range(2):
            self.canvas.create_line(
                0,
                (i + 1) * size_of_board / 3,
                size_of_board,
                (i + 1) * size_of_board / 3,
            )

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(
            grid_position[0] - symbol_size,
            grid_position[1] - symbol_size,
            grid_position[0] + symbol_size,
            grid_position[1] + symbol_size,
            width=symbol_thickness,
            outline=symbol_O_color,
        )

    def draw_X(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(
            grid_position[0] - symbol_size,
            grid_position[1] - symbol_size,
            grid_position[0] + symbol_size,
            grid_position[1] + symbol_size,
            width=symbol_thickness,
            fill=symbol_X_color,
        )
        self.canvas.create_line(
            grid_position[0] - symbol_size,
            grid_position[1] + symbol_size,
            grid_position[0] + symbol_size,
            grid_position[1] - symbol_size,
            width=symbol_thickness,
            fill=symbol_X_color,
        )

    def display_game_over(self):
        if self.X_wins:
            self.X_score += 1
            text = "🎉 X WINS! 🎉"
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = "🎉 O WINS! 🎉"
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = "🤝 TIE! 🤝"
            color = Green_color

        self.canvas.delete("all")
        self.canvas.create_text(
            size_of_board / 2,
            size_of_board / 3,
            font="cmr 50 bold",
            fill=color,
            text=text,
        )

        score_text = "📊 SCORES"
        self.canvas.create_text(
            size_of_board / 2,
            5 * size_of_board / 8,
            font="cmr 35 bold",
            fill=Green_color,
            text=score_text,
        )

        score_text = "Player 1 (X): " + str(self.X_score) + "\n"
        score_text += "Player 2 (O): " + str(self.O_score) + "\n"
        score_text += "Ties: " + str(self.tie_score)
        self.canvas.create_text(
            size_of_board / 2,
            3 * size_of_board / 4,
            font="cmr 25 bold",
            fill=Green_color,
            text=score_text,
        )
        self.reset_board = True

        score_text = "Click to play again ➤"
        self.canvas.create_text(
            size_of_board / 2,
            15 * size_of_board / 16,
            font="cmr 18 bold",
            fill="gray",
            text=score_text,
        )

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return (grid_position // (size_of_board / 3)).astype(int)

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0], logical_position[1]] == 0:
            return False
        else:
            return True

    def is_valid_position(self, logical_position):
        x, y = logical_position
        return 0 <= x < 3 and 0 <= y < 3

    def is_winner(self, player):
        player = -1 if player == "X" else 1

        for i in range(3):
            if (
                self.board_status[i][0]
                == self.board_status[i][1]
                == self.board_status[i][2]
                == player
            ):
                return True
            if (
                self.board_status[0][i]
                == self.board_status[1][i]
                == self.board_status[2][i]
                == player
            ):
                return True

        if (
            self.board_status[0][0]
            == self.board_status[1][1]
            == self.board_status[2][2]
            == player
        ):
            return True
        if (
            self.board_status[0][2]
            == self.board_status[1][1]
            == self.board_status[2][0]
            == player
        ):
            return True

        return False

    def is_tie(self):
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True
        return tie

    def is_game_over(self):
        self.X_wins = self.is_winner("X")
        if not self.X_wins:
            self.O_wins = self.is_winner("O")

        if not self.O_wins:
            self.tie = self.is_tie()

        self.game_over = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print("🎉 X wins!")
        elif self.O_wins:
            print("🎉 O wins!")
        elif self.tie:
            print("🤝 Tie!")

        return self.game_over

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.is_valid_position(logical_position):
            return

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            if self.is_game_over():
                self.display_game_over()

        else:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


# Print welcome message before starting the game
print_welcome()

game_instance = TicTacToe()
game_instance.mainloop()