import random

option = (1,5)
user = random.randrange(1,5)
Cleopatria_Lenchrich = "0"
Patrick_Owens ="2"
Cameron_lens ="3"
Max_House ="4"
Lida_Williams="5"
user = int(input("Guess a number between 1 and 5"))
if user == 6:
    print("This is not a option. Game over")   
elif 0 < user and user < 6:
    print ("Lets conduct a investigation")
else:
    print ("This is not a option. Please leave the investigation room.")
user = -1
Cleopatria_Lenchrich = 0
Patrick_Owens =2
Cameron_lens =3
Max_House =4
Lida_Williams=5
num_guesses =0

while user != 0 and num_guesses < 3:
  user = int(input("Enter a number 0-5"))
  num_guesses +=1
  if user == 1:
    print("You guessed a wrong number. Game Over.")
  elif user == 2:
    print("This is not the person who killed Luther!")
    print ("Please guess again.")
  elif user == 3:
    print("This not a girl")
    print("Please guess again.")
  elif user == 4 or user == 5:
    print("These might be the girls that killed Luther.")
  elif user == 0:
    print("This is the person that Killed Luther.Do you know if this the person?")
  else:
    print("This is not a option. Please guess again.")
if num_guesses==3:
    print("You ran out of tries. Game over")
else:
    print("Lets go to chapter 3.")
