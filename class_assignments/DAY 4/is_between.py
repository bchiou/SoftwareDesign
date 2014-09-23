# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:55:37 2014

@author: brandon
"""

x = int(raw_input('What is the value of "x"?\n'))
y = int(raw_input('What is the value of "y"?\n'))
z = int(raw_input('What is the value of "z"?\n'))

def is_between(x,y,z):
   return x <= y <= z
print is_between(x, y, z)