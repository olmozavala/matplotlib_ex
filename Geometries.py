# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Ellipse
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

# %% Elipse example
import matplotlib.pyplot as plt
import numpy as np

# Parameters for ellipse
h = 0.0  # x-position of the center
k = 0.0  # y-position of the center
a = 2.0  # Major axis length
b = 1.0  # Minor axis length
# Print major and minor axis length
print(f"Major axis length: {a:0.2f}")
print(f"Minor axis length: {b:0.2f}")

t = np.linspace(0, 2*np.pi, 100)  # parameter t to parametrize x and y

# Parametrize x and y
x = h + (a/2)*np.cos(t)
y = k + (b/2)*np.sin(t)

fig, ax = plt.subplots()  # Create a new figure with a single subplot

ax.plot(x, y)  # Plot x and y
ax.set_aspect('equal')  # Set the aspect of the plot to equal
ax.grid(True, which='both')  # Add a grid
#
d = 2*np.sqrt((a/2)**2 - (b/2)**2)
print(f"Distance between the foci: {d:0.2f}")
# print length of the string
print(f"Length of the string: {2*np.pi*b + 4*(a-b):0.2f}")
ax.scatter([-d/2, d/2], [0, 0], c='r')  # Plot the foci

# Set x and y spines to zero, i.e., draw x and y axis
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Remove unnecessary spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()


for i in range(10):
    x = np.linspace(-b,b,100)
    dpts = lambda p1, p2: sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


    y = np.sqrt
    y = np.random.uniform(-1, 1)
    if x**2/a**2 + y**2/b**2 <= 1:
        ax.scatter(x, y, c='g')
    else:
        ax.scatter(x, y, c='r')

plt.show()  # Show the plot


# %%
