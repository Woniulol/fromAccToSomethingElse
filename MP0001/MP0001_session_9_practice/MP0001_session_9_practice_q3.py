#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/24 22:32
@user: jiananwang
@title: MP0001_session_9_practice_q3
"""

a = {chr(i): (100 + (i - 97) * 10) for i in range(97, 97 + 26)}
print('-' * 5 + ' a ' + '-' * 5)
print(a)

alphas = [chr(i) for i in range(97, 97+26)]
betas = range(100, 360, 10)
a_in_class = { k: v for k, v in zip(alphas, betas)}
print('-' * 5 + ' a_in_class ' + '-' * 5)
print(a_in_class)
print(a == a_in_class)

b_2 = [[j for j in range(i, i+2+1)] for i in range(1, 997+1, 3)]
print('-' * 5 + ' b ' + '-' * 5)
print(b_2)

b_in_class = [[i, i+1, i+2] for i in range(1, 997+1, 3)]
print('-' * 5 + ' b_in_class ' + '-' * 5)
print(b_in_class)
print(b_2 == b_in_class)

print('-' * 5 + ' c ' + '-' * 5)
c = {}
for i in range(1, 11 + 1):
    c[chr(73 + i) + '5'] = [j for j in range(10 * i + 1, 10 * i + 4 + 1)]
    c[chr(73 + i) + '6'] = [j for j in range(10 * i + 3, 10 * i + 7 + 1, 2)]
print(c)

print('-' * 5 + ' c_4 ' + '-' * 5)
c_4 = {key: value for key, value in
       tuple(i for y in
             tuple(
                 ((chr(73 + i) + '5', [j for j in range(10 * i + 1, 10 * i + 4 + 1)]),
                  (chr(73 + i) + '6', [j for j in range(10 * i + 3, 10 * i + 7 + 1, 2)]))
                 for i in range(1, 11 + 1))
             for i in y)
       }
print(c_4)

q3c = {k+str(j): ([m for m in range(10*(i+1)+1, 10*(i+1)+5)]
                  if j == 5 else [m for m in range(10*(i+1)+3, 10*(i+1)+8, 2)])
       for j in range(5, 7)
       for i, k in enumerate(list("JKLMNOPQRST"))}
print("(c)", q3c)
print("="*30)

print(c == c_4)

print('-' * 5 + ' d ' + '-' * 5)
d = tuple([i, (i * 5, i * 10)] for i in range(1, 20 + 1))
print(d)

# pay attention to the tuple comprehension

# you cannot tuple(a generator)
# you have to run the tuple when the generator is defined

