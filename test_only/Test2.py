import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv', header=0)

# Create a figure instance
fig = plt.figure(figsize=(10, 7))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot([df['501'], df['502'], df['503']], patch_artist=True, notch=True, vert=0, labels=['501', '502', '503'])

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

# annotate median values
for i, line in enumerate(bp["medians"]):
    # get position data for median line
    x, y = line.get_xydata()[1] # top of median line
    # overlay median value
    ax.annotate(f'{y}', (x, y), xytext=(10, -5), 
                textcoords='offset points', horizontalalignment='right', 
                verticalalignment='center', fontsize=12, color='red')

# Adding title
plt.title("Box Plots of Columns")

# show plot
plt.show()
