#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:22:12 2023

@author: jiananwang
"""
# practice question - 1

import turtle as t

def initialize():
    t.up()
    t.goto(0, 0)
    t.setheading(0)

t.speed(5)
t.setup(width=600, height=600, startx=200, starty=200)

# # Q1.1
# initialize()
# t.down()
# count_square  = 0
# while count_square < 4:
#     t.forward(100)
#     t.left(90)
#     count_square += 1
# t.up()
# t.done()

# # ----------------

# # Q1.2
# initialize()
# t.setheading(-45)
# t.down()
# t.circle(50 * (2**0.5), steps=4)
# t.done()
# # ----------------


# # Q2.1
# initialize()
# t.down()
# count_e_triangle = 0
# while count_e_triangle < 3:
#         t.forward(100)
#         t.left(120)
#         count_e_triangle += 1
# t.up()
# t.down()
# # ----------------

# # Q2.2
# initialize()
# t.setheading(-60)
# t.down()
# t.circle(100, steps=3) # the length is not 100
# t.done()
# # ----------------

# # Q3
# initialize()

# # print the trapezium
# t.goto(0,-100)
# t.down()

# t.fillcolor('brown')
# t.begin_fill()

# t.forward(120) # bottom line
# t.goto(120 - ((120 - 100) / 2), -100 + 80) # upper right of the trapezium
# t.setheading(180) # reverse direction
# t.forward(100)

# t.end_fill()

# # print the square
# t.fillcolor('orange')
# t.begin_fill()

# t.right(90) # from the upleft of the trapezium
# t.forward(80)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(80)

# t.end_fill()
# t.up()

# # print the circle
# t.fillcolor('yellow')
# t.begin_fill()

# t.goto(120 / 2, -100 + 80 * 2) # connection point of circle and rectangle
# t.setheading(0)
# t.down()
# t.circle(80 / 2)
# t.up()
# t.end_fill()

# # print the triangle
# x, y = t.pos() # connection point of circle and rectangle
# t.fillcolor('red')
# t.begin_fill()
# t.goto(x - 50, y + 80) # bottom-left of the triangle
# t.down()
# t.forward(100) # bottom line of the triangle
# t.goto(x, y + 80 * 2) # top
# t.goto(x - 50, y + 80) # bottom-left of the triangle
# t.end_fill()

# # print the face
# initialize()
# t.goto(x, y + 10)
# t.setheading(0)
# t.down()
# t.circle(20, extent=-90)
# t.circle(20, extent=180)

# # print two eyes
# t.fillcolor('blue')


# t.up()
# t.goto(x-20, y+40)

# t.down()
# t.begin_fill()
# t.circle(-6)
# t.end_fill()

# t.up()
# t.goto(x+20, y+40)

# t.down()
# t.begin_fill()
# t.circle(6)
# t.end_fill()

# initialize()
# t.done()
# # ----------------

# # Q4
# initialize()

# t.goto(-50, -50)
# t.down()

# count = 0
# while count < 4:
#     t.forward(50)
#     t.circle(-50)
#     t.forward(50)
#     t.left(90)
#     count += 1

# t.done()

# # ----------------

# # Q5
# initialize()

# t.goto(0, -100)
# t.down()

# count = 0
# while count < 6:
#     t.circle(100, extent=360/6, steps=1)
#     t.right(60)
#     t.circle(-100, steps=6) # right hand side
#     t.left(60) # back to the right direction for the basic hexagon

#     count += 1

# t.done()

# # ----------------

# # Q6
# initialize()

# t.width(10)
# count = 0
# heading = t.heading()

# while count < 12:
#     t.setheading(heading)
#     t.forward(200)
#     t.down()
#     t.forward(20)
#     initialize()

#     count += 1
#     heading += 360/12

# # print minute-hand
# initialize()
# t.color('purple')
# t.down()
# t.right((12 / 60 * 360) - 90)
# t.forward(180)
# t.up()

# # print hour-hand
# initialize()
# t.width(25)
# t.color('red')
# t.down()
# t.right((10 / 12 * 360 + 12 / 60 / 12 * 360) - 90)
# t.forward(100)
# t.up()

# t.done()

# # ----------------

# # Q7
# initialize()
# t.speed(0)
# t.width(10)

# count_1min = 0
# heading = t.heading()

# # the clock
# while count_1min < 60:
#     t.setheading(heading)
    
#     if count_1min % 5 == 0:
#         t.forward(200)
#         t.down()
#         t.color('black')
#         t.forward(20)
#         initialize()
#     else:
#         t.forward(200)
#         t.down()
#         t.color('blue')
#         t.forward(10)
#         initialize()
    
#     count_1min += 1
#     heading += 360/60

# # the second-hand clock
# initialize()
# t.delay(1000)
# t.goto(0,180)

# while True:
#     t.delay(1000) # 1000ms = 1s
#     # t.down()
#     t.circle(-180, extent=360/60, steps=1)

# t.done()
# # ----------------
    




















