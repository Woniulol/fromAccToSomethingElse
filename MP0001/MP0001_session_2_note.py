#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:01:28 2023

@author: jiananwang
"""

import os

x = 123 # assigning value
print("A. In global namespace: x =", x)
# value of x is referenced

x = 123
X_OK = 567
print("A. x = ", x, "and X_OK = ", X_OK)
print("B. x = ", x, "and X_OK = ", X_OK)
print("C. os.X_OK = ", os.X_OK)

def sumProfit(profit1, profit2):
	x = profit1 + profit2
	print('=== In sumProfit function ===')
	print('profit1=', profit1, 'profit2=', profit2)
	print('x=', x) # will be the x within the namespace of sumProfit() and does not
	print('=== Returning from sumProfit ===')
	return x

x = 789
X_OK = 345
print("D. Before function call x =", x, 'and X_OK=', X_OK)
totalProfit = sumProfit(x, X_OK)
print('E: After function call x=', x, 'and X_OK=', X_OK, 'totalProfit=', totalProfit) # the x variable within sumProfit() wont influence the global variable x

x = 456
y = 1000
print('F: x=', x, 'y=', y)

def difference (v1, v2): # even though here we do not give the function a parameter for x, since x is a global variable, it is still reachable by the function
	print("=== Inside difference function ===")
	print('x=', x, 'v1=', v1, 'v2=', v2)
	diff = v1 - v2 - x
	return diff

d = difference(800, 1000)
print('F: d=', d, 'x=', x)

def setX(newValue):
	global x
	x = newValue

setX(200)
d2 = difference(800,1000)
print("G: d2=", d2, "x=",x)

text1 = '123'
text2 = '456'
print(f'the first str is {text1}, the second str is {text2 + "aaa"}')
print('the first str is %s, the second str is %s' % (text1, text2))

print(r"what you see is what you \n get \x21")
print("what you see is what you \n get \x21")

a = b"0123\xFF\xFE\xFD"
print(a)
b = b"\x30\x31\x32"
print(b)

print('-' * 100)
print('~3 = ', ~3 , 'this should not be your expected answers')
print('~3 = ', ~3 & 2, 'this should be your expected ')
print((3).bit_length( ) == (2).bit_length( ))
print('-' * 100)
print('~3 = ', ~3 , 'this should not be your expected answers')
print('~3 = ', ~3 & 2, 'this should be your expected ')
print((3).bit_length( ) == (2).bit_length( ))
print((156).bit_length( ) == (255).bit_length( ))

decimal_number = int('11111100', 2)
print(decimal_number)

from collections import defaultdict
word_counts = defaultdict(int)
for word in "A sentence with a message".split():
	word_counts[word.lower()] += 1

print(word_counts)