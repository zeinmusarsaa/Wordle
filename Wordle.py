# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


#The following code pulls a random word from the WordleDictionary doc and formats it in the boxes
def choose_random_word():
    return random.choice(FIVE_LETTER_WORDS)

def display_word_in_row(word, row, window):
    for col in range(N_COLS):
        window.set_square_letter(row, col, word[col].upper())

def main():
    # Initialize WordleGWindow
    window = WordleGWindow()

    # Choose a random word from the list
    chosen_word = choose_random_word()

    # Display the chosen word in the first row of the window
    display_word_in_row(chosen_word, 0, window)

    # Keep the window open until the user closes it
    window.mainloop()

if __name__ == "__main__":
    main()



"""
def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

 Startup code

if __name__ == "__main__":
    wordle()
"""

