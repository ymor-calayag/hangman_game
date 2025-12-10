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

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
lives = 6

for letter in range(0, len(chosen_word)):
    placeholder.append("_")

while True:
    guess = input("Guess a letter: ").lower()

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
    print(chosen_word)


# TODO-2:
# If guess is not a letter in the chosen_word, Then reduce lives by 1.
# If lives goes down to 0 then the game should end, and it should print "You lose."
# TODO-3:
# print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.