# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:13:13 2019

@author: libozhang
"""

from bokeh.plotting import figure,show,output_file
from bokeh.models import BoxAnnotation
from bokeh.layouts import gridplot
from bokeh.models.widgets import Panel,Tabs
import numpy as np
import pandas as pd
import xlrd as rd
import xlwt as wt

data_source=rd.open_workbook(r"d:/python/data/化疗泵压力传感器数据分析.xlsx")
sheet_unclamped=data_source.sheet_by_name('未装药盒时')
sheet_exhaust=data_source.sheet_by_name("排气时")
sheet_speed5=data_source.sheet_by_name("5ml每h")
sheet_speed50=data_source.sheet_by_name("50ml每h")

time=np.arange(0,13,0.1)
unclamped_adc=[]
unclamped_p=[]
for i in range(130):
    unclamped_adc.append(sheet_unclamped.cell(i,0).value)
    unclamped_p.append(sheet_unclamped.cell(i,1).value)

exhaust_adc=[]
exhaust_p=[]
for i in range(130):
    exhaust_adc.append(sheet_exhaust.cell(i,0).value)
    exhaust_p.append(sheet_exhaust.cell(i,1).value)
speed5_adc=[]
speed5_p=[]
for i in range(130):
    speed5_adc.append(sheet_speed5.cell(i,0).value)
    speed5_p.append(sheet_speed5.cell(i,1).value)
speed50_adc=[]
speed50_p=[]
for i in range(150,280):
    speed50_adc.append(sheet_speed50.cell(i,0).value)
    speed50_p.append(sheet_speed50.cell(i,1).value)




p1=figure(toolbar_location="above",plot_width=1080,plot_height=540)
p1.title.text="不同状态下，压力传感器采集的信号"
p1.title.align="left"
p1.title.text_color="orange"
p1.title.text_font_size="20px"
#p1.title.background_fill_color="#aaaaee"
p1.circle(time,unclamped_adc,fill_color="grey",legend="未装药盒时",size=2)
p1.line(time,exhaust_adc,line_color="black",legend="排气时",line_width=2)
p1.line(time,speed5_adc,line_dash="dotted",line_color="red",legend="5ml/h")
p1.triangle(time,speed5_adc,size=4,color="red",alpha=0.5,legend="5ml/h")
p1.square(time,speed50_adc,fill_color="purple",legend="50ml/h")
p1.line(time,speed50_adc,line_dash="dotted",line_color="purple",legend="50ml/h")

low_box=BoxAnnotation(top=50,fill_alpha=0.1,fill_color="gray")
mid_box=BoxAnnotation(bottom=50,top=700,fill_alpha=0.1,fill_color="red")
high_box=BoxAnnotation(bottom=700,fill_alpha=0.1,fill_color="gray")
p1.add_layout(low_box)
p1.add_layout(mid_box)
p1.add_layout(high_box)

p1.xaxis.axis_label="Time(s)"
p1.yaxis.axis_label="ADC(mv)"

tab1=Panel(child=p1,title="采集的ADC信号")

p2=figure(toolbar_location="above",plot_width=1080,plot_height=540)
p2.title.text="不同状态下,检测到的压力值"
p2.title.align="left"
p2.title.text_color="orange"
p2.title.text_font_size="20px"
p2.title.background_fill_color="#aaaaee"
p2.circle(time,unclamped_p,fill_color="grey",size=2,legend="未装药盒时")
p2.line(time,exhaust_p,line_color="black",legend="排气时")
p2.triangle(time,speed5_p,size=4,color="red",alpha=0.5,legend="5ml/h")
p2.line(time,speed5_p,line_dash="dotted",line_color="red",legend="5ml/h")
p2.square(time,speed50_p,color="purple",alpha=0.5,legend="50ml/h")
p2.line(time,speed50_p,line_dash="dotted",line_color="purple",legend="50ml/h")


low_box=BoxAnnotation(top=-170,fill_alpha=0.1,fill_color="red")
mid_box=BoxAnnotation(bottom=-170,top=0,fill_alpha=0.1,fill_color="green")
high_box=BoxAnnotation(bottom=0,fill_alpha=0.1,fill_color="red")
p2.add_layout(low_box)
p2.add_layout(mid_box)
p2.add_layout(high_box)

p2.xaxis.axis_label="Time(s)"
p2.yaxis.axis_label="Pressure(kpa)"
tab2=Panel(child=p2,title="检测的压力值")

output_file("压力传感器采集的信号&压力值.html")
tabs=Tabs(tabs=[tab1,tab2])

show(tabs)

