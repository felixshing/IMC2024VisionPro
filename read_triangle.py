from config import plot,FONT_SIZE,LABEL_SIZE,LEGEND_FONT_SIZE,LINE_WIDTH,color,marker,marker_size
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
import os
import statistics as s
import numpy as np
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
fig, ax1 = plt.subplots()
num_samples = 5
labels = ['2', '3', '4', '5']
index = 1


data = np.load("triangle_scalability.npy")
ax1.set_xlim([0.8, 2.8])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# ax1.set_ylabel(user)
ax1.set_ylabel('# of Triangles', fontsize=LABEL_SIZE)
ax1.set_xlabel('# of Users', fontsize=LABEL_SIZE)

ax1.set_yticks([100000, 200000, 300000], ["100K", "200K", "300K"])
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
plt.subplots_adjust(left=0.22, bottom=0.18, right=0.97, top=0.92)

plt.show()
