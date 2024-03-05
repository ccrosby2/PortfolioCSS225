from Gvars import *
def pick_name():
    import random
    name = input("Choose who you want. 1. Cleo, 2. TT, 3. Stoney, 4. Frankie")
    
    
    while name not in ["1","2","3","4"]:
        print("This is not a option. Game Over")
        name = input("Choose who you want. 1. Cleo, 2. TT, 3. Stoney, 4. Frankie")
    
    if name == ("2"):
        name = "TT"
        print("Let's go to the agency and get my son so we can leave out the country.")
    elif name == "3":
        name = ("Stoney")
        print("Let go to the hood and ask one of them men to give us some money.")
    elif name == "4":
        name =("Frankie")
        print ("Let's go to the bank and get some more of the money from the cops.")
    elif name == "1":
        name = "Cleo"
        print("Let's go rob Bank Federal Downtown.")
    else:
        print("That is not a option. Please choose again.")
    for num in names:
        print (num) 
                    #names.remove("Stoney")
                    #names.remove("Frankie")
                    #names.remove("Cleo")
                    #names.remove("TT")
                    #print("Game Over")
