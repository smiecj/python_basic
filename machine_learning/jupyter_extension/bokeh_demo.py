import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%d%d%d" % (r, g, 150) for r, g in zip(np.floor(50 + 2*x), np.floor(30 + 2*y))]

output_notebook()

p = figure()
p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

show(p)