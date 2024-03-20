import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data = [np.random.normal(0, std, size=100) for std in range(1, 4)]

# Create a boxplot
fig, ax = plt.subplots()
bp = ax.boxplot(data)

# Get the width of the first box
box = bp['boxes'][0]
# width = box.get_xdata()[1] - box.get_xdata()[0]
box_width = box.get_bbox().width

for i in range(len(data)):
    median = bp['medians'][i].get_ydata()[0]
    ax.annotate(text=f'{median:.1f}',
                xy=(i+1, median),
                xytext=(-0.5, 0.3),
                textcoords='offset fontsize',
                fontsize=box_width*20)

print(f'The width of the first box is {box_width}')
plt.show()
