#Number Guessing Game
import random
print("Hi, welcome to the number guessing game!")
print("pick a number between 1 and 50!)

guess_taken = 0
computer_guess = random.randint(1, 50) #Random integer from 1-50
print("is it " number"? yes, higher, or lower")
guess_taken += 1

#Input Higher or Lower or Yes
decision=input()
      
#Game Logic
while decision =! "yes"
      if decision = "lower"
        new_computer_guess = random.randint(0, computer_guess)
        print("is it " new_computer_guess "? yes, lower, or higher")
        guess_taken += 1
      else if decision = "higher"
        new_computer_guess = random.randint(computer_guess, 50)
        print("is it "new_computer_guess "? yes, no or higher")
        guess_taken += 1
if decision = "yes"
      print(I guessed it with "guess_taken " tries!")
