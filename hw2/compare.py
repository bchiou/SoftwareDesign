# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:38:18 2014

@author: brandon
"""

x = int(raw_input('Value for "x"?\n'))
y = int(raw_input('Value for "y"?\n'))

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print compare(x,y)