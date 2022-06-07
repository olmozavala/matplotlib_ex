import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

##  Empty map
fig, ax = plt.subplots(1,1,  subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
plt.show()

## -------------------- Scatter locations
n = 100
lats = np.linspace(-20,40,n)
lons = np.linspace(-100, 100, n)

## -------------------- Scatter plot in a map
bbox = (-180, 180, -90, 90)
# Here is the geoaxes api
# https://scitools.org.uk/cartopy/docs/latest/reference/matplotlib.html#geoaxes
fig, ax = plt.subplots(1, 1,  subplot_kw={'projection': ccrs.PlateCarree()})
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(bbox)  # If we do not set this, it will cropp it to the limits of the locations
ax.gridlines()
ax.scatter(lons, lats)
ax.coastlines()
plt.show()

## -------------------- Lines in a map
bbox = (-180, 180, -90, 90)
# Here is the geoaxes api
# https://scitools.org.uk/cartopy/docs/latest/reference/matplotlib.html#geoaxes
fig, ax = plt.subplots(1,1,  subplot_kw={'projection': ccrs.PlateCarree()})
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(bbox)  # If we do not set this, it will cropp it to the limits of the locations
ax.gridlines()
ax.plot([200, 170], [0, 0], 'r', transform=ccrs.PlateCarree())
ax.coastlines()
plt.show()

## ------------ Image with specific extent
fig = plt.figure()
gs = fig.add_gridspec(1, 1)

ax1 = fig.add_subplot(gs[0], projection=ccrs.PlateCarree())
ax1.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
ax1.coastlines(resolution='auto', color='k')
ax1.imshow(np.random.random((10,10)), extent=[-170,170,-70,70])
plt.show()

print("Done!")