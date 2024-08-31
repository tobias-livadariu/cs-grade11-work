#Tobias Livadariu
#ISC3U1-23
#Instructor: Ms. Mohammed
#2023_04_13
#Dice Game
'''The purpose of this program is to allow the user to wager a certain amount on a pair of dice rolls. If the sum of the user's rolls is higher than the sum of the computer's rolls, they win the wager. Otherwise, they lose the wager. The program checks for invalid inputs and also allows the user to choose if they want to roll again with the same wager in the case of ties.'''

'''In the block below I am importing the random module which is needed for simulating dice rolls.
I am also literally defining variables to hold the user's starting points amount, if the user wants to keep play the game (the user can change this value when they hit 0 points) and if the user is rolling again after a draw (the user can change this value when a draw is achieved).'''
import random
gameRunning = "Y"
rollAgain = False
userPoints = 500

'''In the print statement below, I am introducing the title of the game to the user. Note that I formatted this title using the format() function. I also changed the end parameter of the print statement to print an extra blank line at the end of the string, I do this a lot throughout the program to make it easier for the user to use.'''
print(format("DICE GAME", "^36"), end = "\n\n")

# This while loop holds the body of my program.
# The purpose of the while loop is to keep the program running until the user's points reach zero and the user decides to stop playing. The while loop does this by checking if the gameRunning variable still holds the value 'Y' before it iterates.
while gameRunning == "Y":
  # If the user is rolling again after a tie with the computer, the program must skip reassigning the value of the wager variable and checking if it is valid. This is done through the if statement below, which only allows the section of the while loop which reassigns the wager value to run if the user is not rolling again after a tie.
  if rollAgain == False:
    print(f"You have {userPoints} points to wager.")
    # In the try and except statement below, the user's wager is inputted and the program tries to convert it into an integer value. If an exception arises, that means the user inputted a non-integer value and the program warns the user that they can't do this before returning to the beginning of the while loop with a continue statement.
    try:
      wager = int(input("Enter points to wager (-1 to QUIT): "))
      print()
    except:
      print("\nYou must input a positive integer wager!", end = "\n\n")
      continue
    # If the user inputted -1 as their wager, meaning that they want to quit the program, the code within the if statement below will run and the break keyword within will end the while loop.
    if wager == -1:
      break
    # If the user's wager was an integer below one point, this elif block will run and warn the user that their wager must be at least one point or higher before skipping to the next iteration of the while loop with the continue keyword. It is important to note that an input of -1 will not cause this elif block to run since the if block above would have ran.
    elif wager <= 0:
      print("You must wager atleast one (1) point!", end = "\n\n")
      continue
    # This elif block checks if the user's wager was above their total points. If it was, the block runs and warns the user that their wager must be less than or equal to their points as well as continuing to the next iteration of the while loop.
    elif wager > userPoints:
      print(f"Please enter a wager less than or equal to {userPoints}!", end = "\n\n")
      continue
  # The block of variable definitions below calculates the user's two dice rolls as well as the computer's two dice rolls using the random.randrange() function, and stores them in variables.
  userRoll1 = random.randrange(1, 7)
  userRoll2 = random.randrange(1, 7)
  computerRoll1 = random.randrange(1, 7)
  computerRoll2 = random.randrange(1, 7)
  # The print statements below print out the user's rolls as well as the computer's rolls to the user.
  print(f"You rolled a [{userRoll1}][{userRoll2}]")
  print(f"Computer rolled a [{computerRoll1}][{computerRoll2}]", end = "\n\n")
  # The if statement below checks if the total of the user's rolls equals the total of the computer's rolls. If this is true, it means a tie has occurred, and the user is informed of this with a print statement. The user is also asked if they want to try again and their response to this question is recorded in the tryAgain variable.
  if (userRoll1 + userRoll2) == (computerRoll1 + computerRoll2):
    print("It's a tie!")
    tryAgain = input("Enter 'R' to roll again: ")
    print()
    # The nested if statement below checks if the user inputted 'R' or 'r' when prompted if they wanted to try again. If they did, the value of the rollAgain variable is set as True. This causes the wager variable to not be reassigned.
    if tryAgain.casefold() == "r":
      rollAgain = True
    # If the user did not input 'R' or 'r' when prompted if they want to try again, the value of the rollAgain variable is set to false since the user is not rolling again.
    else:
      rollAgain = False
  # The elif statement below checks if the total of the user's rolls is greater than the total of the computer's rolls. If this is true, it means the user won the wager, and the user is informed of this with a print statement. Also, if the user won, their total number of points is incremented by the amount of their wager, and the value in the rollAgain variable is set to False since a draw was not achieved in this iteration of the while loop.
  elif (userRoll1 + userRoll2) > (computerRoll1 + computerRoll2):
    print(f"You win {wager} points!", end = "\n\n")
    userPoints += wager
    rollAgain = False
  # If this else block is reached, it means the total of the user's rolls were lower than the total of the computer's rolls, so the user lost. The user is informed of their loss with a print statement, and their total number of points is decremented by their wager. Also, the value in the rollAgain variable is set to False since a draw was not achieved in this iteration of the while loop.
  else:
    print(f"You lose {wager} points!", end = "\n\n")
    userPoints -= wager
    rollAgain = False
    # This nested if statement checks if the user's total points equal zero after having been decremented by their lost wager. If this is true, it means the game is over. The user is informed of this with a print statement and also asked if they want to play again. If they input Y or y, the game restarts with their total points being reset to 500. If they input N or n, the overall while loop containing the body of the program ends. Note that a smaller nested while loop has been used here to force the user into giving valid input.
    if userPoints == 0:
      print("GAME OVER! You have zero points left!", end = "\n\n")
      gameRunning = input("Would you like to play again (Y or N)? ")
      while gameRunning.casefold() != "y" and gameRunning.casefold() != "n":
        print("\nYou must input either Y or N.")
        gameRunning = input("Would you like to play again (Y or N)? ")
      if gameRunning == "Y":
        userPoints = 500
        print()

print("Thank you for playing! Goodbye!")