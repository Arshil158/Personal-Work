
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
}
xedges = {
    'Rivet.yoda' : [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [0.0, nan, nan, nan, nan, nan],
}
xerrs = {
    'Rivet.yoda' : [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [nan, 0.0, 0.0, 0.0, 0.0, 0.0],
        [nan, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [1.0, nan, nan, nan, nan, nan],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [nan, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, nan],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}