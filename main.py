import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "whale", "capybara"]

chosen_word = random.choice(word_list)

placeholder = []
lives = 6

for letter in range(0, len(chosen_word)):
    placeholder.append("_")

print("".join(placeholder))

while True:
    guess = input("\nGuess a letter: ").lower()

    if "".join(placeholder) == chosen_word:
        print("==========")
        print("You Won!")
        print("==========")
        break 

    if lives == 0:
        print(stages[0])
        print("==========")
        print("You Lose!")
        print("==========")
        break

    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            placeholder[index] = letter
            
    print("".join(placeholder))
