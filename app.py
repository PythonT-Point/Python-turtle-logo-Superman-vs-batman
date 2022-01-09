from turtle import *
import turtle as tur
 
#get the turtle object and save it in turt variable
turt = tur.Turtle()
 
#size of pointer and pen
turt.turtlesize(1, 1, 1)
turt.pensize(3)
 
#screen info
ws = tur.Screen()
ws.bgcolor("cyan")
ws.title("Pythontpoint")
 
#change the color of pen
turt.color("yellow", "black")
 
 
#begin filling color
turt.begin_fill()
 
#turn1
turt.left(90)   # turn pointer direction to left of 90'
turt.circle(50, 85) #draw circle of radius = 50 and 85'
turt.circle(15, 110)
turt.right(180) 
 
#turn 2
turt.circle(30, 150)
turt.right(5)
turt.forward(10) #draw forward line of 10 units
 
#turn 3
turt.right(90)
turt.circle(-70, 140)
turt.forward(40)
turt.right(110)
 
#turn 4
turt.circle(100, 30)
turt.circle(30, 100)
turt.left(50)
turt.forward(50)
turt.right(145)
 
#turn5
turt.forward(30)
turt.left(55)
turt.forward(10)
 
#reverse
 
#turn 5
turt.forward(10)
turt.left(55)
turt.forward(30)
 
#turn 4
 
turt.right(145)
turt.forward(50)
turt.left(50)
turt.circle(30, 100)
turt.circle(100, 30)
 
#turn 3
turt.right(90)
turt.right(20)
turt.forward(40)
turt.circle(-70, 140)
 
#turn 2
turt.right(90)
turt.forward(10)
turt.right(5)
turt.circle(30, 150)
 
#turn 1
turt.left(180)
turt.circle(15, 110)
turt.circle(50, 85)
 
#end color filling
turt.end_fill()
 
#end the turtle method
tur.done()