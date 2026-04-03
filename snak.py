from tkinter import *
from tkinter import messagebox
import random

class SnakeGame:
     def __init__(self):
          """Initialize the game window and parameters"""

          # window setup
          self.window = Tk()
          self.window.title("🐍 Snake Game 🐍")
          self.window.geometry("600x400")
          self.window.resizable(False, False)

          # grid setup
          self.grid_size = 20
          self.width = 30
          self.height = 20

          # color setup
          self.snake_color = "#00FF00"
          self.food_color = "#FF0000"
          self.bg_color = "#000000"
          self.grid_color = "#333333"

          # create canvas
          self.canvas = Canvas(
               self.window,
               width=self.width * self.grid_size,
               height=self.height * self.grid_size,
               bg=self.bg_color
          )
          self.canvas.pack()

          # create info frame for score and instructions
          self.info_frame = Frame(self.window)
          self.info_frame.pack()

          self.score_label = Label(
               self.info_frame,
               text="Score: 0",
               font=("Arial", 12, "bold"),
               fg="#FFFFFF",
               bg=self.bg_color
          )
          self.score_label.pack()

          self.instructions_label = Label(
               self.info_frame,
               text="Use arrow keys to move. Eat food to grow!",
               font=("Arial", 10),
               fg="#FFFFFF",
               bg=self.bg_color
          )
          self.instructions_label.pack()

          # Snake [x, y] positions
          self.snake = [
               [15, 10], #head
               [14, 10], #body
               [13, 10] #tail
          ]

          self.food = self.generate_food() # generate food
          self.direction = "Right" # current direction
          self.next_direction = "Right" # next direction to turn
          self.score = 0 # current score
          self.game_over = False # game over flag
          self.paused = False # paused flag
          self.speed = 100 # current speed (ms)

          # bind keys for movement and pause
          self.window.bind("<Up>", self.change_direction)
          self.window.bind("<Down>", self.change_direction)
          self.window.bind("<Left>", self.change_direction)
          self.window.bind("<Right>", self.change_direction)
          self.window.bind("<space>", self.toggle_pause)

          # start game loop
          self.update_game()

     def generate_food(self):
          """Generate food at random position not occupied by snake."""

          while True:
               x = random.randint(0, self.width - 1)
               y = random.randint(0, self.height - 1)
               if [x, y] not in self.snake: # don't spawn on snake
                    return [x, y]

     def change_direction(self, event):
          """Change direction based on key press while preventing reverse."""

          key = event.keysym # get key symbol

          # Prevent snake from reversing direction
          if key == "Up" and self.direction != "Down":
               self.next_direction = "Up"
          elif key == "Down" and self.direction != "Up":
               self.next_direction = "Down"
          elif key == "Left" and self.direction != "Right":
               self.next_direction = "Left"
          elif key == "Right" and self.direction != "Left":
               self.next_direction = "Right"

     def toggle_pause(self, event):
          """Toggle pause state."""

          self.paused = not self.paused
          status = "PAUSED" if self.paused else "RESUMED"
          self.instructions_label.config(text=f"Game {status} - Use space to toggle pause")

     def move_snake(self):
          """Move snake in current direction."""

          self.direction = self.next_direction # update direction to next direction
          head_x, head_y = self.snake[0] # get head position

          # calculate new head position based on direction
          if self.direction == "Up":
               head_y -= 1
          elif self.direction == "Down":
               head_y += 1
          elif self.direction == "Left":
               head_x -= 1
          elif self.direction == "Right":
               head_x += 1

          # add new head position to snake
          new_head = [head_x, head_y]
          self.snake.insert(0, new_head) # add new head to snake

          if new_head == self.food: # check if food is eaten
               self.score += 10
               self.food = self.generate_food() # generate new food

               if self.speed > 50: # increase speed as score increases
                    self.speed -= 2
          else:
               self.snake.pop() # remove tail if no food eaten

     def check_collisions(self):
          """Check for collisions with walls or self."""

          head_x, head_y = self.snake[0]

          # hit wall?
          if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
               return True

          # hit self?
          if [head_x, head_y] in self.snake[1:]:
               return True

          return False

     def draw_game(self):
          """Draw the game on canvas."""

          self.canvas.delete("all") # clear canvas

          # draw grid
          for x in range(self.width):
               for y in range(self.height):
                    px = x * self.grid_size
                    py = y * self.grid_size
                    self.canvas.create_rectangle(
                         px, py,
                         px + self.grid_size,
                         py + self.grid_size,
                         fill=self.bg_color,
                         outline=self.grid_color
                    )

          # draw snake
          for segment in self.snake:
               x, y = segment
               px = x * self.grid_size
               py = y * self.grid_size
               self.canvas.create_rectangle(
                    px, py,
                    px + self.grid_size,
                    py + self.grid_size,
                    fill=self.snake_color,
                    outline=self.snake_color
               )

          # draw food
          food_x, food_y = self.food
          px = food_x * self.grid_size
          py = food_y * self.grid_size
          self.canvas.create_rectangle(
               px + 1, py + 1,
               px + self.grid_size - 1,
               py + self.grid_size - 1,
               fill=self.food_color,
               outline=self.food_color
          )

          # update score
          self.score_label.config(text=f"Score: {self.score}")

     def show_game_over(self):
          """Display game over message."""

          messagebox.showinfo(
               "Game Over! 💀",
               f"Final Score: {self.score}\n\nWould you like to play again?"
          )
          self.window.destroy() # close game window

     def update_game(self):
          """Main game loop - runs repeatedly until game over."""

          if not self.paused and not self.game_over:
               self.move_snake() # move snake

               # check for collisions
               if self.check_collisions():
                    self.game_over = True
                    self.show_game_over() # show game over message
                    return

               self.draw_game() # redraw game

          # keep ticking even when paused so resume is instant
          if not self.game_over:
               self.window.after(self.speed, self.update_game)

     def run(self):
          """Start the game."""

          self.window.mainloop() # start Tkinter event loop

def print_welcome():
    """Print game instructions to terminal"""
    print("=" * 70)
    print("🐍 WELCOME TO SNAKE GAME! 🐍".center(70))
    print("=" * 70)
    print()
    print("📋 GAME DESCRIPTION:")
    print("   A classic Snake game where you eat food to grow longer.")
    print("   The more food you eat, the longer your snake becomes!")
    print("   Avoid hitting walls and your own body to survive.")
    print()
    print("🎯 HOW TO PLAY:")
    print("   1. Use ARROW KEYS to control the snake direction")
    print("      ↑ UP    - Move snake up")
    print("      ↓ DOWN  - Move snake down")
    print("      ← LEFT  - Move snake left")
    print("      → RIGHT - Move snake right")
    print()
    print("   2. Eat the RED food to grow and increase score")
    print("   3. Each food eaten: +10 points")
    print("   4. Press SPACE to pause/resume the game")
    print()
    print("⚠️  GAME OVER CONDITIONS:")
    print("   ✗ Snake hits the wall (boundary)")
    print("   ✗ Snake hits itself (body)")
    print()
    print("🎮 GAME MECHANICS:")
    print("   • Snake: GREEN rectangles")
    print("   • Food: RED rectangle")
    print("   • Game speed increases as you eat more food")
    print("   • Head is always at the front of the snake")
    print()
    print("💡 TIPS:")
    print("   • Plan ahead - the snake can't reverse")
    print("   • Keep your snake away from walls")
    print("   • Create space so you don't trap yourself")
    print("   • The game gets faster as you progress!")
    print()
    print("=" * 70)
    print()

if __name__ == "__main__":
     print_welcome() # print instructions to terminal
     game = SnakeGame() # create game instance
     game.run() # start the game 