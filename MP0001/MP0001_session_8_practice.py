#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:07:50 2023

@author: jiananwang
"""

"""
Q1. 
Write a Python function to calculate the sum of integers from 1 to 60,000.
"""
print()
print('=' * 10 + 'Question 1' + '=' * 10)

def my_sum(start: int, end: int) -> int:
    """
    return the sum of the integers from start to end (both inclusive)
    """
    return sum(range(start, end+1))

def my_sum2(n):
    results = (1 + n) * n // 2
    return results


print("my_sum: ", my_sum(1, 60000))
print("my_sum2: ", my_sum2(60000))
# print(f"sum form {start:d} to {end:d} is: ", my_sum(60000))

total = my_sum(1, 60000)
print(f"{total:,d}")
print(f"{total: 7,d}")  # zero fillers

"""
Q2. Write a Python function to calculate the sum of squares of integers from 2 to 100,000
which are divisible by 3.
"""
print()
print('=' * 10 + 'Question 2' + '=' * 10)

def my_sum_of_squares(start: int, end: int, divisible: int) -> int:
    """
    return the sum of squares of integers from start to end (both inclusive) that are divisible by 3
    """
    return sum(i ** 2 for i in range(start, end+1) if i % divisible == 0)


print(my_sum_of_squares(2, 100000, 3))

"""
Q3. Fibonacci sequence starts from 1, 1, 2, 3, 5, 8, 13, ... and never ends, where the next integer is the sum of the previous 2 integers. Write a Python function to calculate the sum of first 5,000 Fibonacci integers. (Note: the first and second Fibonacci integers are 1, and 1)
"""
print()
print('=' * 10 + 'Question 3' + '=' * 10)

def my_sum_fibonacci(count: int) -> int:
    """
    return the sum of fist count Fibonacci integers as the first and second Fibonacci integers are 1 and 1.
    """
    fibona_list = [1, 1]
    while len(fibona_list) < count:
        fibona_list.append(sum(fibona_list[-2:]))

    return sum(fibona_list[:count])  # [:count]: in case count is 1 


print(my_sum_fibonacci(10000))


"""
Q4. Write a function which takes a list of integers, filters out any integer which is divisible by 2 or 5, and returns the remaining list.
"""
print()
print('=' * 10 + 'Question 4' + '=' * 10)

def pop_2_and_5(lst: list) -> list:
    """
    take a list of integers, filter out any integer divisible by 2 or 5, returns the remaining list
    """
    return (list(i for i in lst if (i % 2 != 0) and (i % 5 !=0)))

my_ls = list(range(31))
print(pop_2_and_5(my_ls))
    
"""
Q5. Write a function wordHistogram(dt) that takes a piece of text string and returns a dictionary where the unique words in the text are the keys, and the values are the frequencies of occurrences of the words in the text. All words are reduced to lowercase. Punctuation marks are all ignored. Hyphenated words are treated as two words (ie the hyphen is ignored). So the returned dictionary shall have no punctuation mark in any of the keys. The values are integers.
Write another assisting function printHistogram(dt) to print this dictionary, such that key- values which have the highest frequencies are printed first, then the next highest, and so on.
"""
print()
print('=' * 10 + 'Question 5' + '=' * 10)

def wordHistogram(strs: str) -> dict:
    import string
    strs = strs.strip().lower().replace('-', " ")
    
    for i in string.punctuation:
        strs = strs.replace(i, '')
        
    strs = strs.split( )
    strs_dict = { }
    for word in set(strs):
        strs_dict[word] = strs.count(word)
    
    return strs_dict
    
def printHistogram(dt: dict) -> tuple:
    ls = [(count, key) for key, count in dt.items()]
    ls.sort(reverse=True)
    
    for count, key in ls:
        print((key, count))


my_str = '''
Write a function wordHistogram(dt) that takes a piece of text string and returns a dictionary where the unique words in the text are the keys, and the values are the frequencies of occurrences of the words in the text. All words are reduced to lowercase. Punctuation marks are all ignored. Hyphenated words are treated as two words (ie the hyphen is ignored). So the returned dictionary shall have no punctuation mark in any of the keys. The values are integers.
Write another assisting function printHistogram(dt) to print this dictionary, such that key- values which have the highest frequencies are printed first, then the next highest, and so on.
'''

dict_of_my_str = wordHistogram(my_str)
printHistogram(dict_of_my_str)

"""
Q6. to approximate integration of the function

- The rectangle's width is determined by the interval of integration
    one rectangle could span the width of the interval of integration and approximate the entire integral
    alternatively, the interval of integration could be sub-divided into n smaller intervals of equal lengths, and n rectangles would used to approximate the integral, each samller rectangle has the width of the smaller interval
- The rectangle's height is the function's value at the midpoint of its base

for interval [a, b]
- Area of rectangle = base * height = (b-a) * f[0.5*(b+a)]
"""
print()
print('=' * 10 + 'Question 6' + '=' * 10)

import numpy as np


def fn(x):
    return 1 / (x ** 2)


def integ(fn, start, end, n) -> float:
    rectangle_base = (end - start) / n
    rectangle_left_x = np.arange(start, end, rectangle_base)  
    # each middle point is calculated based on bottom-left point of each rectangle
    # no need to include the end (bottom-right) of last rectangle
    rectangle_middle_x = rectangle_left_x + (rectangle_base / 2)
    rectangle_middle_y = fn(rectangle_middle_x)

    return np.sum((rectangle_base * rectangle_middle_y))
    
area = integ(fn, 2, 10, 8)
print(area)
