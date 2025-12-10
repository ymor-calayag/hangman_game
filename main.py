import random
import hangman_words
import hangman_art

stages = hangman_art.stages

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

placeholder = []
lives = 6

for letter in range(0, len(chosen_word)):
    placeholder.append("_")

print(hangman_art.logo)
print(f"\n{''.join(placeholder)}")

while True:
    if "_" not in placeholder:
        print("==========")
        print("You Won!")
        print("==========")
        break 

    if lives == 0:
        print(stages[0])
        print("==========")
        print("You Lose!")
        print(f"The word is {chosen_word}")
        print("==========")
        break

    guess = input("\nGuess a letter: ").lower()
    

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, it's not in the word. You lose a life")
    
    if guess in placeholder:
        print(f"You've already guessed {guess}")

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            placeholder[index] = letter
            
    print("".join(placeholder))
    print(f"++++++++++ {lives}/6 LIVES ++++++++++")
