#from Gvars import*
import random
import turtle

num = input("Choose who you want. 1. Cleo, 2. Stoney, 3. TT, 4. Frankie")
#name = ["Frankie", "Stoney", "TT","Cleo"]

while num not in ["1","2","3","4"]:
    print("This is not a option. Game Over")
    name = input("Choose who you want. 1. Cleo, 2. TT, 3. Stoney, 4. Frankie")

if num == ("2"):
    name = "TT"
elif num == "3":
    name = ("Stoney")
elif num == "4":
    name =("Frankie")
elif num == "1":
    name = "Cleo"
else:
    print("That is not a option. Please choose again.")
print (name)
alex = turtle.Turtle()
wn = turtle.Screen()
	
#wn.exitonclick()
jim=turtle.Turtle()


# draw head
jim.color("black")
jim.circle(45)

# draw body
jim.right(90)
jim.forward(90)
#jim.penup()

#draw legs
jim.right(45)
jim.forward(60)
jim.penup()
jim.setpos(0,-90)
jim.pendown()
jim.left(90)
jim.forward(60)

#draw arms
jim.penup()
jim.setpos(0,-45)
jim.left(180)
jim.pendown()
jim.forward(45)
jim.penup()
jim.setpos(0,-45)
jim.right(90)
jim.pendown()
jim.forward(45)
    
#main()
                    #names.remove("Stoney")
                    #names.remove("Frankie")
                    #names.remove("Cleo")
                    #names.remove("TT")
                    #print("Game Over")
                    


                    
