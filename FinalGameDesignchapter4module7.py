import random

option = (1,12)
int = random.randrange(1,12)
burger="burger"
fries="fries"
drink = "drink"
hotdog = "hotdog"
salad= "salad" 
large_drink = "large_drink"
crab = "crab"
spaghetti = "spaghetti"
soup_chicken = "soupw/chicken"
small_drink = "small drink"
Luguine="luguine pasta desert" 
hungry = ("burger")or("hotdog")or("crab")or("spaghetti")or("soup_chicken")
option= input("Choose dinner:")
print(input)

num_attempts = 9
if num_attempts > 9:
    print ("Please order something to eat.")
print("Banker responses")
if option == hungry:
    print("Bank manager says:   I am a vegan")
elif option == Luguine:
    print("This restaurant is pretty good.")
    print("You can move to chapter five")
elif option == hungry:
    print("This is not a option")
else:
    print("Game Over.")    


