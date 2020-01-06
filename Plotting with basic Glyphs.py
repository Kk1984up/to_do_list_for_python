# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:48:35 2019

@author: libozhang
"""

from bokeh.plotting import figure,output_file,show
from bokeh.models import ColumnDataSource,CustomJS,Slider
from bokeh.util.hex import axial_to_cartesian
from bokeh.io import output_file,show
from bokeh.layouts import gridplot,grid,column
from math import pi
import numpy as np
import pandas as pd

output_file('layout_grid.html')
s1=figure(background_fill_color="#fafafa")
          
#add a circle renderer with a size ,color,and a alpha
s1.circle([1,2,3,4,5],[3,5,6,7,9],size=20,color="navy",alpha=0.8)
#add a square renderer with a size,color and a alpha

s2=figure(background_fill_color="#fafafa")
s2.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)

#add a line renderer with a line_width,color
s3=figure(background_fill_color="#fafafa")
s3.line([1,2,3,4,5],[6,7,9,8,4],line_width=4,color='yellow')

#add a step renderer with a line_width ,color and a mode
s4=figure(background_fill_color="#fafafa")
s4.step([1,2,3,4,5],[5,6,8,9,4],line_width=3,mode='center',color='blue')

#add a multi_line with a color ,a alpha,and a line_width
s5=figure(background_fill_color="#fafafa")
s5.multi_line([[1,2,2],[3,4,6,7]],[[2,4,5],[4,7,9,3]],color=["firebrick","red"],
             alpha=[0.3,0.6],line_width=[2,4])

#add a line with a missing point
s6=figure(background_fill_color="#fafafa")
nan=float('nan')
s6.line([1,2,3,nan,4,5],[8,4,5,5,4,9],line_width=5,color="grey")

s7=figure(background_fill_color="#fafafa")
source=ColumnDataSource(data=dict(
        x=[1,2,3,4,5],
        y1=[1,2,5,6,8],
        y2=[3,5,6,2,5]))
s7.vline_stack(['y1','y2'],x='x',source=source,line_width=[1,6],color=["black",'green'])

s8=figure(background_fill_color="#fafafa")
source1=ColumnDataSource(data=dict(
        y=[1,2,3,4,5],
        x1=[1,2,5,6,8],
        x2=[3,5,6,2,5]))
s8.hbar_stack(['x1','x2'],y='y',source=source1,height=0.8,color=("grey", "lightgrey"))

s9=figure(background_fill_color="#fafafa")
s9.quad(top=[2,3,4],bottom=[1,2,3],left=[1,2,3],right=[1.2,3.2,3.5],color="#B3DE69",
        legend="some_new")

s9.rect(x=[1,2,3],y=[2,4,5],width=0.5,height=30,color="#CAB2D6",
       angle=pi/3,height_units="screen",legend="some_old")
s9.legend.location="bottom_right"


q=np.array([0,0,0,-1,-1,-1,1,1,1])
r=np.array([0,-1,1,0,1,-1,0,-1,1])

s10=figure(plot_width=480,plot_height=480,toolbar_location=None)
s10.grid.visible=False
s10.hex_tile(q,r,size=1,fill_color=["firebrick"]*4+["navy"]*5,
            line_color="black",alpha=0.4)
x,y=axial_to_cartesian(q,r,1,"pointytop")
s10.text(x,y,text=['(%d,%d)'%(q,r)for(q,r) in zip(q,r)],
                  text_baseline="top",text_align="center")

tools = 'pan'


def bollinger():
    # Define Bollinger Bands.
    upperband = np.random.randint(100, 150+1, size=100)
    lowerband = upperband - 100
    x_data = np.arange(1, 101)

    # Bollinger shading glyph:
    band_x = np.append(x_data, x_data[::-1])
    band_y = np.append(lowerband, upperband[::-1])

    p = figure(x_axis_type='datetime', tools=tools)
    p.patch(band_x, band_y, color='#7570B3', fill_alpha=0.2)

    p.title.text = 'Bollinger Bands'
    p.title_location = 'left'
    p.title.align = 'left'
    p.plot_height = 240
    p.plot_width = 240
    p.grid.grid_line_alpha = 0.4
    return [p]


def slider():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    source = ColumnDataSource(data=dict(x=x, y=y))

    plot = figure(
        y_range=(-10, 10), tools='', toolbar_location=None,
        title="Sliders example")
    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    amp_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
    freq_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
    phase_slider = Slider(start=0, end=6.4, value=0, step=.1, title="Phase")
    offset_slider = Slider(start=-5, end=5, value=0, step=.1, title="Offset")

    callback = CustomJS(args=dict(source=source, amp=amp_slider, freq=freq_slider, phase=phase_slider, offset=offset_slider),
                        code="""
        const data = source.data;
        const A = amp.value;
        const k = freq.value;
        const phi = phase.value;
        const B = offset.value;
        const x = data['x']
        const y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = B + A*Math.sin(k*x[i]+phi);
        }
        source.change.emit();
    """)

    amp_slider.js_on_change('value', callback)
    freq_slider.js_on_change('value', callback)
    phase_slider.js_on_change('value', callback)
    offset_slider.js_on_change('value', callback)

    widgets = column(amp_slider, freq_slider, phase_slider, offset_slider)
    return [widgets, plot]


def linked_panning():
    N = 100
    x = np.linspace(0, 4 * np.pi, N)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + np.cos(x)

    s11 = figure(tools=tools)
    s11.circle(x, y1, color="navy", size=8, alpha=0.5)
    s11.ygrid.band_fill_color="orange"
    s11.ygrid.band_fill_alpha=0.1
    s12 = figure(tools=tools, x_range=s1.x_range, y_range=s1.y_range)
    s12.circle(x, y2, color="firebrick", size=8, alpha=0.5)
    s13 = figure(tools='pan, box_select', x_range=s1.x_range)
    s13.circle(x, y3, color="olive", size=8, alpha=0.5)
    s13.xaxis.axis_label="x_value"
    s13.xaxis.axis_line_width=3
    s13.xaxis.axis_line_color="red"
    s13.xaxis.major_label_text_color="blue"
    s13.xaxis.major_tick_line_color="firebrick"
    s13.xaxis.major_tick_line_width=3
    s13.xaxis.minor_tick_line_color="orange"
    s13.ygrid.minor_grid_line_color="navy"
    s13.ygrid.minor_grid_line_alpha=0.1
    s13.xaxis.major_label_orientation = pi/4
    
    
    return [s11, s12, s13]

l = grid([
    bollinger(),
    slider(),
    linked_panning(),
], sizing_mode='stretch_both')


#make a grid
grid=gridplot([[s1,s2,s3,s4],[s5,s6,s7,s8],[s9,s10,l,None]]
,plot_width=240,plot_height=240)
#show the results
show(grid)