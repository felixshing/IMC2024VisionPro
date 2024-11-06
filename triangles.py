import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from config import plot,FONT_SIZE,LABEL_SIZE,LEGEND_FONT_SIZE,LINE_WIDTH,color,marker,marker_size
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fig, ax1 = plt.subplots()

# Updated label order
labels = ['BL', 'D', 'F', 'V']
hatches = ['/', '', '\\', 'x']  # Different hatches for each bar
cmap = plt.get_cmap('tab10')  # 'tab10' is a good choice for 10 distinct colors
colors = cmap(np.arange(10))
# Data for each label
data = [[[78030]], [[45036]], [[21036]], [[36]]]  # Data reordered to match new labels

index = 2.0

# Iterate through each data point and plot bars with specific attributes
for i in range(len(data)):
    for j in range(len(data[i])):
        ax1.bar(index, height=np.mean(data[i][j]), yerr=np.std(data[i][j]),
                width=1, error_kw={'elinewidth': 5, 'ecolor': 'black'}, fill=True, hatch=hatches[i],
                color=colors[i], capsize=10)
        index += 2

    # Set percentage labels as per new order
    if i == 3:
        percentage_label = ">99%"
    elif i == 2:
        percentage_label = "73%"
    elif i == 1:
        percentage_label = "42%"
    else:
        percentage_label = ""  # No label for the last one
    
    # Annotate percentage labels on the bars
    if percentage_label:
        ax1.text(index - 1.5, np.mean(data[i][0]) + 0.4, percentage_label, ha='center', va='bottom', fontsize=LEGEND_FONT_SIZE)

    index += 2  # Increase index to maintain spacing

# Set x-axis tick positions and labels
xtick_index = [2, 6, 10, 14]
ax1.set_xticks(ticks=xtick_index)
ax1.set_xticklabels(labels, fontsize=LABEL_SIZE)

# Configure y-axis
ax1.set_ylabel('# of Triangles', fontsize=LABEL_SIZE)
ax1.set_yticks([0, 20000, 40000, 60000, 80000], [0, "20K", "40K", "60K", "80K"])
ax1.set_ylim([0, 81000])
ax1.set_xlim([-1, 17])

# Remove unnecessary plot borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Customize tick parameters
ax1.tick_params(axis='x', labelsize=FONT_SIZE)
ax1.tick_params(axis='y', labelsize=FONT_SIZE)

# Add gridlines for y-axis
plt.grid(axis='y')

# Adjust subplot layout
plt.subplots_adjust(left=0.22, bottom=0.18, right=0.97, top=0.92)

# Display the figure
plt.show()
