# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:30:03 2014

@author: brandon
"""

from pattern.web import *
g  = Google ()
for result in g.search('Olin College'):
    print result.url    
    print plaintext(result.text)