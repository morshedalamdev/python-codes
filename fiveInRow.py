from tkinter import *
from tkinter import messagebox
import numpy as np

# Game Constants
BOARD_SIZE = 15
GRID_SIZE = 30

BOARD_WIDTH = BOARD_SIZE * GRID_SIZE
BOARD_HEIGHT = BOARD_SIZE * GRID_SIZE

PIECE_RADIUS = GRID_SIZE // 2 - 2

# Colors
BOARD_COLOR = "#CD853F"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"
GRID_COLOR = "#5D2A05"
WIN_COLOR = "#009D05"

# Piece values
EMPTY = 0
BLACK = 1
WHITE = 2


def print_welcome():
    """Print welcome message and game instructions"""
    print("=" * 75)
    print("🎮 WELCOME TO FIVE IN A ROW (GOMOKU)! 🎮".center(75))
    print("=" * 75)
    print()
    print("📋 GAME DESCRIPTION:")
    print("   Five In A Row is an ancient strategy board game.")
    print("   Players take turns placing pieces on a 15x15 grid.")
    print("   The first player to align 5 pieces in a row (horizontally,")
    print("   vertically, or diagonally) wins the game!")
    print()
    print("🎯 GAME RULES:")
    print("   1. Each player holds pieces of the same color (Black vs White)")
    print("   2. Start with an empty 15x15 chessboard")
    print("   3. Black plays first, White plays second")
    print("   4. Players alternate turns, placing one piece at a time")
    print("   5. Pieces are placed on empty intersections only")
    print("   6. Once placed, pieces CANNOT be moved or removed")
    print("   7. Black's first move can be placed on ANY intersection")
    print("   8. First player to get 5 in a row wins!")
    print()
    print("🎮 HOW TO PLAY:")
    print("   1. A 15x15 chessboard will appear on the screen")
    print("   2. Black (●) plays first - click any empty intersection")
    print("   3. White (○) plays second - click any empty intersection")
    print("   4. Continue alternating turns")
    print("   5. Try to align 5 pieces in a row before your opponent")
    print("   6. Game ends when someone gets 5 in a row or board is full")
    print()
    print("🏆 WINNING POSITIONS:")
    print("   ✓ Five in a row horizontally (→)")
    print("   ✓ Five in a column vertically (↓)")
    print("   ✓ Five in a diagonal (↘ or ↙)")
    print()
    print("💡 TIPS:")
    print("   • Control the center of the board for better positions")
    print("   • Defend against opponent's winning combinations")
    print("   • Create multiple threats to force opponent into defense")
    print("   • Look ahead several moves to plan your strategy")
    print()
    print("=" * 75)
    print()

class FiveInRow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Five In A Row (Gomoku)")
        self.window.geometry(f"{BOARD_WIDTH + 100}x{BOARD_HEIGHT + 100}")

        # Create canvas for the board
        self.canvas = Canvas(
            self.window,
            width=BOARD_WIDTH,
            height=BOARD_HEIGHT,
            bg=BOARD_COLOR,
            bd=2,
            relief=RAISED,
        )
        self.canvas.pack(pady=10, padx=10)
        self.canvas.bind("<Button-1>", self.on_click)

        # Create info frame
        self.info_frame = Frame(self.window)
        self.info_frame.pack()

        self.info_label = Label(self.info_frame, text="", font=("Arial", 12, "bold"))
        self.info_label.pack()

        self.reset_button = Button(
            self.info_frame,
            text="🔄 New Game",
            command=self.reset_game,
            font=("Arial", 10),
        )
        self.reset_button.pack(pady=5)

        # Initialize game state
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = BLACK
        self.game_over = False
        self.move_count = 0
        self.winning_positions = []  # Store winning pieces positions

        self.draw_board()
        self.update_info()

    def draw_board(self):
        """Draw the chessboard grid"""
        self.canvas.delete("all")

        # Draw grid lines
        for i in range(BOARD_SIZE):
            # Horizontal lines
            self.canvas.create_line(
                0, i * GRID_SIZE, BOARD_WIDTH, i * GRID_SIZE, fill=GRID_COLOR
            )
            # Vertical lines
            self.canvas.create_line(
                i * GRID_SIZE, 0, i * GRID_SIZE, BOARD_HEIGHT, fill=GRID_COLOR
            )

        # Draw pieces
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] != EMPTY:
                    self.draw_piece(i, j, self.board[i][j])

        # Draw winning line if game is over
        if self.game_over and len(self.winning_positions) >= 5:
            self.draw_winning_line()

    def draw_piece(self, row, col, player):
        """Draw a piece on the board"""
        x = col * GRID_SIZE
        y = row * GRID_SIZE
        color = BLACK_COLOR if player == BLACK else WHITE_COLOR

        self.canvas.create_oval(
            x - PIECE_RADIUS,
            y - PIECE_RADIUS,
            x + PIECE_RADIUS,
            y + PIECE_RADIUS,
            fill=color,
            outline=GRID_COLOR,
            width=2,
        )

    def draw_winning_line(self):
        """Draw a red line through the winning pieces"""
        if len(self.winning_positions) < 5:
            return

        # Get the first and last winning piece
        first_pos = self.winning_positions[0]
        last_pos = self.winning_positions[-1]

        # Convert to pixel coordinates
        x1 = first_pos[1] * GRID_SIZE
        y1 = first_pos[0] * GRID_SIZE
        x2 = last_pos[1] * GRID_SIZE
        y2 = last_pos[0] * GRID_SIZE

        # Draw the line
        self.canvas.create_line(x1, y1, x2, y2, fill=WIN_COLOR, width=5)

    def on_click(self, event):
        """Handle mouse click on the board"""
        if self.game_over:
            return

        # Convert pixel coordinates to board coordinates
        col = round(event.x / GRID_SIZE)
        row = round(event.y / GRID_SIZE)

        # Check if click is within board bounds
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            messagebox.showwarning("Invalid Move", "Please click on the board!")
            return

        # Check if position is empty
        if self.board[row][col] != EMPTY:
            messagebox.showwarning("Invalid Move", "That position is already occupied!")
            return

        # Place the piece
        self.board[row][col] = self.current_player
        self.move_count += 1

        # Check for winner
        if self.check_winner(row, col, self.current_player):
            self.game_over = True
            player_name = "⚫ Black" if self.current_player == BLACK else "⚪ White"
            messagebox.showinfo(
                "Game Over",
                f"{player_name} WINS! 🎉\n\nA red line shows the winning path!\n\nCongratulations!",
            )

        # Check for tie
        elif self.move_count == BOARD_SIZE * BOARD_SIZE:
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a TIE! 🤝\n\nBoard is full!")

        # Switch player
        self.current_player = WHITE if self.current_player == BLACK else BLACK

        # Redraw board and update info
        self.draw_board()
        self.update_info()

    def check_winner(self, row, col, player):
        """Check if the current player has won"""
        directions = [
            (0, 1),  # Horizontal
            (1, 0),  # Vertical
            (1, 1),  # Diagonal \
            (1, -1),  # Diagonal /
        ]

        for dr, dc in directions:
            count = 1  # Count the piece just placed
            positions = [(row, col)]  # Store positions in this direction

            # Check in positive direction
            r, c = row + dr, col + dc
            while (
                0 <= r < BOARD_SIZE
                and 0 <= c < BOARD_SIZE
                and self.board[r][c] == player
            ):
                count += 1
                positions.append((r, c))
                r += dr
                c += dc

            # Check in negative direction
            r, c = row - dr, col - dc
            while (
                0 <= r < BOARD_SIZE
                and 0 <= c < BOARD_SIZE
                and self.board[r][c] == player
            ):
                count += 1
                positions.append((r, c))
                r -= dr
                c -= dc

            # If 5 or more in a row, player wins
            if count >= 5:
                # Store the winning positions (first 5 pieces in the line)
                self.winning_positions = sorted(positions[:5])
                return True

        return False

    def update_info(self):
        """Update the information label"""
        if self.game_over:
            self.info_label.config(text="Game Over! Click 'New Game' to play again.")
        else:
            player_name = "⚫ Black" if self.current_player == BLACK else "⚪ White"
            self.info_label.config(
                text=f"Current Player: {player_name} | Moves: {self.move_count}"
            )

    def reset_game(self):
        """Reset the game"""
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = BLACK
        self.game_over = False
        self.move_count = 0
        self.winning_positions = []  # Clear winning positions
        self.draw_board()
        self.update_info()

    def mainloop(self):
        """Start the game"""
        self.window.mainloop()

# Print welcome message and instructions
print_welcome()
# Start the game
game = FiveInRow()
game.mainloop()
