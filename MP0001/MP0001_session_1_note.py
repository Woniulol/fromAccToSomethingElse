#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:49:12 2023

@author: jiananwang
"""

print('hello world')

if 1 > 2:
	print('How come?')
else:
	print('Hello World')

while 1  > 2:
	print('Oh no!!!')
print("Finished while loop.")

i = 1
while i <= 10:
	print(i, end = " \n")
	if i % 2 == 0:
		i += 3
	else:
		i += 1 #  <-- this is same as i = i + 1

total = 0

for i in range(10): # rang(10) --> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	print(i, end = " \n")
	total += i

print(total)
print('-' * 20)

i = 0
while i < 20:
	if i % 2 == 0:
		i += 1
		continue # from here it will jump to the beginning of the loop (i.e. start a new loop)
	if i >= 8:
		break # jump out of the loop (i.e. the loop will be ended)
	print(i, end = ' ')
	i += 1
print('-' * 20)

total = 0

for i in [1, 17, 5, 1, 0, 3, 11, 4]:
	if i == 0:
		break
	elif i < 5:
		continue
	else:
		total += i

print(total)

print('-' * 20)
for i in range(1, 7, 2): print(i, end=" ")

def printHelloWorld():
	print('Hello World')

printHelloWorld()

# lucky = input('Enter number:')
# print('your lucky number is', lucky)

def calcSquare(x):
	return x * x

area = calcSquare(3)
print(area)

# we create an error
try:
	i = 1 / 0
except:
	print('there is an erro in calculation')
    
i=0
while i < 20:
    if i % 2 == 0: 
        i += 1
        # continue 
    if i >= 8:
        break
    print(i, end=" ")
    i += 1

total = 100
try:
	total += 555 / 0
	print('total = ', total)
except:
	print('oops, error!!!')
finally:
	total += 200
	print('We are done. total =', total)









