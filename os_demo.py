# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:58:37 2019

@author: libozhang
"""

import os
import pandas as pd
import numpy  as nu
fd = os.open( "simple_edit.dat", os.O_RDWR|os.O_CREAT )

os.write(fd,"it is my message")
print(fd)