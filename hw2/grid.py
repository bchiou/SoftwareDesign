# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:42:20 2014

@author: brandon

creates 2x2 grid with '+' and '-'
"""
"""
def do_quad(f):
    f()
    f()
    f()
    f()

def print_hor():
    print '+----+----+'
def print_ver():
    print '|    |    |'
    
for i in range(2):
    print_hor()
    do_quad(print_ver)
print_hor()
"""

"""
creates 4x4 grid with '+' and '-'
"""

def do_quad(f):
    f()
    f()
    f()
    f()

def print_hor():
    print '+----+----+----+----+'
def print_ver():
    print '|    |    |    |    |'


def grid(size)
    for i in range(size):
        print_hor()
        do_quad(print_ver)
    print_hor() 

grid(4)