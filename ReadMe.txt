
=======================================
Building PlotFigure frame

- Controller should create a list of plots, each Plot is one item of Boxplot list
- Then Controller will pass this list of Plots to View object
- View object will handle it by placing each plot as a single widget to a single page of a QTab widget
- The function to handle the list of plot should reside inside the class of PlotFigure


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans

fig, axes = plt.subplots(3,2, squeeze=False)

for i, ax in enumerate(axes.flat):
    ax.plot([1,2])
    ax.set_title('Title ' + str(i+1))
    ax.set_xlabel('xaxis')
    ax.set_ylabel('yaxis')

# rearange the axes for no overlap
fig.tight_layout()

# Get the bounding boxes of the axes including text decorations
r = fig.canvas.get_renderer()
get_bbox = lambda ax: ax.get_tightbbox(r).transformed(fig.transFigure.inverted())
bboxes = np.array(list(map(get_bbox, axes.flat)), mtrans.Bbox).reshape(axes.shape)

#Get the minimum and maximum extent, get the coordinate half-way between those
ymax = np.array(list(map(lambda b: b.y1, bboxes.flat))).reshape(axes.shape).max(axis=1)
ymin = np.array(list(map(lambda b: b.y0, bboxes.flat))).reshape(axes.shape).min(axis=1)
ys = np.c_[ymax[1:], ymin[:-1]].mean(axis=1)

# Draw a horizontal lines at those coordinates
for y in ys:
    line = plt.Line2D([0,1],[y,y], transform=fig.transFigure, color="black")
    fig.add_artist(line)


plt.show()