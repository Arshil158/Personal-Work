
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [0.06283185, 0.18849554999999998, 0.31415925, 0.43982295, 0.56548665, 0.69115035, 0.8168140500000001, 0.94247795, 1.0681414999999999, 1.193805, 1.319469, 1.4451325000000002, 1.570796, 1.69646, 1.822124, 1.9477875, 2.0734510000000004, 2.199115, 2.3247785, 2.450442, 2.5761060000000002, 2.70177, 2.8274334999999997, 2.9530969999999996, 3.078761],
}
xedges = {
    'Rivet.yoda' : [0.0, 0.1256637, 0.2513274, 0.3769911, 0.5026548, 0.6283185, 0.7539822, 0.8796459, 1.00531, 1.130973, 1.256637, 1.382301, 1.507964, 1.633628, 1.759292, 1.884956, 2.010619, 2.136283, 2.261947, 2.38761, 2.513274, 2.638938, 2.764602, 2.890265, 3.015929, 3.141593],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
xerrs = {
    'Rivet.yoda' : [
        [0.06283185, 0.06283185, 0.06283185000000002, 0.06283184999999997, 0.06283185000000002, 0.06283185000000002, 0.06283184999999991, 0.06283204999999992, 0.06283150000000015, 0.062832, 0.062832, 0.06283149999999993, 0.062832, 0.062832, 0.062832, 0.06283150000000015, 0.06283199999999978, 0.06283200000000022, 0.06283150000000015, 0.06283200000000022, 0.06283199999999978, 0.06283200000000022, 0.06283150000000015, 0.06283200000000022, 0.06283199999999978],
        [0.06283185, 0.06283185, 0.06283185000000002, 0.06283184999999997, 0.06283185000000002, 0.06283185000000002, 0.06283185000000002, 0.06283205000000003, 0.06283149999999993, 0.062832, 0.062832, 0.06283150000000015, 0.062832, 0.062832, 0.062832, 0.06283149999999993, 0.06283200000000022, 0.06283199999999978, 0.06283149999999971, 0.06283199999999978, 0.06283200000000022, 0.06283199999999978, 0.06283149999999971, 0.06283199999999978, 0.06283200000000022],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}