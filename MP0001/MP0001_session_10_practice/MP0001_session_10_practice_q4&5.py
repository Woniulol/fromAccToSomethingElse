#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/25 16:27
@user: jiananwang
@title: MP0001_session_9_practice_q4&5
"""
import math

from is_prime import is_prime
import time as ttm


def get_prime(n):
    to_n = list(range(2, n + 1))
    for i in to_n.copy():
        if not is_prime(i):
            to_n.remove(i)
    return to_n


def get_eras(n):

    to_n = list(range(2, n + 1))
    count = 0

    while count < len(to_n) - 1:
        next_prime = to_n[count]
        for i in to_n.copy():
            if (i / next_prime > 1) and (i % next_prime == 0):
                to_n.remove(i)
        count += 1

    return to_n


def get_eras_2(n):
    primes = list(range(n+1))
    nlen = len(primes)
    stopping = int(math.sqrt(n)) + 1
    for k in range(2, stopping + 1):
        v = primes[k]
        if v == 0:
            continue
        i = k + k
        while i < n+1:
            primes[i] = 0
            i += k

    primes[1] = 0
    primesFin = [ p for p in primes if p != 0]
    return primesFin


prime_imported = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
    227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
    379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
    457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
    619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
    883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
    983, 991, 997
]

# start_time = ttm.time()
# prime_list_get_prime = get_prime(200000)
# end_time = ttm.time()
# get_prime_process_time = end_time - start_time
# print('get_prime_process_time = ', get_prime_process_time)

start_time = ttm.time()
prime_list_get_eras = get_eras_2(20)
end_time = ttm.time()
get_eras_process_time = end_time - start_time
print('get_eras_process_time = ', get_eras_process_time)

# print(prime_list_get_prime == prime_list_get_eras == prime_imported)
# print(prime_list_get_prime == prime_list_get_eras)
# print(len(prime_list_get_eras))

