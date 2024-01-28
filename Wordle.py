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
        correct_guess = True  # Assume the guess is correct

        # Check and color the boxes based on the match
        for col in range(min(N_COLS, len(input_word), len(chosen_word))):
            if input_word[col] == chosen_word[col]:
                window.set_square_color(window.get_current_row(), col, CORRECT_COLOR)
            else:
                correct_guess = False  # The guess is incorrect
                if input_word[col] in chosen_word:
                    window.set_square_color(window.get_current_row(), col, PRESENT_COLOR)
                else:
                    window.set_square_color(window.get_current_row(), col, MISSING_COLOR)

        if correct_guess:
            tries = window.get_current_row() + 1  # Number of tries is the current row + 1
            window.show_message("Congratulations! You guessed the word in {} trie(s).".format(tries))
            return  # Exit the function to avoid further processing

        # Move on to the next row only if it's not the last guess
        if window.get_current_row() < N_ROWS - 1:
            window.set_current_row(window.get_current_row() + 1)

        # If the last guess has been made, show the game-over message
        elif window.get_current_row() == N_ROWS - 1:
            window.show_message("Sorry, you've run out of guesses. The word was: {}".format(chosen_word))

    else:
        # Show message ofr invalid guess
        window.show_message("Invalid guess.")
 


def main():
    # Initialize WordleGWindow
    window = WordleGWindow()

    # Choose a random word from the list
    chosen_word = choose_random_word()

    # Print chosen word to the terminal
    print(f"Chosen word: {chosen_word}")

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