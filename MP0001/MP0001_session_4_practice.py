#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:49:44 2023

@author: jiananwang
"""

"""
practice question - 5
"""

import turtle as t

def initialize(pos=(0,0), heading=0):
    t.up()
    t.goto(pos)
    t.setheading(heading)


t.speed(5)
t.setup(width=850, height=850, startx=50, starty=50)

# # Q1.1 draw isosceles triangle
# def triangle(length, angle):
#     pos_initial = t.pos()
#     heading_initial = t.heading()

#     t.down()
#     t.left(angle)
#     t.forward(length)
#     t.right(2 * angle)
#     t.forward(length)
#     t.goto(pos_initial)
    
#     t.setheading(heading_initial)
#     t.up()


# initialize((-100, 50), 45)
# triangle(200, 75)
# t.done()
# # ----------------

# # Q1.2 draw isosceles triangle
# def triangle(length, angle):
#     heading_initial = t.heading()

#     top_angle = 180 - (2 * angle)
#     bottom_length = 2 * length * m.cos(m.radians(75))
    
#     t.down()
#     t.forward(bottom_length)
#     t.left(180 - angle)
#     t.forward(length)
#     t.left(180 - top_angle)
#     t.forward(length)
#     t.up()
    
#     t.setheading(heading_initial)


# initialize((-100, 50), 45)
# triangle(200, 75)
# t.done()
# # ----------------

# # Q2 draw centered circle
# def org_circle(radius):
#     pos_initial = t.pos()
#     heading_initial = t.heading()
    
#     t.up()
#     t.forward(radius)
#     t.left(90)
#     t.down()
#     t.circle(radius)
#     t.up()

#     t.goto(pos_initial)
#     t.setheading(heading_initial)    


# initialize((-100, -50), 45)
# org_circle(200)

# t.done()
# # ----------------

# # Q3 modify centered circle
# def org_circle(radius, col: str = None, filled: bool = False):
#     pos_initial = t.pos()
#     heading_initial = t.heading()
#     pencolor_initial = t.pencolor()
#     fillcolor_initial = t.fillcolor()

#     t.up()
#     t.forward(radius)
#     t.left(90)

#     if col != None:
#         t.pencolor(col)
        
#     if filled == True:
#         t.fillcolor(t.pencolor())
#         t.begin_fill()
        
#     t.down()
#     t.circle(radius=radius)
    
#     if filled == True:
#         t.end_fill()

#     t.up()
#     t.goto(pos_initial)
#     t.setheading(heading_initial)   
#     t.pencolor(pencolor_initial)
#     t.fillcolor(fillcolor_initial)


# initialize((100, -50), 135)
# org_circle(150, col='orange', filled=True)
# # org_circle(150)
# t.done()
# # ----------------

# # Q4
# def draw_y(angle, size):
#     t.forward(size)
    
#     tempPos = t.pos()
#     tempHeading = t.heading()
    
#     t.left(angle)
#     t.forward(size)
    
#     t.up()
#     t.goto(tempPos)
#     t.setheading(tempHeading)
#     t.down()
    
#     t.right(angle)
#     t.forward(size)


# def call_draw_y(position, hding, angle, size):
#     t.up()
#     t.goto(position)
#     t.setheading(hding)
#     t.down()
#     draw_y(angle, size)
#     t.up()


# call_draw_y((-200,100), 60, 100, 200)
# call_draw_y((250,-50), 245, 60, 60)
# t.done()
# # ----------------

# Q5.1
def draw_y_oneSide(angle, size, tilt):
    t.forward(size)
    
    tempPos = t.pos()  # Y junction pos
    tempHeading = t.heading()  # Y junction heading
    
    t.left(angle)
    t.forward(size)
    
    if size * 0.7 >= 10:
        t.left(tilt)
        draw_y_oneSide(angle, 0.7 * size, tilt)
    
    t.up()
    t.goto(tempPos)  # back to Y junction pos
    t.setheading(tempHeading)  # back to Y junction heading
    t.down()
    
    t.right(angle)
    t.forward(size)
    
    if size * 0.7 >= 10:
        t.right(tilt)
        draw_y_oneSide(angle, 0.7 * size, tilt)


initialize((0, -200), 90)
t.color('brown')
t.width(7)

t.down()
draw_y_oneSide(20, 80, 15)
initialize((0, -200), 90)

t.done()
# ----------------

# # Q5.2
# def draw_y_bottomUp(angle, size, tilt):
#     statusList = [ ]
#     t.forward(size)
#     tempPos = t.pos()
#     tempHeading = t.heading()
    
#     t.left(angle)
#     t.forward(size)
#     statusList.append((t.pos(), t.heading()))
    
#     t.up()
#     t.goto(tempPos)
#     t.setheading(tempHeading)
#     t.down()
    
#     t.right(angle)
#     t.forward(size)
#     statusList.append((t.pos(), t.heading()))
    
#     if 0.7 * size > 10:
#         for pos, heading in statusList:
#             t.up()
#             t.goto(pos)
#             t.setheading(heading)
            
#             if statusList.index((pos, heading)) == 0:
#                 t.left(tilt)
#             else:
#                 t.right(tilt)
                
#             t.down()
#             draw_y_bottomUp(angle, 0.7*size, tilt)


# initialize((0, -200), 90)
# t.color('brown')
# t.width(7)
# t.down()

# draw_y_bottomUp(15, 80, 15)
# initialize((0, -200), 90)
# t.done()











