# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:24:45 2019

@author: libozhang
"""
#NumPy库简单练习

import numpy as np
import os
import pandas as pd
import matplotlib.plot as plt
import matplotlib

myfont=matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyhl.ttc')

with open("C:/Users/libozhang/Desktop/demo.TXT") as f:
    data=f.readlines()