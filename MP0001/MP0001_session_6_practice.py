#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:45:06 2023

@author: jiananwang
"""

"""
Question 1
Give 3 very different-looking, but valid, variable names

Answer 1
x, tmp, x_1, _, y1, strrange, _123, nOrI
"""

"""
Question 2
Give 5 very different-looking, but valid, literals.
"""

"""
Question 3
Peter would like to define a variable that stores the maximum mark allowed, which is 9. 
He wants this maximum mark to be visible (readable) to everywhere in his Python program, 
including within functions. How should he define the variable in Python?
"""

"""
Question 4
Write a Python program that prints out all integers between 100 to 200 (inclusive) 
and which are divisible by both 3 and 5, or divisible by both 6 or 7.
"""
     
for i in range(100, 200+1):
    if (i % 15 == 0) or (i % 42 == 0):
        print(i)

"""
Question 5
Write a Python program that asks user “How long did you walk today (in seconds)?”, 
and prints out the duration walked in hours, colon, minutes, colon, seconds. 
Minutes and seconds must be zero-padded on the left (eg a 2 should be printed as 02).
"""
input_time_in_sec = int(input('How long did you walk today (in seconds): '))

sec_str = '0' + str(input_time_in_sec % 60)
min_str= '0' + str(input_time_in_sec // 60 % 60)
hour_str = '0' + str(input_time_in_sec // 60 // 60)

print(f'Duration: {hour_str[-2:]}:{min_str[-2:]}:{sec_str[-2:]}')

"""
Question 6
Write a Python program that asks user “Enter base-10 integer to convert to base-2: ”, 
and prints out the correct base-2 representation. 
You must actually write the codes to perform the conversion in Python, 
not just make a call to any existing function.
"""

input_base_10_integer = int(input('Enter base-10 integer to convert to base-2: '))

digit_str = ''
while True:
    digit_str = str(input_base_10_integer % 2) + digit_str
    input_base_10_integer //= 2
    
    if input_base_10_integer == 0:
        break

print('0b' + digit_str)



        
        
    