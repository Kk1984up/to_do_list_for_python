# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:25:05 2019

@author: libozhang
"""

from bokeh.plotting import figure,show,output_file

import numpy as np
import pandas as pd

SN=["A90901019",'A90901016','A81201009','A90901017','A90901002',
    'A90901009','A90901006','A90901011','A90901012','A90901013']

y1=[1.35,1.4,1.0,1.0,0.6,0.85,1.55,0.4,0.75,0.8]
y2=[0.2,0.28,0.65,0.3,0.55,0.42,0.25,0.25,0.35,0.42]
sorted_SN=sorted(SN,key=lambda x:y2[SN.index(x)])
sorted_y1=sorted(y1,key=lambda x:y2[y1.index(x)])
y2.sort()
SN=sorted_SN
y1=sorted_y1
df=pd.DataFrame({'gap':y1,'gap2':y2},index=SN)
df.to_excel('d:/python/data/化疗泵装夹到位检测.xlsx',sheet_name='sheet1')
p=figure(x_range=sorted_SN,plot_width=1080,plot_height=480)
p.title.text="'未装夹到位'报警功能测试"
p.title.align="left"
p.title.text_color="orange"
p.title.text_font_size="20px"
p.step(x=SN,y=y1,line_width=5,line_color='red',mode='center',
       legend="开始自流时的间隙")
p.circle(x=SN,y=y2,fill_color='yellow',line_color='blue',
         line_width=3,legend="报警时的间隙",size=10)
#p.ellipse(x=SN,y=y2,width=0.5,height=0.2,angle=np.pi/2,color="#CAB2D6")
p.line(x=SN,y=y2,line_dash="dotted",line_color="purple",legend="报警时的间隙")
p.xaxis.axis_label="化疗泵序列号(SN)"
p.yaxis.axis_label="泵体和药盒的间隙(mm)"
p.legend.location="top_center"
output_file("未装夹到位功能验证.html")
show(p)
