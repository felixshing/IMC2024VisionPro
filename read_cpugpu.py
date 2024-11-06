import numpy as np
from config import plot,FONT_SIZE,LABEL_SIZE,LEGEND_FONT_SIZE,LINE_WIDTH,color,marker,marker_size
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
import os
import statistics as s
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
fig, ax1 = plt.subplots()
num_samples = 5
labels = ['2', '3', '4', '5']
index = 1



data = np.load("cpu_scalability.npy")
data_gpu = np.load("gpu_scalability.npy")

ax1.set_xlim([0.8, 2.8])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_ylabel('Time (ms)', fontsize=LABEL_SIZE)
ax1.set_xlabel('# of Users', fontsize=LABEL_SIZE)

ax1.set_yticks([2, 4, 6, 8, 10])
ax1.set_ylim([3, 10.1])
ax1.tick_params(axis='x', labelsize=FONT_SIZE)
ax1.tick_params(axis='y', labelsize=FONT_SIZE)

ax1.boxplot(data, labels=labels, positions=[1,1.5,2,2.5],showmeans=True, showfliers=False, widths=0.12,
                capprops={'linewidth': '5'}, whis=(5, 95), 
                meanprops={'linewidth': '5', 'marker': 'o', 'markersize': '28', 'markerfacecolor': 'blue'},  # Color for mean marker
                # flierprops={"markersize": '30', "markerfacecolor": "red"},
                # whiskerprops={'linewidth': '15'},
                medianprops={'linewidth': '8', 'color': 'red'},  # Color for median line
                boxprops={'linewidth': '5'}
                )
ax1.grid(axis='y')

ax2 = ax1.twinx() 
ax2.set_ylim([3, 10.1])
ax2.set_yticks([])
boxplot = ax2.boxplot(data_gpu, labels=labels, positions=[1.2,1.7,2.2,2.7], showmeans=True, showfliers=False, widths=0.12,
            capprops={'linewidth': '5'}, whis=(5, 95), 
            meanprops={'linewidth': '5', 'marker': 'o', 'markersize': '28', 'markerfacecolor': 'blue'},  # Color for mean marker
            # flierprops={"markersize": '30', "markerfacecolor": "red"},
            # whiskerprops={'linewidth': '15'},
            medianprops={'linewidth': '8', 'color': 'red'},  # Color for median line
            boxprops={'linewidth': '5'},
            patch_artist=True
            )

for box in boxplot["boxes"]:
    box.set_edgecolor('black')
    box.set_facecolor('white')
    box.set_hatch(hatch='/')
import matplotlib.patches as mpatches

legend_patches = [
    mpatches.Patch(edgecolor='black', facecolor='white', hatch=s * 1, label=l)
    for s, l in zip(['', '/'], ["CPU", "GPU"])
]
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
legend = ax1.legend(handles=legend_patches, loc="upper center", ncol=4, bbox_to_anchor=(0.515, 1.05),fontsize=FONT_SIZE)
labels2 = ['     2', '    3', '    4', '    5', '', '', '', '']

ax1.set_xticklabels(labels2, fontsize=FONT_SIZE, rotation=0)
plt.subplots_adjust(left=0.22, bottom=0.18, right=0.97, top=0.92)

plt.show()
