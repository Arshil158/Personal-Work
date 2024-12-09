
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [11.07474, 13.455235, 16.347414999999998, 19.86126, 24.1304, 29.317185000000002, 35.618854999999996, 43.275059999999996, 52.576955, 63.878275, 77.60879, 94.29064, 114.55825, 139.18234999999999, 169.0993, 205.44684999999998, 249.6073, 303.25995, 368.4451, 447.6417, 543.86145, 660.7634, 802.79325, 975.3524, 1185.0025],
}
xedges = {
    'Rivet.yoda' : [10.0, 12.14948, 14.76099, 17.93384, 21.78868, 26.47212, 32.16225, 39.07546, 47.47466, 57.67925, 70.0773, 85.14028, 103.441, 125.6755, 152.6892, 185.5094, 225.3843, 273.8303, 332.6896, 404.2006, 491.0828, 596.6401, 724.8867, 880.6998, 1070.005, 1300.0],
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
        [1.0747400000000003, 1.3057549999999996, 1.586425000000002, 1.927419999999998, 2.3417199999999987, 2.845064999999998, 3.4566050000000033, 4.199600000000004, 5.102295000000005, 6.199024999999992, 7.531490000000005, 9.150360000000006, 11.117249999999999, 13.506850000000014, 16.4101, 19.937450000000013, 24.223000000000013, 29.42964999999998, 35.755499999999984, 43.441100000000006, 52.77864999999997, 64.12329999999997, 77.90655000000004, 94.65260000000012, 114.99749999999995],
        [1.0747400000000003, 1.3057549999999996, 1.5864249999999984, 1.9274200000000015, 2.3417200000000022, 2.8450650000000017, 3.456604999999996, 4.199599999999997, 5.102294999999998, 6.199024999999999, 7.531490000000005, 9.150359999999992, 11.117249999999999, 13.506849999999986, 16.4101, 19.937449999999984, 24.223000000000013, 29.42964999999998, 35.75550000000004, 43.441100000000006, 52.77864999999997, 64.12330000000009, 77.90654999999992, 94.6526, 114.99749999999995],
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