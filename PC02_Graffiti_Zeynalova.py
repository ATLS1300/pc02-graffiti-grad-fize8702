#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:28:20 2020

@author: fidan
"""

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("grey68")
panel.bgpic(image)

#=======Add your code here======

#Creating turtle

t = Turtle()
t.pensize(20)
t.shape('turtle')
t.speed(8)
t.pencolor(80, 80, 85)
t.fillcolor(45, 45, 45)

# Drawing a hat for the cold weather :D

t.up()
t.goto(50, 170)
t.left(100)
t.down()
t.begin_fill()
t.circle(75, 180)
t.end_fill()
t.left(90)
t.goto(50, 170)
t.left(180)
t.pensize(30)
t.forward(210)

# Drawing the Levitating Cube

t.setheading(0)
t.up()
t.pensize(10)
t.pencolor(0,0,0)

# Front side of the Cube is Red

t.begin_fill()
t.fillcolor(255,0,0)
t.speed(8)
t.goto(170, -130)
t.down()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# Top side of the Cube is Green

t.begin_fill()
t.fillcolor(0,255,0)
t.speed(5)
t.goto(120, -85)
t.right(90)
t.forward(100)
t.goto(270, -130)
t.setheading(180)
t.forward(100)
t.end_fill()

# Left side of the Cube is Blue

t.begin_fill()
t.fillcolor(0,0,255)
t.speed(3)
t.goto(120, -85)
t.left(90)
t.forward(100)
t.goto(170, -230)
t.setheading(90)
t.forward(100)
t.goto(120, -85)
t.end_fill()

# I call it an abstract Burning Sun

#Yellow

t.up()
t.goto(300, 150)
t.down()
t.begin_fill()
t.fillcolor('yellow')
t.speed(10)
t.pensize(3)
t.circle(60)
t.end_fill()

#Orange

t.begin_fill()
t.fillcolor('orange')
t.speed(7)
t.pensize(6)
t.circle(50)
t.end_fill()

#Red

t.begin_fill()
t.fillcolor('red')
t.speed(5)
t.pensize(9)
t.circle(40)
t.end_fill()
t.up()

# Lastly, a simple smile or a gotee to brighten Jeff's day.

t.pensize(5)
t.goto(-10,55)
t.down()
t.setheading(280)
t.circle(30,180)
t.goto(-10,55)


# Ending the scene with Turtle landing on the Cube


t.up()
t.goto(220,-180)
t.fillcolor('black')


