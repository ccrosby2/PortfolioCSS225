#from Gvars import*
import turtle

names=["TT", "Cleo","Stoney","Frankie"]
name = input("Choose who you want. Cleo, Stoney, TT, Frankie")

while name not in names:
    print("This is not a option. Game Over")
    name = input("Choose who you want. Cleo, TT, Stoney, Frankie")
    
if name == "Cleo":
    print (name + " is running to the car")
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
    
    
    jim.penup()
    jim.setpos(-50,-35)
    jim.pendown()
    jim.left(135)
    jim.forward(90)
    jim.left(135)
    jim.forward(45)
    jim.penup()
    jim.back(45)
    jim.left(90)
    jim.pendown()
    jim.forward(45)
    print("TT died")
    print("Frankie gets shot by police")
    print("Stoney gets on a bus to Mexico")
    
if name == "TT" or name == "Stoney" or name == "Frankie":
    print("Girls split up")
    if name == "TT":
        print("The girls get arrested")
        names.remove("Frankie")
        names.remove("Cleo")
        names.remove("TT")
        names.remove("Stoney")
    elif name== "Stoney":
        print("TT dies")
        print("Cleo and Frankie gets arrested")
        names.remove("Frankie")
        names.remove("Cleo")
        names.remove("TT")
    elif name== "Frankie":
        print("TT gets shot")
        print("Cleo dies in police accident")
        print("Stoney gets on a bus to mexico")
        names.remove("Cleo")
        names.remove("TT")
        names.remove("Stoney")
else:
    print("You win the game")
                    
#main()
                    #names.remove("Stoney")
                    #names.remove("Frankie")
                    #names.remove("Cleo")
                    #names.remove("TT")
                    #print("Game Over")
                    


                    
