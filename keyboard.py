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
BUTTON_COLOR = (50, 150, 50)
BUTTON_HOVER_COLOR = (70, 170, 70)

# Create letter rectangles and control buttons
letter_rects = {}
collected_letters = ""
saved_strings = []
rect_width = 50
rect_height = 50
letters_per_row = 13
margin = 10

# Define special buttons
space_button = Rect(200, 450, 100, 50)
backspace_button = Rect(350, 450, 150, 50)
enter_button = Rect(550, 450, 100, 50)

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
    
    # Draw the special function buttons
    # Space button
    screen.draw.filled_rect(space_button, BUTTON_COLOR)
    screen.draw.text("SPACE", center=space_button.center, fontsize=24, color=TEXT_COLOR)
    
    # Backspace button
    screen.draw.filled_rect(backspace_button, BUTTON_COLOR)
    screen.draw.text("BACKSPACE", center=backspace_button.center, fontsize=24, color=TEXT_COLOR)
    
    # Enter button
    screen.draw.filled_rect(enter_button, BUTTON_COLOR)
    screen.draw.text("ENTER", center=enter_button.center, fontsize=24, color=TEXT_COLOR)
    
    # Draw collected letters at the bottom of the screen
    screen.draw.text(
        f"Current string: {collected_letters}",
        midtop=(WIDTH // 2, HEIGHT - 80),
        fontsize=30,
        color=TEXT_COLOR
    )
    
    # Draw saved strings
    if saved_strings:
        saved_text = "Saved strings: " + ", ".join(saved_strings)
        screen.draw.text(
            saved_text,
            midtop=(WIDTH // 2, HEIGHT - 40),
            fontsize=20,
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
    global collected_letters, saved_strings
    
    # Check if any letter rectangle was clicked
    for letter, rect in letter_rects.items():
        if rect.collidepoint(pos):
            collected_letters += letter
            return
    
    # Check if space button was clicked
    if space_button.collidepoint(pos):
        collected_letters += " "
    
    # Check if backspace button was clicked
    elif backspace_button.collidepoint(pos):
        if collected_letters:  # Only if the string is not empty
            collected_letters = collected_letters[:-1]
    
    # Check if enter button was clicked
    elif enter_button.collidepoint(pos):
        if collected_letters:  # Only save non-empty strings
            saved_strings.append(collected_letters)
            collected_letters = ""  # Clear the current string

# Set up the letters when the program starts
setup_letters()

# Run the game
pgzrun.go()
