# File: Wordle.py

# File: Wordle.py

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def choose_random_word():
    return random.choice(FIVE_LETTER_WORDS)

def display_word_in_row(word, row, window):
    pass
    #for col in range(N_COLS):
        #window.set_square_letter(row, col, word[col].upper())

def enter_action(input_word, chosen_word, window):
    input_word = input_word.strip().lower()

    if input_word in FIVE_LETTER_WORDS:
        # Check and color the boxes based on the match
        for col in range(min(N_COLS, len(input_word), len(chosen_word))):
            if input_word[col] == chosen_word[col]:
                window.set_square_color(window.get_current_row(), col, CORRECT_COLOR)
            elif input_word[col] in chosen_word:
                window.set_square_color(window.get_current_row(), col, PRESENT_COLOR)
            else:
                window.set_square_color(window.get_current_row(), col, MISSING_COLOR)

        # Move on to the next row
        window.set_current_row(window.get_current_row() + 1)

        # Check if the user has correctly guessed all five letters
        if window.get_current_row() == N_ROWS:
            tries = window.get_current_row() - 1  # Number of tries is the current row minus 1
            window.show_message("Congratulations! You guessed the word in {} tries.".format(tries))
            
            # Close the window
            window._root.destroy()
        else:
            window.show_message(" ")
    else:
        window.show_message("Not in word list.")

        # Check if the user has run out of guesses
        if window.get_current_row() == N_ROWS:
            window.show_message("Sorry, you've run out of guesses. The word was: {}".format(chosen_word))
            
            # Close the window
            window._root.destroy()
            # Optionally, you may want to include additional actions here.


def main():
    # Initialize WordleGWindow
    window = WordleGWindow()

    # Choose a random word from the list
    chosen_word = choose_random_word()

    # Display the chosen word in the first row of the window
    display_word_in_row(chosen_word, 0, window)

    def enter_action_wrapper(input_word):
        enter_action(input_word, chosen_word, window)

    window.add_enter_listener(enter_action_wrapper)

    # Start the main event loop
    #window.mainloop()
    window._root.mainloop()  # Use the root instance for mainloop


if __name__ == "__main__":
    main()