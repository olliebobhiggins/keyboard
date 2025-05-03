import string
import pgzrun
from pygame import Rect

# Set up the window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
BACKGROUND_COLOR = (0, 0, 0)
RECTANGLE_COLOR = (100, 100, 255)
TEXT_COLOR = (255, 255, 255)

# Create letter rectangles
letter_rects = {}
collected_letters = ""
rect_width = 50
rect_height = 50
letters_per_row = 13
margin = 10

# Position the letter rectangles in rows
def setup_letters():
    global letter_rects
    letter_rects = {}
    
    # Calculate starting position for centering
    total_width = letters_per_row * (rect_width + margin) - margin
    start_x = (WIDTH - total_width) / 2
    start_y = 100
    
    for i, letter in enumerate(string.ascii_lowercase):
        row = i // letters_per_row
        col = i % letters_per_row
        x = start_x + col * (rect_width + margin)
        y = start_y + row * (rect_height + margin)
        letter_rects[letter] = Rect((x, y), (rect_width, rect_height))

def draw():
    # Fill the screen with black
    screen.fill(BACKGROUND_COLOR)
    
    # Draw letter rectangles
    for letter, rect in letter_rects.items():
        screen.draw.filled_rect(rect, RECTANGLE_COLOR)
        screen.draw.text(letter, center=rect.center, fontsize=30, color=TEXT_COLOR)
    
    # Draw collected letters at the bottom of the screen
    screen.draw.text(
        f"Collected letters: {collected_letters}",
        midtop=(WIDTH // 2, HEIGHT - 80),
        fontsize=30,
        color=TEXT_COLOR
    )
    
    # Draw instructions
    screen.draw.text(
        "Click on letters to collect them",
        midtop=(WIDTH // 2, 30),
        fontsize=24,
        color=TEXT_COLOR
    )

def on_mouse_down(pos):
    global collected_letters
    
    # Check if any letter rectangle was clicked
    for letter, rect in letter_rects.items():
        if rect.collidepoint(pos):
            collected_letters += letter
            break

# Set up the letters when the program starts
setup_letters()

# Run the game
pgzrun.go()