
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [0.16666665, 0.5, 0.83333335, 1.1666665, 1.5, 1.8333335, 2.1666665, 2.5, 2.8333335, 3.1666665, 3.5, 3.8333335, 4.1666665, 4.5, 4.8333335],
}
xedges = {
    'Rivet.yoda' : [0.0, 0.3333333, 0.6666667, 1.0, 1.333333, 1.666667, 2.0, 2.333333, 2.666667, 3.0, 3.333333, 3.666667, 4.0, 4.333333, 4.666667, 5.0],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
xerrs = {
    'Rivet.yoda' : [
        [0.16666665, 0.16666669999999995, 0.16666665000000003, 0.16666650000000005, 0.1666669999999999, 0.16666650000000005, 0.16666650000000027, 0.1666669999999999, 0.16666649999999983, 0.16666650000000027, 0.1666669999999999, 0.16666649999999983, 0.16666649999999983, 0.16666700000000034, 0.16666649999999983],
        [0.16666665, 0.1666667, 0.16666665000000003, 0.16666650000000005, 0.1666669999999999, 0.16666650000000005, 0.16666649999999983, 0.1666669999999999, 0.16666650000000027, 0.16666649999999983, 0.1666669999999999, 0.16666650000000027, 0.16666649999999983, 0.16666700000000034, 0.16666649999999983],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}