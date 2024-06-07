# day31_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------- 

# Flash Card App
This Flash Card App is designed to help you learn French vocabulary effectively using a simple and interactive interface. The app displays a French word, gives you a few seconds to think of the English translation, and then flips the card to reveal the correct answer. You can mark words as known to track your progress.

## Features
- __Random Word Selection:__ Each session presents a random French word from the list.
- __Timer-Based Flip:__ The card flips automatically after 3 seconds to reveal the English translation.
- __Persistent Progress:__ Known words are removed from the list, and progress is saved between sessions.
- __Interactive Buttons:__ Mark words as known or skip to the next word using intuitive buttons.
- 
## How It Works

1. __Data Loading:__
The app tries to load your progress from words_to_learn.csv.
If no progress file is found, it loads the initial set of words from french_words.csv.

2. __Displaying Cards:__
The app displays a French word and sets a timer to flip the card after 3 seconds.

4. __Flipping Cards:__
After the timer expires, the card flips to show the English translation.

4. __Tracking Progress:__
When you mark a word as known, it is removed from the list of words to learn and saved to words_to_learn.csv.

Lessons Learned
- Exception Handling:
  - Use try-except blocks to handle file not found errors gracefully.
  - Example: Trying to load a CSV file and handling the case where the file is not found.
  - 
- Random Selection:
  - Use the random.choice method to select a random item from a list.
    
- UI Management with Tkinter:
  - Create and configure UI elements like windows, buttons, and canvases using Tkinter.
  - Use window.after to schedule tasks (e.g., flipping the card after a delay).
    
- Data Persistence with Pandas:
  - Read and write CSV files using pandas to persist data between sessions.
  - Convert data between DataFrames and dictionaries for easy manipulation.


