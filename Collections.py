import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
import numpy as np
##

#https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html

# YOU NORMALLY NEED TO SET THE PROPER LIMITS, THEY WILL NOT ADJUST, BUT TAKEN FROM FIRST LINE
fig, ax = plt.subplots()

# Make a sequence of (x, y) pairs.
# The way it is arranged is
colors = [mcolors.to_rgba(c) for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]
# seg = np.array([ [[0,0], [1,1]], [[0.1,.5], [.9,.1]] ])  # Two simple lines (2,2,2)
# seg = np.array([ [[0,0], [1,1], [.9,.4]], [[0.1,.5], [.9,.1], [.5, .9]] ]) # Two multisegment lines. (2,3,2)
seg = np.array([ [[0,0], [1,1]], [[0.1,.5], [.9,.1]],  [[0.2,.1], [.4,.9]] ]) # Three lines (3,2,2)
line_segments = LineCollection(seg,
                               linewidths=(0.5, 2),
                               linestyles='dashed')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.show()

#################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
# three lines
paths_x = [[1,2,3], [1,2,3], [1,2,3]]
paths_y = [[1,1,1], [2,2,2], [3,3,3]]
values = np.array([0, 1, 2]) # you can also plot a value line (as to be an array for some reason!)
# plot line with time as color
segments = []
colors = []
for i in range(0, len(paths_x)):
    x = paths_x[i]
    y = paths_y[i]
    segments.append(list(zip(x, y)))
# format of this is not super intuitive
# create a list of tuple of points
segments
fig = plt.figure(dpi=200)
ax = fig.add_subplot(1,1,1)
lc = LineCollection(segments, cmap='viridis', alpha=1.0) # create the collection
lc.set_array(values) # color per segments/lines
lc.set_linewidth(1) # size of lines
lccb = fig.colorbar(lc) # if you want a colorbar of the line color
lccb.set_label('Unit [-]') # colorbar label
ax.add_collection(lc)
ax.set_xlim([0.5,3.5])
ax.set_ylim([0.5,3.5])