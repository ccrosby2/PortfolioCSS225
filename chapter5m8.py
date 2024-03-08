
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
def draw_(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
alex.color("black")
for i in range(5):
	draw_(alex,40*i+0)
	alex.penup()
	alex.backward(20)
	alex.right(90)
	alex.forward(20)
	alex.left(90)
	alex.pendown()
	
#wn.exitonclick()
jim=turtle.Turtle()
jim.setpos(0, -20)
   
jim.left(90)
    
    # draw body
jim.color("black")
jim.forward(60)
    
    # draw head
jim.color("black")
jim.forward(90)
jim.circle(45)
    
    # move to position
jim.penup()
jim.setpos(20, -20) #Sets the position of the turtle
jim.left(90)
jim.pendown()
    
#main()
                    #names.remove("Stoney")
                    #names.remove("Frankie")
                    #names.remove("Cleo")
                    #names.remove("TT")
                    #print("Game Over")
                    
