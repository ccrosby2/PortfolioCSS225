#Cierra Crosby
#Instructor Nathan Braun
#2/23/2024
#Module 6 Team Project
#This program generates a dice throwing game that a user will receive feedback based on the correct number guess.
print ("This is a dice guessing game throwing the dice to get feedback. If you guess the correct number you win the game.")
import random

iceThrow = random.randrange(1,11)
user = 0

while user != iceThrow:
  user = int(input("Enter a number between 1 and 10"))
  if user == iceThrow:
    print("Well done you guessed it")
  elif user > iceThrow:
    print("This number is too large")
    print ("Please guess again.")
  elif user < iceThrow:
    print("This number is too small")
    print("Please guess again.")


