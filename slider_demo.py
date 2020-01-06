
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:57:54 2019

@author: libozhang
"""
import numpy as np

from bokeh.layouts import row, column
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource

x = np.linspace(-10, 10, 1000)
y = 0.2*x**2+np.random.standard_normal(1000)

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-500, 500), plot_width=640, plot_height=640)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

open_slider = Slider(start=-5, end=5, value=1, step=.1, title="open")
phase_slider = Slider(start=-20, end=20, value=1, step=.1, title="Phase")
offset_slider = Slider(start=-10, end=10, value=0, step=.1, title="Offset")

link = CustomJS(args=dict(source=source, open=open_slider, phase=phase_slider, offset=offset_slider),
                    code="""
    const data = source.data;
    const A = open.value;
    const C = offset.value;
    const B = phase.value;
    const x = data['x']
    const y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = A*x[i]**2+B*x[i]+C;
    }
    source.change.emit();
""")

open_slider.js_on_change('value', link)
phase_slider.js_on_change('value', link)
offset_slider.js_on_change('value', link)

layout = row(
    plot,
    column(open_slider,  phase_slider, offset_slider),
)

output_file("slider.html", title="slider.py example")

show(layout)