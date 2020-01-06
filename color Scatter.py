# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:36:53 2019

@author: libozhang
"""

import numpy as np

from bokeh.plotting import figure, show, output_file

N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+x, 30+2*y)
]
line_colors=[
        "#%02x%02x%02x" % (int(r), int(g), 255) for r, g in zip(150+x, 150+y)
        ]

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.5,
          line_color=line_colors)

output_file("color_scatter.html", title="color_scatter.py example")
print(colors[:10])
show(p)  # open a browser