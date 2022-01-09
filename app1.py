from turtle import *
import turtle as tur
#create turtle object and save it in the variable t
turt=tur.Turtle()
tur.title("Pythontpoint")
tur.Screen().bgcolor('navy') #set the color of the screen to navy to match Superman’s costume
 
def curve(value):
    for i in range(value): #for loop to repeat the inputted value number of times 
        turt.right(1) #step by step curve
        turt.forward(1)
 
turt.penup() #pen is in the up position so it will not draw
turt.setposition(0,43) #move the pen to these x and y coordinates
turt.pendown() #pen is in the down position so it will draw
turt.begin_fill() #start filling in the shape
turt.pencolor('black') #change the pen color to black
turt.fillcolor('maroon') #change the shape fill color to maroon to match the Superman logo
turt.pensize(3) #use a pen size of 3 to create a black border
turt.forward(81.5) #the pen will move forward this number to start the shield of the logo
turt.right(49.4) #rotate the pen right 49.4 degrees
turt.forward(58) #move the pen forward by 58 
turt.right(81.42) #rotate right by 81.42 degrees
turt.forward(182) #move the pen forward by 182
turt.right(98.36) #rotate the pen right by 98.36 degrees
turt.forward(182) #move the pen forward by 182 
turt.right(81.42) #rotate the pen by 81.42 degrees to the right
turt.forward(58) #move the pen forward 58 
turt.right(49.4) #rotate the pen to the right by 49.4
turt.forward(81.5) #move the pen forward by 81.5 to meet the start at the top of the shield
turt.end_fill() #complete the fill of the shield so the shape is closed off
turt.penup() #pen will not draw 
 
turt.setposition(38,32) #now to create the yellow parts of the Superman logo
turt.pendown() #the pen is now poised to draw
turt.begin_fill() #start a new shape 
turt.fillcolor('gold') #change the fill color to gold to match the Superman logo
turt.forward(13) #move the pen forward by 13
turt.right(120) #rotate the pen right by 120 degrees
turt.forward(13) #move the pen forward by 13
turt.right(120) #rotate the pen right by 120 degrees
turt.forward(13) #move the pen forward by 13
turt.end_fill() #the small triangle on the right is now complete
turt.penup() #stop the pen from drawing
 
turt.setposition(81.5,25) #now to create the larger yellow part of the Superman logo, change the position of the pen
turt.pendown() #the pen will now draw again
turt.begin_fill() #the fill is still the same color set before
turt.right(210) #rotate the pen right by 210 degrees
turt.forward(25) #move the pen forward by 25
turt.right(90) #rotate the pen right by 90 degrees
turt.forward(38) #move the pen forward by 38
turt.right(45) #rotate the pen right by 45 degrees
turt.circle(82,90) #this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
turt.left(90) #rotate the pen left by 90 degrees
turt.circle(82,60) #create a circle of radius 82 and only complete 60 degrees of the circle 
curve(61) #call the curve function that was previously defined, pass an integer value equal to the length of the curve desired 
turt.left(90) #rotate the pen left by 90 degrees
turt.forward(57) #move the pen forward by 57
turt.left(90) #rotate the pen left by 90 degrees
turt.forward(32) #move the pen forward by 32
turt.end_fill() #fill in the larger yellow part of the logo
turt.penup() #stop drawing 
turt.home() #reset the pen location to the origin so the orientation is also reset
 
turt.setposition(-69,-38) #finish the major parts of the S superimposition on the shield
turt.pendown()
turt.begin_fill()
curve(20)
turt.forward(33)
turt.left(10)
turt.circle(82,20)
curve(30)
turt.forward(10)
turt.right(110)
curve(40)
turt.right(10)
turt.circle(50,10)
curve(45)
turt.right(5)
turt.forward(45)
turt.end_fill()
turt.penup()
turt.home()
 
turt.setposition(20,-100)
turt.pendown()
turt.begin_fill()
turt.right(135)
turt.forward(27)
turt.right(90)
turt.forward(27)
turt.right(135)
turt.forward(38.18)
turt.end_fill()
turt.penup()
turt.home()
 
turt.setposition(-57,32)
turt.pendown()
turt.begin_fill()
turt.right(180)
turt.forward(18)
turt.left(45)
turt.forward(44)
turt.left(80)
turt.forward(15)
turt.left(130)
curve(40)
turt.forward(20)
turt.end_fill()
 
turt.hideturtle() #use this command to hide the turtle so it is not visible in the final image
tur.exitonclick()