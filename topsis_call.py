# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 07:43:34 2020

@author: HP
"""

#cmd call
#python topsis_call.py Indian_Idol.csv 1,2,1,1,1 "+","+","-","+","+"

import topsis as tp
import pandas as pd
import numpy as np
import sys

if len(sys.argv)!=4:
    print("Insufficient number of arguments! Please provide 3 arguments")
    exit(0)

if len(sys.argv[2])!=len(sys.argv[3]):
    print("Length of parameter 2 and parameter 3 should be same")
    exit(0)
dataset= tp.Topsis(sys.argv[1])

weights=[int(w) for w in sys.argv[2].split(',')]
impacts=[str(im) for im in sys.argv[3].split(',')]
result =tp.Topsis.evaluate(dataset,weights,impacts)

print(result)