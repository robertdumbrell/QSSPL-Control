# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 11:52:15 2015

@author: z3185971
"""

from useful_functions import *
import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(3,4,100)

print x
print x.astype(int)
print round_int_sig(x,5) 