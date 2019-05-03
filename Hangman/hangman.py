from random import choice
from string import ascii_lowercase

FILENAME = 'Hangman\\sowpods.txt'


def get_rand_word(filename):
    with open(filename, 'r') as f:
        return choice([x.strip() for x in f]).lower()


def print_game(wrong, word, letters):
    # Print wrong guesses
    print('\nWrong guess:', end=' ')
    for i in range(len(wrong)):
        if i != 0:
            print(',', end=' ')
        print(wrong[i], end='')
    print()
    # Print letters
    for i in letters:
        if i is None:
            print(' ', end=' ')
        else:
            print(i, end=' ')
    print()
    # Print dashes
    for i in word:
        if i != ' ':
            print('-', end=' ')
        else:
            print(' ', end=' ')
    print()


def get_letter(attempt, guess):
    user_input = input(f'> Guess a letter ({attempt} attempts left): ').lower()
    # Make sure if the user input is a letter and not in the guess list
    if len(user_input) != 1 or user_input not in ascii_lowercase:
        print(f"> Please input a letter!")
    elif user_input in guess:
        print(f"> You have guessed '{user_input}' before")
    else:
        return user_input


def play(word):
    attempt = 6
    guess, guess_wrong = [], []
    letters = []
    for i in word:
        # Assign None to letters if i is not a space otherwise assign space
        # instead
        i = None if i != ' ' else i
        letters.append(i)
    while attempt > 0:
        print_game(guess_wrong, word, letters)
        if None not in letters:
            print('> You win!')
            break
        user_letter = get_letter(attempt, guess)
        # Make sure get_letter is returning the user input
        if user_letter is not None:
            # Search trough the word and assign user_letter to letters[i] if
            # the user_letter match a character in word[i]
            for i in range(len(word)):
                if user_letter == word[i]:
                    letters[i] = user_letter
            guess.append(user_letter)
            if user_letter not in letters:
                guess_wrong.append(user_letter)
                attempt -= 1
    else:
        print_game(guess_wrong, word, letters)
        print('> You lose...')
        print(f'> Answer: {word.capitalize()}')


if __name__ == "__main__":
    word = get_rand_word(FILENAME)
    play(word)
