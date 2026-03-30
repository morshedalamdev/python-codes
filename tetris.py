from tkinter import *
from tkinter import messagebox
import random


class TetrisGame:
    def __init__(self):
        """Initialize game window, state, controls, and loop."""

        # Window setup
        self.window = Tk()
        self.window.title("Tetris Game")
        self.window.geometry("500x660")
        self.window.resizable(False, False)

        # Board and cell configuration
        self.grid_width = 10
        self.grid_height = 20
        self.cell_size = 30

        # Theme colors
        self.bg_color = "#1A1A1A"
        self.grid_color = "#333333"
        self.text_color = "#FFFFFF"

        # Piece colors (0 means empty)
        self.colors = {
            0: self.bg_color,
            1: "#00FFFF",  # I
            2: "#0000FF",  # J
            3: "#FFA500",  # L
            4: "#FFFF00",  # O
            5: "#00FF00",  # S
            6: "#FF0000",  # Z
            7: "#AA00FF",  # T
        }

        # UI containers
        self.container = Frame(self.window, bg=self.bg_color)
        self.container.pack(padx=12, pady=12)

        self.canvas = Canvas(
            self.container,
            width=self.grid_width * self.cell_size,
            height=self.grid_height * self.cell_size,
            bg=self.bg_color,
            highlightthickness=2,
            highlightbackground=self.grid_color,
        )
        self.canvas.grid(row=0, column=0, padx=(0, 16), pady=8)

        self.info_frame = Frame(self.container, bg=self.bg_color)
        self.info_frame.grid(row=0, column=1, sticky="n")

        self.score_label = Label(
            self.info_frame,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
        )
        self.score_label.pack(pady=8)

        self.level_label = Label(
            self.info_frame,
            text="Level: 1",
            font=("Arial", 14, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
        )
        self.level_label.pack(pady=8)

        self.lines_label = Label(
            self.info_frame,
            text="Lines: 0",
            font=("Arial", 14, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
        )
        self.lines_label.pack(pady=8)

        self.next_piece_label = Label(
            self.info_frame,
            text="Next Piece: -",
            font=("Arial", 12, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
        )
        self.next_piece_label.pack(pady=(20, 8))

        self.instructions_label = Label(
            self.info_frame,
            text=(
                "Controls:\n"
                "Up: Rotate\n"
                "Left/Right: Move\n"
                "Down: Soft Drop\n"
                "Space: Hard Drop\n"
                "Enter: Change Shape\n"
                "P: Pause"
            ),
            font=("Arial", 10),
            justify=LEFT,
            fg="#CCCCCC",
            bg=self.bg_color,
        )
        self.instructions_label.pack(pady=10)

        # Tetromino rotations
        self.pieces = {
            "I": [
                [(0, 1), (1, 1), (2, 1), (3, 1)],
                [(2, 0), (2, 1), (2, 2), (2, 3)],
                [(0, 2), (1, 2), (2, 2), (3, 2)],
                [(1, 0), (1, 1), (1, 2), (1, 3)],
            ],
            "J": [
                [(0, 0), (0, 1), (1, 1), (2, 1)],
                [(1, 0), (2, 0), (1, 1), (1, 2)],
                [(0, 1), (1, 1), (2, 1), (2, 2)],
                [(1, 0), (1, 1), (0, 2), (1, 2)],
            ],
            "L": [
                [(2, 0), (0, 1), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (1, 2), (2, 2)],
                [(0, 1), (1, 1), (2, 1), (0, 2)],
                [(0, 0), (1, 0), (1, 1), (1, 2)],
            ],
            "O": [
                [(1, 0), (2, 0), (1, 1), (2, 1)],
                [(1, 0), (2, 0), (1, 1), (2, 1)],
                [(1, 0), (2, 0), (1, 1), (2, 1)],
                [(1, 0), (2, 0), (1, 1), (2, 1)],
            ],
            "S": [
                [(1, 0), (2, 0), (0, 1), (1, 1)],
                [(1, 0), (1, 1), (2, 1), (2, 2)],
                [(1, 1), (2, 1), (0, 2), (1, 2)],
                [(0, 0), (0, 1), (1, 1), (1, 2)],
            ],
            "Z": [
                [(0, 0), (1, 0), (1, 1), (2, 1)],
                [(2, 0), (1, 1), (2, 1), (1, 2)],
                [(0, 1), (1, 1), (1, 2), (2, 2)],
                [(1, 0), (0, 1), (1, 1), (0, 2)],
            ],
            "T": [
                [(1, 0), (0, 1), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (2, 1), (1, 2)],
                [(0, 1), (1, 1), (2, 1), (1, 2)],
                [(1, 0), (0, 1), (1, 1), (1, 2)],
            ],
        }

        self.piece_color_index = {
            "I": 1,
            "J": 2,
            "L": 3,
            "O": 4,
            "S": 5,
            "Z": 6,
            "T": 7,
        }

        # Game state
        self.board = [
            [0 for _ in range(self.grid_width)] for _ in range(self.grid_height)
        ]
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_speed = 600
        self.paused = False
        self.game_over = False

        self.current_piece_type = None
        self.current_piece = None
        self.piece_rotation = 0
        self.piece_x = 3
        self.piece_y = 0
        self.piece_color = 0
        self.next_piece_type = random.choice(list(self.pieces.keys()))

        # Controls
        self.window.bind("<Up>", self.rotate_piece)
        self.window.bind("<Left>", self.move_piece_left)
        self.window.bind("<Right>", self.move_piece_right)
        self.window.bind("<Down>", self.move_piece_down)
        self.window.bind("<space>", self.hard_drop)
        self.window.bind("<Return>", self.change_shape)
        self.window.bind("<p>", self.toggle_pause)
        self.window.bind("<P>", self.toggle_pause)

        self.spawn_piece()
        self.update_game()

    def spawn_piece(self):
        """Spawn a new piece at the top center."""

        self.current_piece_type = self.next_piece_type
        self.next_piece_type = random.choice(list(self.pieces.keys()))
        self.next_piece_label.config(text=f"Next Piece: {self.next_piece_type}")

        self.piece_rotation = 0
        self.current_piece = self.pieces[self.current_piece_type][self.piece_rotation]
        self.piece_color = self.piece_color_index[self.current_piece_type]
        self.piece_x = 3
        self.piece_y = 0

        if not self.is_valid_position(self.piece_x, self.piece_y, self.current_piece):
            self.game_over = True
            self.show_game_over()

    def is_valid_position(self, x, y, piece):
        """Return True if piece can be placed at (x, y)."""

        for dx, dy in piece:
            px = x + dx
            py = y + dy

            if px < 0 or px >= self.grid_width:
                return False
            if py < 0 or py >= self.grid_height:
                return False
            if self.board[py][px] != 0:
                return False

        return True

    def move_piece_left(self, event=None):
        if self.paused or self.game_over:
            return
        if self.is_valid_position(self.piece_x - 1, self.piece_y, self.current_piece):
            self.piece_x -= 1
            self.draw_game()

    def move_piece_right(self, event=None):
        if self.paused or self.game_over:
            return
        if self.is_valid_position(self.piece_x + 1, self.piece_y, self.current_piece):
            self.piece_x += 1
            self.draw_game()

    def move_piece_down(self, event=None):
        if self.paused or self.game_over:
            return
        if self.is_valid_position(self.piece_x, self.piece_y + 1, self.current_piece):
            self.piece_y += 1
        else:
            self.lock_piece()
        self.draw_game()

    def hard_drop(self, event=None):
        if self.paused or self.game_over:
            return
        while self.is_valid_position(
            self.piece_x, self.piece_y + 1, self.current_piece
        ):
            self.piece_y += 1
        self.lock_piece()
        self.draw_game()

    def rotate_piece(self, event=None):
        if self.paused or self.game_over:
            return

        next_rotation = (self.piece_rotation + 1) % 4
        rotated_piece = self.pieces[self.current_piece_type][next_rotation]

        # Basic wall-kick checks
        for kick_x in (0, -1, 1, -2, 2):
            if self.is_valid_position(
                self.piece_x + kick_x, self.piece_y, rotated_piece
            ):
                self.piece_rotation = next_rotation
                self.current_piece = rotated_piece
                self.piece_x += kick_x
                self.draw_game()
                return

    def change_shape(self, event=None):
        """Change current piece to another random shape while keeping position."""

        if self.paused or self.game_over:
            return

        current_type = self.current_piece_type
        candidates = [piece for piece in self.pieces.keys() if piece != current_type]
        random.shuffle(candidates)

        # Try each candidate shape and rotation at current x/y first, then with small x kicks.
        for piece_type in candidates:
            for rotation in range(4):
                next_piece = self.pieces[piece_type][rotation]
                for kick_x in (0, -1, 1, -2, 2):
                    next_x = self.piece_x + kick_x
                    if self.is_valid_position(next_x, self.piece_y, next_piece):
                        self.current_piece_type = piece_type
                        self.piece_rotation = rotation
                        self.current_piece = next_piece
                        self.piece_color = self.piece_color_index[piece_type]
                        self.piece_x = next_x
                        self.draw_game()
                        return

    def toggle_pause(self, event=None):
        if self.game_over:
            return
        self.paused = not self.paused
        status = "Paused" if self.paused else "Running"
        self.instructions_label.config(
            text=(
                "Controls:\n"
                "Up: Rotate\n"
                "Left/Right: Move\n"
                "Down: Soft Drop\n"
                "Space: Hard Drop\n"
                "Enter: Change Shape\n"
                f"P: Pause ({status})"
            )
        )

    def lock_piece(self):
        """Write current piece into board and spawn next."""

        for dx, dy in self.current_piece:
            px = self.piece_x + dx
            py = self.piece_y + dy
            if 0 <= px < self.grid_width and 0 <= py < self.grid_height:
                self.board[py][px] = self.piece_color

        self.clear_lines()
        self.spawn_piece()

    def clear_lines(self):
        """Clear all complete rows and update score/level."""

        full_rows = [
            y
            for y in range(self.grid_height)
            if all(self.board[y][x] != 0 for x in range(self.grid_width))
        ]
        if not full_rows:
            return

        for y in sorted(full_rows, reverse=True):
            del self.board[y]
            self.board.insert(0, [0 for _ in range(self.grid_width)])

        count = len(full_rows)
        self.lines_cleared += count

        score_table = {1: 100, 2: 300, 3: 500, 4: 800}
        self.score += score_table.get(count, 0) * self.level

        old_level = self.level
        self.level = 1 + self.lines_cleared // 10
        if self.level > old_level:
            self.fall_speed = max(120, self.fall_speed - 50)

    def draw_game(self):
        """Render board and current piece."""

        self.canvas.delete("all")

        for y in range(self.grid_height):
            for x in range(self.grid_width):
                px = x * self.cell_size
                py = y * self.cell_size
                color = self.colors[self.board[y][x]]
                self.canvas.create_rectangle(
                    px,
                    py,
                    px + self.cell_size,
                    py + self.cell_size,
                    fill=color,
                    outline=self.grid_color,
                )

        if self.current_piece and not self.game_over:
            for dx, dy in self.current_piece:
                px = (self.piece_x + dx) * self.cell_size
                py = (self.piece_y + dy) * self.cell_size
                self.canvas.create_rectangle(
                    px,
                    py,
                    px + self.cell_size,
                    py + self.cell_size,
                    fill=self.colors[self.piece_color],
                    outline="#FFFFFF",
                    width=2,
                )

        if self.game_over:
            mid_y = self.grid_height * self.cell_size // 2
            self.canvas.create_rectangle(
                0,
                mid_y - 35,
                self.grid_width * self.cell_size,
                mid_y + 35,
                fill="#000000",
                outline="#FF0000",
                width=2,
            )
            self.canvas.create_text(
                self.grid_width * self.cell_size // 2,
                mid_y,
                text="GAME OVER",
                font=("Arial", 28, "bold"),
                fill="#FF0000",
            )

        self.score_label.config(text=f"Score: {self.score}")
        self.level_label.config(text=f"Level: {self.level}")
        self.lines_label.config(text=f"Lines: {self.lines_cleared}")

    def show_game_over(self):
        """Display final score popup."""

        messagebox.showinfo(
            "Game Over",
            f"Final Score: {self.score}\nLines Cleared: {self.lines_cleared}\nLevel: {self.level}",
        )

    def update_game(self):
        """Main timed game loop."""

        if not self.paused and not self.game_over:
            if self.is_valid_position(
                self.piece_x, self.piece_y + 1, self.current_piece
            ):
                self.piece_y += 1
            else:
                self.lock_piece()

        self.draw_game()

        if not self.game_over:
            self.window.after(self.fall_speed, self.update_game)

    def run(self):
        """Start Tkinter event loop."""

        self.window.mainloop()


def print_welcome():
    """Print game instructions in terminal."""

    print("=" * 70)
    print("WELCOME TO TETRIS".center(70))
    print("=" * 70)
    print("Use arrow keys to move and rotate pieces.")
    print("Press SPACE for hard drop, P to pause.")
    print("Clear lines to increase score and level.")
    print("=" * 70)


if __name__ == "__main__":
    print_welcome()
    game = TetrisGame()
    game.run()
