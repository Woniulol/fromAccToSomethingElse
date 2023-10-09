#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:06:35 2023

@author: jiananwang
"""
# practice question - 2

import turtle as t

def initialize():
    t.up()
    t.goto(0, 0)
    t.setheading(0)

t.speed(5)
t.setup(width=850, height=850, startx=50, starty=50)

# # Q1
# initialize()

# for i in range(1, 11):
#     t.goto(-i * 25, -i * 25)
#     print(i, t.pos())
#     t.setheading(-45)
#     t.down()
#     t.circle(i * 50 / (2 ** (0.5)), steps=4) # 4 points in the Circumference and square root of two
#     t.up()

# initialize()
# t.done()
# # ----------------

# # Q2
# initialize()

# for i in range(1,11):
#     t.goto(0, -i * 50 / (2 ** (0.5)))
#     t.down()
#     t.circle(i * 50 / (2 ** (0.5)), steps=4) # square root of two
#     t.up()

# initialize()
# t.done()
# # ----------------

# # Q3
# initialize()

# for i in range(1,11):
#     t.goto(0, -i * 25)
#     t.down()
#     t.circle(i * 25)
#     t.up()

# initialize()
# t.done()
# # ----------------

# # Q4
# initialize()

# for i in range(1,11):
    
#     if i % 2 == 0: # odd or even
#         t.goto(-i * 25, 0)
#         t.setheading(-90)
#     else:
#         t.goto(i * 25, 0)
#         t.setheading(90)

#     t.down()
#     print(f"No.{i}, starting at {t.pos()}, heading toward {t.heading()}")
#     t.circle(i * 25, extent=180)
#     t.up()

# initialize()
# t.done()
# # ----------------

# Q5
initialize()

for i in range(1,11):
    if i % 2 == 0:
        t.goto(-i * 25, 0)
        t.setheading(-90)
    else:
        t.goto(i * 25, 0)
        t.setheading(90)

    t.circle(i*25, extent=60) # pen is up, pure rotation
    t.down()
    print(f"No.{i}, starting at {t.pos()}, heading toward {t.heading()}")
    t.circle(i*25, extent=180)
    t.up()

initialize()
t.done()
# ----------------
