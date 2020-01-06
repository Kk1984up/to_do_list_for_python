# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:25:04 2019

@author: libozhang
"""

import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show
import xlrd as xr
import xlwt as xw

workbook=xr.open_workbook(r'd:\\python\\ad.xlsx')
print(workbook.sheet_names())
sheet1=workbook.sheet_by_name('Sheet1')
nrows=sheet1.nrows
ncols=sheet1.ncols
print(nrows,ncols)
adc=[]
for i in range(392):
    adc.append(sheet1.cell(i,0).value)
pressure=[]
for i in range(54):
    pressure.append(sheet1.cell(i,2).value)
for i in range(169):
    pressure.append(sheet1.cell(53+2*i,2).value)
    
print(pressure)

x=np.linspace(0,200,201)
y1=adc[0:201]
y2=pressure[0:201]
p = figure(
   title="Pressure_adc",
   x_axis_label='time', y_axis_label='adc')

# add some renderers
p.line(x, y1, legend="化疗泵压力传感器变化曲线",line_color="red")
p.circle(x,y1,line_color='red',fill_color='red',size=5)
p.line(x,y2,legend='换算后的压力值',line_color="blue")
p.circle(x,y2,fill_color='blue',size=2)
show(p)






