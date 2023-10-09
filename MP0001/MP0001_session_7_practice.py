#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:01:40 2023

@author: jiananwang
"""

"""
Question 1
Suggest a data representation format to store the explanations of 5 
commonly used Python keywords: for, while, if, try, def.

Answer 1
Diction
"""
print('=' * 10 + 'Question 1' + '=' * 10)

"""
Question 2
How would you represent an Accounts Journal Entry with the following columns:
• Date of Entry: Eg, 2021-Jun-01
• Account Code: Eg, REVEN, XCOGS
• Credit or Debit: Eg Credit, Debit
• Amount (S$): Eg 125.24, 5344.73
• Remarks: Eg Expense claimed on 2021-Apr-15

Answer 2
"""
print('=' * 10 + 'Question 2' + '=' * 10)

class accounts_journal_entry:
    def __init__(self, date, code, credict_or_debit, amount, remarks=None):
        self.date = date
        self.code = code
        self.credict_or_debit = credict_or_debit
        self.amount = amount
        self.remarks = remarks


entry_1 = accounts_journal_entry('2021-Jun-01', 'XCOGS', 'Credit', 125.24,
                                 remarks='Expense claimed on 2021-Apr-15')
print(entry_1)
print(entry_1.date)
print(entry_1.code)
print(entry_1.credict_or_debit)
print(entry_1.amount)
print(entry_1.remarks)

"""
Question 3
What are the outcomes of

Answer 3
"""
print('=' * 10 + 'Question 3' + '=' * 10)
print('-' * 10 + '1' + '-' * 10)
print('abc' + '123')
# print('abc' + 123) 

print('-' * 10 + '2' + '-' * 10)
# print('abc' * '123')
print('abc' * 123)
# print('abc' * 123.45)

print('-' * 10 + '3' + '-' * 10)
print('abc' * True)
print(True * 'abc')
print(False * 'abc')  # return a string of nothingess

print('-' * 10 + '4' + '-' * 10)
print(123.5 / 4)
print(123.5 // 4)

print('-' * 10 + '5' + '-' * 10)
print(123 / True)
# print(123 / False)

print('-' * 10 + '6' + '-' * 10)
print([1,2,3] + [5,2,1])
print([1,2,3] * 5)

print('-' * 10 + '7' + '-' * 10)
# print({1,2,3} + {5,2,1})
# print({1,2,3} * 5)

print('-' * 10 + '8' + '-' * 10)
# print({'a':1, 'b':2, 'c':5} + {3:'A', 2:'B', 1:'C'})

print('-' * 10 + '9' + '-' * 10)
print(list('abcdefg'))

print('-' * 10 + '10' + '-' * 10)
# print(dict([1, 4], [5, 9]))
print(dict([(1,4),(5,9)]))

print('-' * 10 + '11' + '-' * 10)
print(set(list('abracadabra')))

"""
Question 4
Peter likes to add two variables, x and y, as integers. He knows that 
both variables can be either of type str or float. 
How can Peter achieve this using a single Python statement that starts 
with: ans = ... ?

Answer 4
"""
print('=' * 10 + 'Question 4' + '=' * 10)
x = 10.0
y = '7'
ans = int(x) + int(y)
print('ans = ', ans)

"""
Question 5
(a) Ask user to input a string, and prints out first only the even position 
characters (0, 2, ,4, ...) and then on a new line, 
prints out only the odd-positioned characters. 
Eg, if user enters “Hello!”, your program should 
print out “Hlo” and then “el!”

(b) Now re-do (a) by printing out the even-positioned and 
odd-positioned characters in reverse.
"""
print('=' * 10 + 'Question 5' + '=' * 10)

input_str = input('Please enter a string: ')
even_postion_str = ''
odd_postion_str = ''

for index, value in enumerate(input_str):
    if index % 2 == 0:
        even_postion_str += value
    else:
        odd_postion_str += value

print('even_postion_str = ', even_postion_str)
print('odd_postion_str = ', odd_postion_str)

even = ''.join([value for index, value in enumerate(input_str) if index % 2 == 0])
odd = ''.join([value for index, value in enumerate(input_str) if index % 2 != 0])
print("even = ", even)
print("odd = ", odd)

evens = input_str[::2]
odds = input_str[1::2]
print("evens = ", evens)
print("odds = ", odds)

even_postion_str_reversed = even_postion_str[-1::-1]
odd_postion_str_reversed = odd_postion_str[-1::-1]
print('even_postion_str_reversed = ', even_postion_str_reversed)
print('odd_postion_str_reversed = ', odd_postion_str_reversed)

"""
Question 6
Ask user to enter 2 strings, and the recombined the 2 strings 
into single string using one character alternatively from each input strings, 
starting with the first input string.
Eg, if user enters “eehn” and “lpat”, your program should print out “elephant”.

Answer 6
"""
print('=' * 10 + 'Question 5' + '=' * 10)

input_str_1 = input('Please enter the 1st string: ')
input_str_2 = input('Please enter the 2nd string: ')

input_str_1_list = list(input_str_1)
input_str_2_list = list(input_str_2)

len_max = max(len(input_str_1), len(input_str_2))

combined_str_list = [ ]

for i in range(len_max):
    combined_str_list.extend(input_str_1_list[i: i+1])
    combined_str_list.extend(input_str_2_list[i: i+1])

print('recombined string: ', ''.join(combined_str_list))
    
    
    


















