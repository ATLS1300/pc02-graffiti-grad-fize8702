#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:00:12 2020

@author: Dr. Z

A generative art piece that uses 5 turtles to make random walk patterns in 
different colors. One turtle draws a wiggly spiral in the middle of the 
screen. 
"""
from turtle import *
import math, random

# create palette
COLORS = ['aquamarine','pink','white','orange','yellow']

# create screen, and set size
panel = Screen()
w = 500
h = 500
panel.setup(width=w,height=h)
tracer(0) # turn off the animation or it will take forEVER

# set background color
panel.bgcolor('purple')

# define variables for turtle movement
step = 2  # amount of straightness in paths
rot = 90  # amount of bend in paths # moved here for better legibility

# create turtles
turtle1 = Turtle(visible=False)
turtle2 = Turtle(visible=False)
turtle3 = Turtle(visible=False)
turtle4 = Turtle(visible=False)
spiral = Turtle(visible=False)

# I am not sure if the turtles below are meant to pick the colors randomly or are assigned to pick 1 color each, as assigned. 

# assign colors
turtle1.color(COLORS[0])
turtle2.color(COLORS[1])
turtle3.color(COLORS[2])
turtle4.color(COLORS[3])
spiral.color(COLORS[4]) #random.choice(COLORS)) #this comment is making me 
#confused and has two closing parenthesis.
# I don't think #random.choice(COLORS)) need to be in this code

# Code below is not defined right, therefore, it is useless
# thicc = 20  # pen width 

# We could keep each line of width seperated like this on the top
# for later modification or define them like on the line 65

# turtle1.width(20)
# turtle2.width(20)
# turtle3.width(20)
# turtle4.width(20)
# spiral.width(20)

# This way all my turtles will have the same width
# """I asked my brother to help me to define all of my turtles to draw with the same width
# and he gave me a feedback on how to write the code below"""
def fatTurtles (turtles):
   for t in turtles:
       t.width(20)

fatTurtles([turtle1, turtle2, turtle3, turtle4, spiral])

# all the penup and pendown functions should be shifted to lines shown below
# in order for the turtles to actually draw the art work


# place randomly around edge screen
turtle1.penup()
turtle1.pendown()
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle1.goto(X,Y)
turtle1.seth(turtle1.towards(0,0))


# place randomly around edge screen
turtle2.penup()
turtle2.pendown()
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle2.goto(X,Y)
turtle2.seth(turtle1.towards(spiral))

# place randomly around edge screen
turtle3.penup()
turtle3.pendown()
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle3.goto(X,Y)
turtle3.seth(turtle1.towards(0,0))


# place randomly around edge screen
turtle4.penup()
turtle4.pendown()
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle4.goto(X,Y)
turtle4.seth(turtle1.towards(0,0))



# walk forward (iterate 10000 times or use a while loop) with random turns
for i in range(10000): # I changed the range from 2 to 10000 as instructed on the comment above
    
    turtle1.forward(step)
    turtle1.left(random.randint(-rot,rot))
    turtle2.forward(step)
    turtle2.left(random.randint(-rot,rot))
    turtle3.forward(step)
    turtle3.left(random.randint(-rot,rot))
    
    #2 lines below have incorrect indentation
    
    # therefore I fixed the indentation to match the rest
    turtle4.forward(step)
    turtle4.left(random.randint(-rot,rot))
    spiral.left(random.randint(-rot,rot))
    
    # TODO: spin in circles??
    spiral.forward(random.randint(-step*2,step*2))
    spiral.left(rot)
    
# I modified the ending code to the one listed below for easier exit from the screen
panel.exitonclick()

# """ I really enjoyed the idea of the randomness after drawing 4 straight lines in this composition.
# The overall code had issues with mainly the placement of some of the codes, especially,
# penup and pendown to be able to actually draw the codes that is included for the art.
# Overall, the given code was easy to clean up and didn't require much additional lines of codes.
# As a creative, I also really enjoyed the color scheme and final outcome of the abstract art a lot."""


