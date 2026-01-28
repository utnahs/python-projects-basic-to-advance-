import random

HANGMANPICS = [
r'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''',
r'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''',
r'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''',
r'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',
r'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',
r'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',
r'''
 +---+
 |   |
     |
     |
     |
     |
=========
'''
]

WORDS = ['hello', 'world', 'funny', 'trip', 'elephant']


def choose_word(words):
    return random.choice(words)


def display_word(chosen_word, correct_letters):
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    return display


def play_game():
    chosen_word = choose_word(WORDS)
    lives = 6
    correct_letters = []
    game_over = False

    print("_" * len(chosen_word))

    while not game_over:
        guess = input("Enter a letter: ").lower()

        if guess in correct_letters:
            print("You already guessed that.")
            continue

        if guess in chosen_word:
            correct_letters.append(guess)
        else:
            lives -= 1

        display = display_word(chosen_word, correct_letters)
        print(display)
        print(HANGMANPICS[lives])

        if "_" not in display:
            print("You win")
            game_over = True

        if lives == 0:
            print("You lose")
            print(f"The word was: {chosen_word}")
            game_over = True


play_game()
