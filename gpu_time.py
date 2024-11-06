# @Time    : 11/01/24 3:16 PM
# @Author  : Ruizhi Cheng
# @FileName: gpu_time.py
# @Email   : rcheng4@gmu.edu
from config import plot,FONT_SIZE,LABEL_SIZE,LEGEND_FONT_SIZE,LINE_WIDTH,color,marker,marker_size
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
import os
import csv
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
fig, ax1 = plt.subplots()
num_samples = 5
label = ['V', 'F', '', 'BL']
hatch = ['/', '', '\\', 'x']  
label = ['BL', 'D', 'F', 'V']
cmap = plt.get_cmap('tab10') 
colors = cmap(np.arange(10))
models = ['JS','WASM']
index = 2.0



data = np.load("gputime.npy")

for i in range(len(data)):
    for j in range(len(data[i])):
        if i==0:
            ax1.bar(index,height=np.mean(data[i][j]),yerr =np.std(data[i][j]),
                    width = 1,error_kw={'elinewidth': 5, 'ecolor': 'black'},fill=True,hatch=hatch[i],color=colors[i], capsize=10,label=models[j])
        else:
            ax1.bar(index,height=np.mean(data[i][j]),yerr =np.std(data[i][j]),
                    width = 1,error_kw={'elinewidth': 5, 'ecolor': 'black'},fill=True,hatch=hatch[i],color=colors[i], capsize=10)
        print(np.mean(data[i][j]), np.std(data[i][j]))
        index += 2
    percentage_diff = (np.mean(data[0][0]) - np.mean(data[i][0])) / np.mean(data[0][0])
    index +=2
    if i == 0:
        continue
    if i == 0:
        ax1.text(index - 4.0, np.mean(data[i][0]), f'{percentage_diff * 100:.0f}%', ha='center', va='bottom', fontsize=LEGEND_FONT_SIZE)
    else:
        ax1.text(index - 3.5, np.mean(data[i][0]), f'{percentage_diff * 100:.0f}%', ha='center', va='bottom', fontsize=LEGEND_FONT_SIZE)

xtick_index = [2,6,10,14]
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xticks(ticks=xtick_index)
ax1.set_xticklabels(label, fontsize=LABEL_SIZE)
ax1.set_ylabel('GPU Time (ms)', fontsize=LABEL_SIZE)
ax1.set_yticks([0, 2, 4, 6, 8])
ax1.set_ylim([0, 8.1])
ax1.set_xlim([-1, 17])
ax1.tick_params(axis='x', labelsize=FONT_SIZE)
ax1.tick_params(axis='y', labelsize=FONT_SIZE)
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,1]
plt.subplots_adjust(left=0.22, bottom=0.18, right=0.97, top=0.92)
plt.grid(axis = 'y')
plt.show()