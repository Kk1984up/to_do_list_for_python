# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:55:42 2019

@author: libozhang
"""
import torch
import numpy as np
a=np.ones(1000)
b=torch.from_numpy(a)
np.add(a,1.92,out=a)
print(a)
print(b)