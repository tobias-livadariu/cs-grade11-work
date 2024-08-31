#Tobias Livadariu and Jason Galutira
#ICS3UI-23
#Instructor: Ms. Mohammed
#2023_05_19
'''The purpose of this program is to run a word guessing game. The user will guess individual letters out of a mystery unknown word. As the user guesses correctly, the guessed letters will be revealed. If the user guesses all letters correctly with less than 5 incorrect guesses, they win. Otherwise, they lose.'''

# Importing the random module
import random

# Defining the get_option() function --> This function will be used to get user input for the main menu of the program
def get_option():
  while True:
    menuChoice = input('''Main Menu:
Option 1 --> Play word game
Option 2 --> Display instructions for the word game
Option 3 --> Quit
Enter either 1, 2 or 3: ''')
    if menuChoice == "1":
      return "PLAY"
    elif menuChoice == "2":
      print("\nIn this game players try to guess all the letters of a secret word. As they guess correctly, letters are revealed in the secret word. However, players can only guess an incorrect letter 5 times. If the user guesses the secret word with less than 5 incorrect guesses, they win. Otherwise, they lose\n")
    elif menuChoice == "3":
      return "QUIT"
    else:
      print(f"\nYour input of {menuChoice} was invalid! You must enter either 1, 2 or 3.\n")

def get_word(ml):
  wordAnswer = list(random.choice(ml))
  return wordAnswer

def guess_letter(right, wrong, guessed):
  while True:
    guess = input(f"*You have {wrongGuesses} wrong guesses* - Guess a letter in this unknown word {guessed}: ")
    if len(guess) == 1 and guess.isalpha():
      if guess in right:
        print(f"Hey! You have already guessed {guess} correctly!")
      elif guess in wrong:
        print(f"Hey! You have already guessed {guess} incorrectly!")
      else:
        return guess
    else:
      print('Please enter a single alphabetic character')

def check_letter(guess, word):
  if guess in word:
    return True
  else:
    return False

def reveal_letters(word, guessed, guess):
  copyWord = word.copy()
  while guess in copyWord:
    guessed[copyWord.index(guess)] = guess
    copyWord[copyWord.index(guess)] = ' '

# Main
master_list = ["bin", "temptation", "budget", "onion", "silly", "cat", "machine","colour", "bicycle"]
while get_option() == "PLAY":
  word = get_word(master_list)
  guessed = ["*"] * len(word)
  wrongGuesses = 0
  lettersRight = []
  lettersWrong = []
  while wrongGuesses < 5:
    guess = guess_letter(lettersRight, lettersWrong, guessed)
    correct = check_letter(guess, word)
    if correct:
      lettersRight.append(guess)
      reveal_letters(word, guessed, guess)
    else:
      lettersWrong.append(guess)
      print(f"Wrong guess! Your guess of {guess} is not in the mystery word.\n")
      wrongGuesses += 1
    if word == guessed:
        print(f"Congratulations! You guessed the word {word} correctly! You had {wrongGuesses} wrong guesses")
        break
  if wrongGuesses == 5:
    print(f"You have incorrectly guessed 5 times. you have lost! the word was {word}\n")