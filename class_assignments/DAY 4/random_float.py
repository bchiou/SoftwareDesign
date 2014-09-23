# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:19:32 2014

@author: brandon
"""
import random

start = float(raw_input('What is the starting number?\n'))
stop = float(raw_input('What is the ending number?\n'))

def random_float(start, stop):
    return random.uniform(start, stop)

print random_float(start, stop)