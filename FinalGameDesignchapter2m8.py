from Gvars import *
import chapter1m8
from Gvars import inventory
chapter1m8.pick_name()

from Gvars import name
print (name)

#from Gvars import inventory

#arrested_heisters.append(name)

option = ("Choose a person")
args = "inventory", "jumpsuit", "masks", "outfits", "agency", "mall"
num = "Cleo", "Stoney", "TT", "Frankie"

outfit = input("1. jumpsuits, 2. masks, 3. outfits, 4. agency, 0.mall,5. inventory")
#jumpsuits= "0"
#masks = "1"
#outfits = "2"
#agency= "3"
#mall = "4"
#inventory="5"

while outfit not in ["1","3","4","0","5"]:
    print("This is not a option. Game Over")
if option == "0":
    print ("Cleo says" ,"I want to get some jumpsuits, mask, and guns to rob the bank downtown")
elif option== "1":
    print ("Stoney says","I want to get the outfits")
elif option == "3":
    print("TT says","I want to get my son from the agency before we leave.")
elif option =="5":
    if name == "Cleo":
        print ("Stoney,TT,and Frankie can get us a new ride")
    else:
        print("You have made the wrong choice.")
for num in names:
    print (num)

option_inventory=input("What option you want to take")
Cleo = "0"
Stoney = "1"
Frankie = "2"
TT = "3"

if option_inventory == "2":
    print ("I want to get some jumpsuits, mask, and guns to rob the bank downtown")

elif option_inventory == "1":
    print ("I want to get the outfits")

elif option_inventory == "0":
	print("This is not a option. Game over")

elif option_inventory == "3":
    print("I want to get my son from the agency before we leave.")

elif type(option)== int:
    print("This is not a option. Try again")

class person:
    def __init__ (self, inventory,jumpsuit, outfits, masks, agency,mall):
        self.inventory = inventory
        self.jumpsuit = jumpsuit
        self.masks= masks
        self.outfits = outfits
        self.agency =  agency
        self.mall = mall
    
    def get_inventory(self): 
        self.Cleo = print ("I want to get some jumpsuits, mask, and guns to rob the bank downtown")
        self.Frankie= print ("I want to get the outfits")
        self.TT= print("I want to get my son from the agency before we leave.")
        self.Stoney= ("I want to get the shoes from the mall.")
    def get_masks(self):
        print ("We do need this but I need a new car,Im not going to that Agency")
        return
    def get_jumpsuit(self):
        print ("I already got the jumpsuits. We need money.")
        return
    def get_outfits(self):
        print("We need more.")
        return
    def get_agency(self):
        print("TT! They not giving you your child unless you go rob Bank Federal Downtown.")
        return
            
    def get_anti_keytype():
        while running:
            pyautogui.press(key_2[randint(0,2)])
            print("This is not a option.")
            return
    def fullperson(self):
        return self.inventory + ' ' + str(self.jumpsuit) + ' ' + self.masks + ' ' + self.agency + ' ' + self.mall
    
person1 = person("Smith and Wesson 669","blue jumpsuits", "we need a outfit","seethru masks", "We not going to the Agency to get your son","We can not go to a mall.We going to be seen.")
person2 = person("I dont want to kill nobody", "pink jumpsuits","we need a outfit", "skull masks", "I want to get my son", "I like malls")
person3 = person("I got a Smith and Wesson 4505", "black jumpsuits","we need a outfit", "wigs like masks", "Your son gone be ok unitl after we rob this bank","the mall better than blue/pink jumpsuits.")
person4 = person("I got a friend but no weapon", "no jumpsuit","we need a outfit","diamond masks","I want to go get your son though TT","the mall too open for us right now,")

print(person1.get_inventory())
print(person1.get_jumpsuit())
print(person1.get_masks())
print(person2.get_jumpsuit()) 
print(person2.get_masks())
print(person3.get_inventory())
print(person3.get_jumpsuit())
print(person3.get_masks())

print(person4)
print(person1.fullperson())
print(person2.fullperson())
print(person3.fullperson())
print(person4.fullperson())

num= ["cleo", "stoney", "tt", "frankie"]
jumpsuits= "0"
masks = "1"
outfits = "2"
agency= "3"
mall = "4"
inventory="5"
num2 = "6"

option= input("1. jumpsuits, 2. masks, 3. outfits, 4. agency, 0.mall,5. inventory,6.num, 7. get_inventory")
jumpsuits= "0"
masks = "1"
outfits = "2"
agency= "3"
mall = "4"
inventory="5"
num = "6"
get_inventory="7"

if option == num:
 print ("Cleo is getting us ready for our next heist")
elif option!= num2:
 print ("Game over")
elif option== "7":
 args [input(get_inventory)]
 print("This is what the next heist clothes.")
