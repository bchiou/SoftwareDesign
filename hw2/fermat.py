# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:56:26 2014

@author: brandon

function check_fermat
"""
a = int(raw_input('Value for "a"?\n'))
b = int(raw_input('Value for "b"?\n'))
c = int(raw_input('Value for "c"?\n'))
n = int(raw_input('Value for "n"?\n'))

def check_fermat(a, b, c, n):
    if n > 2 and (c**n) == (a**n) + (b**n):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No that doesn't work"

check_fermat(a, b, c, n)