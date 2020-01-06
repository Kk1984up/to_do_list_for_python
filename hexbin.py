# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:48:35 2019

@author: libozhang
"""


import numpy as np

from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure

n = 5000
x = 5+3*np.random.standard_normal(n)
y = 6+3*np.random.standard_normal(n)

p = figure(title="Hexbin for 1000 points", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154')
p.grid.visible = False

r,bin= p.hexbin(x, y, size=1, hover_color="pink", hover_alpha=0.8)

p.diamond_cross(x, y, color="white", size=0.5)

p.add_tools(HoverTool(
    tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
    mode="mouse", point_policy="follow_mouse", renderers=[r]
))

output_file("hexbin.html")

show(p)