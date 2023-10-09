#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/25 16:27
@user: jiananwang
@title: MP0001_session_9_practice_q2
"""
import math as m

amt = float(input('please enter a floating point number: '))
fractional_part, integer_part = m.modf(amt)

print(f"the integer part is {int(integer_part)}, while the fractional part is {fractional_part:.5f}")

integer_part_1 = m.floor(amt)
fractional_part_1 = m.fmod(amt, integer_part_1)

print(f"the integer part is {int(integer_part_1)}, while the fractional part is {fractional_part_1:.5g}")
