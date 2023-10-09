#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:53:36 2023

@author: jiananwang
"""

"""/
Question 1
How does a Python program present a set of insturctions to computer?

Answer 1
Instructons are presented to Python (and computer) sequentialy by default.
We call the instruction is executed sequencially
"""

"""/
Question 2
What is the visual mechanism that Python uses to indicate a code block?

Answer 2
code block: a collection or segment of part of the code. Used quite casually.
visual mechanism: ":" with indent 

run-time environment --> the console
programming evnironment --> your script

code block concept is related to the real time environment, i.e. your scrpt.
"""

"""/
Question 3
What keywaords in Python indicate the start of a loop?

Answer 3
"for" and "while"

if we know how many time to loop or iterate just before the loop, we should/could use for loop
if we are not sure how many time to loop or the time to loop may be changed later, it's better to use while loop
"""

"""/
Question 4
Write a loop that prints out integers from 10 to 20 (inclusive)

Answer 4
"""
# for i in range(10, 20+1):
#     print(i)

"""/
Question 5
Write a while-loop that keeps asking for user input until user enters "The End" in exactly that casing.

Answer 5
"""
# text_input = ''
# while text_input != 'The End':
#     text_input = input('Please enter your text here: ')

"""/
Question 6
What mechanisms are there in Python that provide a jump away from current point of executing the sequential instructions?
Write an example cde for each mechanism.

Answer 6
Continue and Break
Hyperlink Jumps (def, class)
Try, Except and Finally
Return
"""

"""/
Question 7
"""
x = float(input('please input the number: '))
try:
    result = 1/x
except:
    result = float('inf')
print(result)






  
