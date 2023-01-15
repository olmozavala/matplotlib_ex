# %%
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import numpy as np

##%------------ data -----------
n = 100
x = np.linspace(0,2*np.pi,n)
y = np.sin(x)

## ------------ plot line -----------
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.set_title('Basic Plot')
ax.plot(x,y, 'r', label='1')
ax.plot(x,y+.5, 'g--', label='2')
ax.set_xlabel("Sopas")
ax.set_ylabel("Pericon")
ax.legend()
plt.show()

## ------------ plot scatter -----------
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.scatter(x,y, label='simplest')
ax.scatter(x,y-.3, color='b', alpha=np.linspace(0,1,len(x)), label='alpha')    # alpha
ax.scatter(x,y-.5, c=np.linspace(0,1,len(x)), label='color')                   # color
ax.scatter(x,y-.8, s=np.linspace(0,100,len(x)), label='size')                 # Size
ax.set_title("Scatter")
ax.legend()
plt.show()

## ------------ COLOR BARS AND COLOR PALETTES-----------
# Palettes here: https://matplotlib.org/stable/tutorials/colors/colormaps.html#sequential
## ----------------- For single plot
fig, ax = plt.subplots(1,1,figsize=(10,10))
s1 = ax.scatter(x,y, c=np.linspace(0,1,len(x)), cmap='plasma')                    # palette
s2 = ax.scatter(x,y-.2, c=np.linspace(0,1,len(x)), cmap='viridis',vmin=-1, vmax=2)
ax.set_title("Color bar and palette")
plt.colorbar(s2,label='label')
plt.colorbar(s1)
plt.show()

## ----------------- For multiple plots
fig, axs = plt.subplots(1,2,figsize=(10,10), gridspec_kw={'width_ratios': [3, 1]})
s1 = axs[0].scatter(x,y, c=np.linspace(0,1,len(x)), cmap='plasma')                    # palette
s2 = axs[1].scatter(x,y-.2, c=np.linspace(0,1,len(x)), cmap='viridis')                    # palette
axs[0].set_title("Plasma")
axs[1].set_title("Viridis")
fig.colorbar(s1,ax=axs[0])
fig.colorbar(s2,ax=axs[1])
plt.show()

## ------------ Text (labels and ticks) options -----------
font_size = 20
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.set_title('Basic Plot')
plt.tick_params(axis='both', which='major', labelsize=font_size)
ax.scatter(x, y, c='r', label='1', )
# ax.set_xticks(np.round(x), labels=[str(np.round(i*2)) for i in x], rotation=90)
plt.xticks(rotation=90)
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=5)
ax.set_xlabel('This is my x label', fontsize=font_size)
ax.set_ylabel('This is my y label', fontsize=font_size)
ax.legend()
plt.show()

## ------------ GRID options-----------
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.set_title('Basic Plot')
ax.plot(x,y, 'r', label='1')
ax.yaxis.grid(True, linestyle='-', which='major', color='blue', alpha=0.5)
ax.xaxis.grid(True, linestyle=':', which='major', color='red', alpha=0.8)
ax.legend()
plt.show()


## ------------ Box plot -----------
# https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py
fig, ax = plt.subplots(figsize=(10,6))
plt.title('Basic Plot')
names = ['name1', 'name2']
data = [np.random.rand(50) * 100, np.random.rand(50) * 100]
bp = plt.boxplot(data, notch=True, labels= names, patch_artist=True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Sopas")
ax.set_ylabel("Pericon")

# fill with colors
colors = ['pink', 'lightblue']
for patch, color in zip(bp['boxes'], colors):
   patch.set_facecolor(color)

plt.show()

## ------------ bar plot-----------
fig, ax = plt.subplots(1,1,figsize=(10,10))
plt.title('BarPlot')
# Multibars are hard to do directly with matplotlib
names = ['name1', 'name2']
pos = np.arange(2)
ax.bar(pos, [2,2.1], color='r')
ax.set_xticks(pos, labels=names)
ax.bar(pos+ .2, [2.1,2.0])
ax.legend()
plt.show()

## ------------ Pie plot-----------
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

## ---- Heat maps / images
import numpy as np

n = 100
x = np.linspace(0,np.pi,n)
y = np.sin(x)*2
X, Y = np.meshgrid(y, y)

fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.imshow(X+Y, extent=(min(x),max(x),min(x),max(x)))
plt.show()

## Annotated heatmap
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.imshow(X+Y)
ax.text(n/2, n/2, "Sopas perico lico", color="red")
plt.show()

## -- Own default style ------------
# Generate basic data
x = np.linspace(0, np.pi*2, 100)
y = np.sin(x)

# ##%
# # Reading own  style
plt.style.use('./my_matplotlib_sytles.mplstyle')
plt.style.use('default') # Reset style
fig, ax = plt.subplots()
ax.plot(x,y, c='r',label='1')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Using custom styles for matplotlib ')
plt.show()
