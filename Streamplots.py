##%
from matplotlib.markers import MarkerStyle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy.ma.core import filled
# For relearning the basics:
# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# Axes class: https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes

##% Streamplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html
print("Working...")
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
fig, axs = plt.subplots(4,3, figsize=(13,13))
#x,y (grid), u,v, density, linewidth, color, cmap, norm, arrowsize, arrowstyle, minlength, start_points, zorder
axs[0,0].streamplot(X, Y, U, V, density=1)  
axs[0,1].streamplot(X, Y, U, V, density=.5) 
axs[0,2].streamplot(X, Y, U, V, density=[2,.5]) 
axs[1,0].streamplot(X, Y, U, V, color='r')  
axs[1,1].streamplot(X, Y, U, V, color=U, cmap='cool')  
axs[1,2].streamplot(X, Y, U, V, linewidth=U, cmap='viridis')  
axs[2,0].streamplot(X, Y, U, V, arrowsize=2)
axs[2,1].streamplot(X, Y, U, V, arrowstyle='->') # Style options https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch
axs[3,0].streamplot(X, Y, U, V, minlength=1) 
axs[3,1].streamplot(X, Y, U, V, maxlength=.8) 
start_pts = np.array([[-1,-1],[0,0],[1,1]])
axs[3,2].scatter(start_pts[:,0],start_pts[:,1], c='r')
axs[3,2].streamplot(X, Y, U, V, start_points=start_pts)
plt.show()
print("Done!")
##

