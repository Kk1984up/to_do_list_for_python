
#-*- coding: utf-8 -*-
"""
Created on Fri 12 6 20119
@Author:libozhang

"""
import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show,ColumnDataSource
from bokeh.models import BoxAnnotation,HoverTool,Span,LinearAxis, Range1d,NumeralTickFormatter,Band
from bokeh.models.widgets import Panel,Tabs
from bokeh.layouts import gridplot
from math import pi

output_file("d:/python/png/临床样品测试曲线.html")
lot=[]
for i in range(2):
      lot.append("CFA180201")
for i in range(5):
      lot.append("CFA181201")
for i in range(2):
      lot.append("CFA190301")
for i in range(20):
      lot.append("CFA190901")
sn0=np.arange(1,23,1)
index=[3,13]
sn1=np.delete(sn0,index)
sn=[2,3,4,8,9,10,11,1,2]+list(sn1)
SN=[lot[i]+str(sn[i]) for i in range(len(sn))]
Data=pd.read_excel("d:/python/data/SourceData.xlsx")

dict={'max_pressure':Data["max_pressure"],
      'current':Data["current"],
      '1.33m-':Data["1.33m-"],
      '1.33m+':Data["1.33m+"],
      "sn":SN
}
df=pd.DataFrame(dict,columns=["sn","max_pressure","current","1.33m-","1.33m+"])
df.to_excel("d:/python/data/output1206.xlsx")

source=ColumnDataSource(dict)

output_file("d:/python/png/clinic samples TestData.html")

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,\
       zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,\
       poly_select,lasso_select,"
TOOLTIPS = [
    ('index', "$index"),
    ("泵序列号", "@sn"),
    ("最大压力", "@max_pressure"),
    ("平均电流", "@current"),
    ("+1.33m时的输液精度","@1.33m+"),
    ("-1.33m时的输液精度","@1.33m-"),
]
   
p=figure(x_range=SN,y_range=(0,260),plot_width=960,plot_height=560,
         tooltips=TOOLTIPS,tools=TOOLS,title="化疗泵的极限压力")
p.line(x="sn",y="max_pressure",source=source,line_color="green",line_width=2,legend="极限压力")
p.scatter(x="sn",y="max_pressure",source=source,color="orange",size=8,line_width=2,legend="极限压力")
p.xaxis.axis_label="化疗泵序列号"
p.yaxis.axis_label="能达到的最大压力(kpa)"
p.xaxis.major_label_orientation = pi/3
p.title.align = "left"
p.title.text_color = "darkblue"
p.title.text_font_size = "25px"
tab1=Panel(child=p,title="最大压力分布")

p2=figure(x_range=SN,y_range=(200,350),plot_width=960,plot_height=560,
         tooltips=TOOLTIPS,tools=TOOLS,title="平均电流")
p2.line(x="sn",y="current",source=source,line_color="green",line_width=2,legend="平均电流")
p2.scatter(x="sn",y="current",source=source,color="orange",size=8,legend="平均电流")
p2.xaxis.axis_label="化疗泵序列号"
p2.yaxis.axis_label="平均电流(mA)"
p2.xaxis.major_label_orientation = pi/3
p2.title.align = "left"
p2.title.text_color = "darkblue"
p2.title.text_font_size = "25px"
p2.title.background_fill_color = "white"
tab2=Panel(child=p2,title="平均电流分布")


p1=figure(x_range=SN,y_range=(-0.2,0.35),plot_width=960,plot_height=560,tooltips=TOOLTIPS,
          tools=TOOLS,title="背景压下的输注精度")
p1.scatter(x="sn",y='1.33m+',color="yellow",source=source,
        size=6,legend="泵低于测试台1.33m")

p1.scatter(x="sn",y="1.33m-",color="red",source=source,
        size=6,legend="泵高于测试台1.33m")
p1.xaxis.axis_label="化疗泵序列号"
p1.yaxis.axis_label="输液精度误差"
p1.yaxis[0].formatter = NumeralTickFormatter(format="0.0%")
p1.xaxis.major_label_orientation = pi/6
p1.title.align = "left"
p1.title.text_color = "darkblue"
p1.title.text_font_size = "25px"
band = Band(base='sn', lower='1.33m-', upper='1.33m+', source=source, level='underlay',
            fill_alpha=0.2,fill_color="gray", line_width=2, line_color='gray')
p1.add_layout(band)
positive=0.05
nagetive=-0.05
start=Span(location=nagetive,dimension="width",
           line_color="red",line_dash=[10,10],line_width=1)
end=Span(location=positive,dimension="width",
         line_color="red",line_dash=[10,10],line_width=1)
p1.add_layout(start)
p1.add_layout(end)
tab3=Panel(child=p1,title="输液精度误差")
show(Tabs(tabs=[tab3,tab2,tab1]))

