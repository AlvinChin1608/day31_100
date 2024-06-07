from tkinter import *
import pandas
import random

# Setting background color for the app
BACKGROUND_COLOR = "#B1DDC6"

# Initialize global variables to keep track of the current card and the list of words to learn
current_card = {}
to_learn = {}

# Try to load the list of words to learn from a CSV file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
# If the file is not found, load the original dataset of French words
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
# If the file is found, convert it to a dictionary of records
else:
    to_learn = data.to_dict(orient="records")

# Function to display the next card
def next_card():
    global current_card, flip_timer
    # Cancel the previous flip timer
    window.after_cancel(flip_timer)
    # Choose a random word from the list of words to learn
    current_card = random.choice(to_learn)
    # Update the card to show the French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)

# Function to flip the card and show the English translation
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

# Function to mark a word as known
def is_known():
    # Remove the current word from the list of words to learn
    to_learn.remove(current_card)
    # Convert the updated list back to a DataFrame and save it to a CSV file
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) # Pandas automatically adds an index, but we don't want that
    # Show the next card
    next_card()

# UI setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create a canvas to hold the flashcard images and text
canvas = Canvas(width=800, height=530)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 265, image=card_front)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

# Configure the canvas background and border
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons for marking a word as unknown or known
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# Show the first card
next_card()

# Start the Tkinter event loop
window.mainloop()
