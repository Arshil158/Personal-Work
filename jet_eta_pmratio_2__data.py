
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [0.1, 0.30000000000000004, 0.5, 0.7, 0.9, 1.1, 1.2999999999999998, 1.5, 1.7000000000000002, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9, 4.1, 4.300000000000001, 4.5, 4.699999999999999, 4.9],
}
xedges = {
    'Rivet.yoda' : [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
xerrs = {
    'Rivet.yoda' : [
        [0.1, 0.09999999999999998, 0.09999999999999998, 0.10000000000000009, 0.09999999999999998, 0.09999999999999987, 0.10000000000000009, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.09999999999999964, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.09999999999999964, 0.10000000000000009, 0.10000000000000053, 0.09999999999999964, 0.09999999999999964, 0.10000000000000053, 0.09999999999999964],
        [0.1, 0.10000000000000003, 0.09999999999999998, 0.09999999999999998, 0.09999999999999998, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009, 0.09999999999999964, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.09999999999999964, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.09999999999999964, 0.10000000000000053, 0.09999999999999964, 0.09999999999999964, 0.10000000000000053],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}