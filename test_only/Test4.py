import matplotlib.pyplot as plt
import numpy as np

# Random data
np.random.seed(10)
data1 = np.random.normal(100, 20, 200)
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(90, 25, 200)

data = [data1, data2, data3]

fig = plt.figure(figsize=(10, 7))

# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot(data)

\
# This loop places an annotation at the position of the median for each boxplot
for i in range(len(data)):
    median = bp['medians'][i].get_ydata()[0]
    ax.annotate(text=f'{median:.1f}',
                xy=(i+1, median),
                xytext=(-0.5, 0.2),
                textcoords='offset fontsize',
                fontsize='xx-small')

plt.show()
