import matplotlib.pyplot as plt
import numpy as np

# Create some data
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Changing color and line width of whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")

# Changing color and line width of caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)

# Changing color and line width of medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)

# Changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
               color ='#e7298a',
               alpha = 0.5)
    
# x-axis labels
ax.set_yticklabels(['data1', 'data2', 'data3'])

# Adding title
plt.title("Customized box plot")

# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# annotate median values
for i, line in enumerate(bp["medians"]):
    # get position data for median line
    x, y = line.get_xydata()[1] # top of median line
    # overlay median value
    ax.annotate(f'{y}', (x, y), xytext=(10, -5), 
                textcoords='offset points', horizontalalignment='right', 
                verticalalignment='center', fontsize=12, color='red')

plt.show()
