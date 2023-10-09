#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:16:03 2023

@author: jiananwang
"""
# practice question - 3

import turtle as t

def initialize():
    t.up()
    t.goto(0, 0)
    t.setheading(0)


t.speed(5)
t.setup(width=850, height=850, startx=50, starty=50)

# # Q1
# initialize()

# textMes = t.textinput(
#     title='getText Window', 
#     prompt='please input the text:')

# print(textMes)
# t.write(textMes,font=('Times', 16))

# t.done()
# # ----------------

# # Q2
# initialize()
# t.goto(-300,300)

# endingMes_user = 'Exiting loop due to user'
# endingMes_overflow = 'Exiting loop due to overflow'

# while True:
    
#     textMes = t.textinput(
#         title='getText Window', 
#         prompt='please input the text:').strip()
    
#     if textMes == 'END':
#         print(endingMes_user)
#         break
    
#     t.write(textMes,font=('Times', 60))
#     t.goto(-300, t.pos()[1] - 80)


#     if t.pos()[1] < -300:
#         print(endingMes_overflow)
#         break
        
# t.done()
# # ----------------

# # Q3
# initialize()

# textList = []
# textLong = ''
# textList_3word = []
# textPerLine = 3
# endingMes_overflow = 'Exiting loop due to overflow'
# initialPos = (-300, 300)

# # get text and store in list
# while True:
#     textMes = t.textinput(
#         title='getText Window', 
#         prompt='please input the text:').strip()
    
#     if textMes == 'END':
#         break
#     elif textMes == '':
#         continue
#     else:
#         textList.append(textMes)

# print('textList = ', textList)

# # long text
# textLong = ' '.join(textList)
    
# print('textLong = ', textLong)

# # list of 3 word long line
# textList = textLong.split()
# print('textList = ', textList)

# while len(textList) != 0:
#     tempText = " ".join(textList[:3])
#     textList_3word.append(tempText)
#     textList = textList[3:]

# print(textList_3word)

# # draw
# t.goto(initialPos)

# for i in textList_3word:
#     t.write(i,font=('Lucida Handwriting', 40))
#     t.goto(initialPos[0], t.pos()[1] - 50)
    
#     if t.pos()[1] < -300:
#         print(endingMes_overflow)
#         t.done()
#         break
    
# t.done()
# # ----------------

# # Q4
# def drawFunction(character):
#     if character == '_':
#         t.setheading(0)
#         t.down()
#         t.forward(25)
#         t.up()
#     elif character == 'S':
#         drawSquare(50)
#     elif character == 's':
#         drawSquare(25)
#     elif character == 'T':
#         drawETriangle(50)
#     elif character == 't':
#         drawETriangle(25)


# def drawSquare(sideLength):
#         t.setheading(90)
#         t.down()
#         t.forward(sideLength)
#         t.right(90)
#         t.forward(sideLength)
#         t.right(90)
#         t.forward(sideLength)
#         t.up()


# def drawETriangle(sideLength):
#         t.setheading(60)
#         t.down()
#         t.forward(sideLength)
#         t.right(120)
#         t.forward(sideLength)
#         t.up()


# initialize()
# t.goto(-400, 0)

# textMes = t.textinput(
#     title='getText Window', 
#     prompt='please input the text:')

# textList = list(textMes)

# if set(textList) !=  {'S', 's', 'T', 't', '_'}:
#     print('Entered strings are not valid.')
#     raise SystemExit()
# else:
#     while len(textList) != 0 and t.pos()[0] < 300:
#         drawFunction(textList[0])
#         textList.pop(0)

# # print(t.pos()[0])
# # 300.00000000000006
# t.done()
# # ----------------

# # Q5
# def drawFunction(character, multiplier):
#     if character == '_':
#         t.setheading(0)
#         t.down()
#         t.forward(25 * multiplier)
#         t.up()
#     elif character == 'S':
#         drawSquare(25 * multiplier)
#     elif character == 'T':
#         drawETriangle(25 * multiplier)


# def drawSquare(sideLength):
#         t.setheading(90)
#         t.down()
#         t.forward(sideLength)
#         t.right(90)
#         t.forward(sideLength)
#         t.right(90)
#         t.forward(sideLength)
#         t.up()


# def drawETriangle(sideLength):
#         t.setheading(60)
#         t.down()
#         t.forward(sideLength)
#         t.right(120)
#         t.forward(sideLength)
#         t.up()


# textMes = t.textinput(
#     title='getText Window', 
#     prompt='please input the text:'
#     )

# textList = list(textMes)
# tupleList = []

# while len(textList) != 0:
#     tupleList.append((textList[0], int(textList[1])))
#     textList.pop(0)
#     textList.pop(0)

# initialize()
# t.goto(-400, 0)

# for character, multiplier in tupleList:
#     drawFunction(character, multiplier)

# t.down()
# # ----------------
    









    
    
























