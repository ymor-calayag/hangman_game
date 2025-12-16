# Hangman Game

This command-line game selects a random word from a predefined list and lets the player guess letters. The player has six lives, and each incorrect guess reduces a life. The game visually represents the hangman’s state as lives are lost, and ends when the player either guesses the word or runs out of lives.

**Technologies Used**

+ ```Python```
+ Modularized code with separate files for words and ASCII art
+ ```random``` module for word selection
+ Lists and string manipulation

**Features**

+ Random word selection from an extensive word list
+ Visual hangman stages showing the player’s progress
+ Tracks guessed letters and prevents repeated guesses
+ User-friendly command-line interface with clear prompts
+ Win/lose messages with final word reveal on loss

**What Users Can Do**

+ Guess letters one by one
+ See the current state of the word with placeholders for unguessed letters
+ Watch the hangman visual update with each wrong guess
+ Win by guessing all letters before losing all lives
+ Replay by restarting the program

**The Process / How It’s Built**

+ The game loads a list of challenging words from a separate module.
+ It randomly selects a word and creates a placeholder list of underscores matching the word’s length.
+ The player inputs guesses, which update the placeholder if correct, or decrease lives if wrong.
+ The program uses a list of hangman ASCII art stages to visually represent the player’s remaining lives.
+ The game loops until the player guesses all letters or runs out of lives, displaying appropriate messages.

