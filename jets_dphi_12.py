#! /usr/bin/env python

# This Python script was auto-generated using YODA v2.0.1.
# Analysis object: /MC_JETS/jets_dphi_12
# Timestamp: 09-12-2024 (22:26:02)

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg') # comment out for interactive use
import os
import numpy as np

plotDir = os.path.split(os.path.realpath(__file__))[0]
if 'YODA_USER_PLOT_PATH' in globals():
    plot_outdir = globals()['YODA_USER_PLOT_PATH']
else:
    plot_outdir = plotDir

#plot style
plt.style.use(os.path.join(plotDir, '../default.mplstyle'))
# plot metadata
figW, figH = plt.rcParams['figure.figsize']
ax_xLabel = r'$\Delta\phi(\mathrm{jet~1,~jet~2})$'
ax_yLabel = r'$\mathrm{d}\sigma/\mathrm{d}\Delta\phi(\mathrm{jet~1,~jet~2})$ [pb]'
ax_title  = r'Azimuthal separation between jets'
ax_xScale = 'linear'
ax_yScale = 'linear'
xLims = (0.0, 3.141593)
yLims = (0.11, 1.0)

# TeX-friendly labels for the legend
labels = {
    'legend' : ([ r"Rivet" ], r""),
}

# Adjust canvas width and height
canvasW = 10.0
canvasH = 9.0
figW *= canvasW/10.
figH *= canvasH/9.

# Create figure and axis objects
fig, (ax, ratio0_ax) = plt.subplots(2, 1, sharex=True,
                  figsize=(figW,figH), gridspec_kw={'height_ratios': (6.0, 3.0)})

# Set figure margins
plt.subplots_adjust(
    left   = 1.0 * plt.rcParams['figure.subplot.left'],
    right  = 1.0 * plt.rcParams['figure.subplot.right'],
    top    = 1.0 * plt.rcParams['figure.subplot.top'],
    bottom = 1.0 * plt.rcParams['figure.subplot.bottom'])

ratio0_ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
ratio0_ax.set_ylim(0.5, 1.4999)
ratio0_ax.set_ylabel('Ratio')

# the numerical data is stored in a separate file
dataf = dict()
prefix = os.path.split(__file__)[0]
if prefix:    prefix = prefix + '/'
exec(open(prefix+'jets_dphi_12__data.py').read(), dataf)


legend_handles = dict() # keep track of handles for the legend

# style options for curves
# starts at zorder>=5 to draw curve on top of legend
styles = {
  'Rivet.yoda': {
    'color' : '#EE3311',
    'linestyle' : '-',
    'linewidth' : 1,
    'marker' : 'none',
    'markersize' : 2,
    'capsize' : 0.0,
    'zorder' : 5,
    'histstyle' : 1,
    'drawstyle' : 'steps-pre',
    'xerrorbars' : 1,
    'yerrorbars' : 1,
    'fillcolor' : None,
    'fillopacity' : 1.0,
    'ratio0_linestyle' : '-',
    'ratio0_linewidth' : 1,
    'ratio0_marker' : 'none',
    'ratio0_markersize' : 2,
    'ratio0_capsize' : 0.0,
    'ratio0_zorder' : 5,
    'ratio0_histstyle' : 1,
    'ratio0_drawstyle' : 'steps-pre',
    'ratio0_xerrorbars' : 1,
    'ratio0_yerrorbars' : 1,
  },
}

# curve from input yoda files in main panel
for label, yvals in dataf['yvals'].items():
    if all(np.isnan(v) for v in dataf['yvals'][label]):
        continue
    tmp = None
    if styles[label]['histstyle']: # draw as histogram
        xpos = dataf['xedges'][label] if styles[label]['drawstyle'] else dataf['xpoints'][label]
        ypos = np.insert(yvals, 0, yvals[0]) if styles[label]['drawstyle'] else yvals
        if styles[label]['fillcolor']: # fill area below curve
            ax.fill_between(xpos, ypos, step='pre',
                            color=styles[label]['fillcolor'],
                            alpha=styles[label]['fillopacity'])
        tmp, = ax.plot(xpos, ypos,
                       color=styles[label]['color'],
                       linestyle=styles[label]['linestyle'],
                       linewidth=styles[label]['linewidth'],
                       drawstyle=styles[label]['drawstyle'], solid_joinstyle='miter',
                       zorder=styles[label]['zorder'], label=label)
    tmp = ax.errorbar(dataf['xpoints'][label], yvals,
                      xerr=np.array(dataf['xerrs'][label])*styles[label]['xerrorbars'],
                      yerr=np.array(dataf['yerrs'][label])*styles[label]['yerrorbars'],
                      fmt=styles[label]['marker'], capsize=styles[label]['capsize'],
                      markersize=styles[label]['markersize'],
                      ecolor=styles[label]['color'],
                      color=styles[label]['color'], zorder=styles[label]['zorder'])
    tmp[-1][0].set_linestyle(styles[label]['linestyle'])
    tmp[-1][0].set_linewidth(styles[label]['linewidth'])
    if label in dataf['add_legend_handle']:  legend_handles[label] = tmp
    for varLabel in dataf['variation_yvals'].keys():
        if varLabel.startswith(label):
            tmp, = ax.plot(dataf['xedges'][label], dataf['variation_yvals'][varLabel],
                           color=styles[label]['color'],
                           linestyle=styles[label]['linestyle'],
                           linewidth=styles[label]['linewidth'],
                           drawstyle='steps-pre', solid_joinstyle='miter',
                           zorder=styles[label]['zorder'], alpha=0.5)


# plots on ratio panel
# curve from input yoda files in ratio panel
for label, yvals in dataf['ratio0_yvals'].items():
    if all(np.isnan(v) for v in yvals):
        continue
    if styles[label]['ratio0_histstyle']: # plot as histogram
        xpos = dataf['xedges']['Rivet.yoda'] if styles[label]['ratio0_drawstyle'] else dataf['xpoints']['Rivet.yoda']
        ypos = np.insert(yvals, 0, yvals[0]) if styles[label]['ratio0_drawstyle'] else yvals
        ratio0_ax.plot(xpos, ypos,
                       color=styles[label]['color'],
                       linewidth=styles[label]['linewidth'],
                       linestyle=styles[label]['ratio0_linestyle'],
                       drawstyle=styles[label]['ratio0_drawstyle'], zorder=styles[label]['zorder'],
                       solid_joinstyle='miter')
    tmp = ratio0_ax.errorbar(dataf['xpoints']['Rivet.yoda'], yvals,
                             xerr=np.array(dataf['ref_xerrs'])*styles[label]['ratio0_xerrorbars'],
                             yerr=np.array(dataf['ratio0_yerrs'][label])*styles[label]['ratio0_yerrorbars'],
                             fmt=styles[label]['ratio0_marker'], capsize=styles[label]['ratio0_capsize'],
                             markersize=styles[label]['ratio0_markersize'],
                             ecolor=styles[label]['color'],
                             color=styles[label]['color'])
    tmp[-1][0].set_linestyle(styles[label]['ratio0_linestyle'])
    tmp[-1][0].set_linewidth(styles[label]['ratio0_linewidth'])

    for varlabel in dataf['ratio0_variation_vals'].keys():
        if varlabel.startswith(label):
            ratio0_ax.plot(dataf['xedges']['Rivet.yoda'],
                            dataf['ratio0_variation_vals'][varlabel],
                            color=styles[label]['color'],
                            linestyle=styles[label]['linestyle'],
                            linewidth=styles[label]['linewidth'],
                            drawstyle='steps-pre', solid_joinstyle='miter',
                            zorder=1, alpha=0.5)

legend_items = list(legend_handles.values())
ax.add_artist(ax.legend(legend_items,
                        labels['legend'][0],
                        title=labels['legend'][1],
                        alignment='left',
                        loc='upper center',
                        bbox_to_anchor=(0.5, 0.97)))

# set plot metadata as defined above
ratio0_ax.set_xlabel(ax_xLabel)
ratio0_ax.xaxis.set_label_coords(1., -0.15)
ax.set_ylabel(ax_yLabel, ha='right', va='top')
ax.yaxis.set_label_coords(-0.11, 1.0)
ax.set_title(ax_title, loc='left')
ax.set_xscale(ax_xScale)
ax.set_yscale(ax_yScale)
ax.set_xlim(xLims)
ax.set_ylim(yLims)

# tick formatting
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
ax.yaxis.set_major_locator(mpl.ticker.LogLocator(base=10.0, numticks=np.inf))
ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(
                           base=10.0, subs=np.arange(0.1, 1, 0.1), numticks=np.inf))
fig.align_ylabels((ax, ratio0_ax))
plt.savefig(os.path.join(plot_outdir, 'jets_dphi_12.pdf'), format='PDF')
plt.savefig(os.path.join(plot_outdir, 'jets_dphi_12.png'), format='PNG')

plt.close(fig)