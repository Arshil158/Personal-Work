
import numpy as np
from numpy import nan

add_legend_handle = [
    'Rivet.yoda'
]

xpoints = {
    'Rivet.yoda' : [10.83399, 12.641075, 14.749575, 17.20977, 20.08032, 23.42967, 27.337685, 31.897545, 37.21798, 43.425855, 50.669185, 59.120684999999995, 68.98187999999999, 80.4879, 93.913085, 109.57755, 127.85485, 149.18075, 174.06375, 203.0972, 236.97335, 276.49995, 322.6195, 376.4317, 439.2196, 512.4804, 597.96095, 697.6994500000001, 814.0741, 949.8598, 1108.2939999999999, 1293.155, 1508.8505],
}
xedges = {
    'Rivet.yoda' : [10.0, 11.66798, 13.61417, 15.88498, 18.53456, 21.62608, 25.23326, 29.44211, 34.35298, 40.08298, 46.76873, 54.56964, 63.67173, 74.29203, 86.68377, 101.1424, 118.0127, 137.697, 160.6645, 187.463, 218.7314, 255.2153, 297.7846, 347.4544, 405.409, 473.0302, 551.9306, 643.9913, 751.4076, 876.7406, 1022.979, 1193.609, 1392.701, 1625.0],
}
ref_xerrs = [
  [abs(xpoints['Rivet.yoda'][i]   - xedges['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))],
  [abs(xedges['Rivet.yoda'][i+1] - xpoints['Rivet.yoda'][i]) for i in range(len(xpoints['Rivet.yoda']))]
]

yvals = {
    'Rivet.yoda' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
xerrs = {
    'Rivet.yoda' : [
        [0.83399, 0.9730949999999989, 1.1354050000000004, 1.3247900000000001, 1.5457600000000014, 1.8035899999999998, 2.104424999999999, 2.4554350000000014, 2.865000000000002, 3.3428749999999994, 3.900455000000001, 4.551045000000002, 5.310150000000007, 6.195869999999999, 7.229315, 8.435149999999993, 9.842150000000004, 11.483750000000015, 13.399249999999995, 15.634200000000021, 18.241950000000003, 21.28465, 24.834900000000005, 28.977300000000014, 33.810599999999965, 39.450199999999995, 46.03035, 53.70814999999993, 62.66649999999993, 73.11920000000009, 85.31500000000005, 99.54600000000005, 116.14949999999999],
        [0.83399, 0.9730950000000007, 1.1354050000000004, 1.3247899999999984, 1.5457600000000014, 1.8035899999999998, 2.104424999999999, 2.4554350000000014, 2.864999999999995, 3.3428749999999994, 3.900455000000001, 4.551044999999995, 5.310149999999993, 6.195869999999999, 7.229315, 8.435150000000007, 9.842150000000004, 11.483749999999986, 13.399249999999995, 15.634199999999993, 18.241950000000003, 21.28465, 24.834900000000005, 28.977299999999957, 33.81060000000002, 39.45020000000005, 46.03035, 53.708150000000046, 62.66650000000004, 73.11919999999998, 85.31499999999983, 99.54600000000005, 116.14949999999999],
    ],
}
yerrs = {
    'Rivet.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Rivet.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'Rivet.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}