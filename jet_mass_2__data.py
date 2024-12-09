
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [1.0482390000000001, 1.149371, 1.2602605, 1.3818485, 1.5151665, 1.6613470000000001, 1.821631, 1.9973785, 2.1900820000000003, 2.401377, 2.6330575, 2.8870905000000002, 3.1656315, 3.471046, 3.8059265, 4.173115, 4.5757295, 5.017188, 5.501237, 6.031986, 6.6139415, 7.2520430000000005, 7.951707000000001, 8.718873, 9.560054000000001, 10.482389999999999, 11.49371, 12.602605, 13.818484999999999, 15.151665, 16.61347, 18.21631, 19.973785, 21.90082, 24.01377, 26.330575000000003, 28.870905, 31.656315, 34.71046, 38.059265, 41.73115, 45.757295, 50.17188, 55.012370000000004, 60.319860000000006, 66.139415, 72.52043, 79.51706999999999, 87.18872999999999, 95.60054],
}
xedges = {
    'Rivet.yoda' : [1.0, 1.096478, 1.202264, 1.318257, 1.44544, 1.584893, 1.737801, 1.905461, 2.089296, 2.290868, 2.511886, 2.754229, 3.019952, 3.311311, 3.630781, 3.981072, 4.365158, 4.786301, 5.248075, 5.754399, 6.309573, 6.91831, 7.585776, 8.317638, 9.120108, 10.0, 10.96478, 12.02264, 13.18257, 14.4544, 15.84893, 17.37801, 19.05461, 20.89296, 22.90868, 25.11886, 27.54229, 30.19952, 33.11311, 36.30781, 39.81072, 43.65158, 47.86301, 52.48075, 57.54399, 63.09573, 69.1831, 75.85776, 83.17638, 91.20108, 100.0],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
xerrs = {
    'Rivet.yoda' : [
        [0.04823899999999992, 0.05289300000000008, 0.057996500000000006, 0.06359150000000002, 0.06972650000000002, 0.0764539999999998, 0.08383000000000007, 0.0919175000000001, 0.10078599999999982, 0.11050899999999997, 0.12117149999999999, 0.13286149999999974, 0.14567949999999996, 0.15973499999999996, 0.17514550000000018, 0.19204299999999996, 0.21057150000000036, 0.23088700000000006, 0.25316200000000055, 0.2775870000000005, 0.3043684999999998, 0.3337329999999996, 0.3659309999999998, 0.4012349999999998, 0.43994599999999906, 0.48239000000000054, 0.5289300000000008, 0.5799649999999996, 0.6359150000000007, 0.6972649999999998, 0.7645400000000002, 0.8383000000000003, 0.9191749999999992, 1.0078600000000009, 1.1050900000000006, 1.211714999999998, 1.3286149999999992, 1.4567949999999996, 1.5973500000000058, 1.751455, 1.9204300000000032, 2.1057150000000036, 2.308869999999999, 2.5316199999999967, 2.7758699999999976, 3.0436849999999964, 3.3373299999999944, 3.659310000000005, 4.012350000000012, 4.399460000000005],
        [0.04823900000000014, 0.05289299999999986, 0.057996500000000006, 0.06359150000000002, 0.06972650000000002, 0.07645400000000002, 0.08383000000000007, 0.09191749999999987, 0.10078600000000026, 0.11050899999999997, 0.12117149999999999, 0.1328615000000002, 0.14567949999999996, 0.15973499999999996, 0.17514550000000018, 0.19204299999999996, 0.21057149999999947, 0.23088700000000006, 0.25316199999999967, 0.2775869999999996, 0.3043684999999998, 0.3337330000000005, 0.3659310000000007, 0.4012349999999998, 0.43994600000000084, 0.48238999999999876, 0.5289300000000008, 0.5799649999999996, 0.6359149999999989, 0.6972649999999998, 0.7645400000000002, 0.8383000000000003, 0.9191749999999992, 1.0078600000000009, 1.1050900000000006, 1.2117150000000017, 1.3286149999999992, 1.4567949999999996, 1.5973499999999987, 1.751455, 1.920429999999996, 2.1057149999999965, 2.308869999999999, 2.5316200000000038, 2.7758700000000047, 3.0436849999999964, 3.3373300000000086, 3.6593099999999907, 4.012349999999998, 4.399459999999991],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}