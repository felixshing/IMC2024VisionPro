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
labels = ['F', 'F*', 'Z', 'W','T']
index = 1



FT = np.load("FT_tput.npy")
FT_2D = np.load("FT2d_tput.npy")
Zoom = np.load("Zoom_tput.npy")
Webex = np.load("Webex_tput.npy")
Teams = np.load("Teams_tput.npy")
FT = np.array(FT)/1000000
FT_2D = np.array(FT_2D)/1000000
Zoom = np.array(Zoom)/1000000
Webex = np.array(Webex)/1000000
Teams = np.array(Teams)/1000000
print(np.mean(FT),np.mean(FT_2D),np.mean(Zoom),np.mean(Webex),np.mean(Teams))



data = [FT,FT_2D,Zoom,Webex,Teams]

ax1.set_xlim([0.8, 3.3])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_ylabel('Throughput (Mbps)', fontsize=LABEL_SIZE)
ax1.set_yticks([1,2,3,4])
ax1.set_ylim([0,4.7])
ax1.tick_params(axis='x', labelsize=FONT_SIZE)
ax1.tick_params(axis='y', labelsize=FONT_SIZE)

ax1.boxplot(data, labels=labels, positions=[1,1.5,2,2.5,3],showmeans=True, showfliers=False, widths=0.15,
	            capprops={'linewidth': '5'}, whis=(5, 95), 
	            meanprops={'linewidth': '5', 'marker': 'o', 'markersize': '25', 'markerfacecolor': 'blue'},  # Color for mean marker
	            # flierprops={"markersize": '30', "markerfacecolor": "red"},
	            # whiskerprops={'linewidth': '15'},
	            medianprops={'linewidth': '8', 'color': 'red'},  # Color for median line
	            boxprops={'linewidth': '5'}
	            )
ax1.grid(axis='y')
plt.subplots_adjust(left=0.18)
plt.subplots_adjust(left=0.22, bottom=0.18, right=0.97, top=0.92)

plt.show()