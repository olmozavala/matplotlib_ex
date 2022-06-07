import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots(1,1)

n = 100
bkground = np.zeros((n,n,3))
patches = []
patches.append(Circle((30,20, 20)))
patches.append(Polygon([[40,40],[40,80],[60,80]]))

colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.8)
p.set_array(colors)

ax.imshow(bkground)
ax.add_collection(p)
# fig.colorbar(p, ax=ax)

plt.show()

##

