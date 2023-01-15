import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from os.path import join

##  Reading data and plotting lats and lons
in_file = "./test_data/hycom_glby_930_2021052912_t000_uv3z.nc"
ds = xr.load_dataset(in_file)
lat_idxs = [np.where(ds.latitude > 15)[0][0] , np.where(ds.latitude > 31)[0][0]]
lon_idxs = [np.where(ds.longitude > 360 -110)[0][0] , np.where(ds.longitude > 360 -78)[0][0]]
ds = ds.sel(lat=slice(lat_idxs[0], lat_idxs[1]), lon=slice(lon_idxs[0], lon_idxs[1]))
myvar = ds['surf_u'][0,:,:]
print(ds.info())

lats = ds.latitude
lons = ds.longitude

## --------- Main example to use -----------
## Grid manipulation
# back_folder = './home/olmozavala/Dropbox/TutorialsByMe/Python/PythonExamples/Python/MatplotlibEx/map_backgrounds/'
back_folder = './map_backgrounds/'
# img = plt.imread('/home/olmozavala/Dropbox/TutorialsByMe/Python/PythonExamples/Python/MatplotlibEx/map_backgrounds/bluemarble.png')
img = plt.imread(join(back_folder,'bluemarble_5400x2700.jpg'))  # BATHYMETRY BLACK LAND
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
img_extent = (-180, 180, -90, 90)
fig, ax = plt.subplots(1, 1, figsize=(8,5), subplot_kw={'projection': ccrs.PlateCarree()})
ax.stock_img()
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
im = ax.imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='viridis')
ax.set_title("Main example to use!")
gl = ax.gridlines(draw_labels=True, color='grey', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.left_labels = False
gl.xlabel_style = {'size': 10, 'weight':'bold'}
plt.colorbar(im, location='right', shrink=.6, pad=.12)
plt.tight_layout()
plt.savefig('./outputs/final.png')
plt.show()

## Imshow  (fast but innacurate)
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
fig, ax = plt.subplots(1, 1, figsize=(8,6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
ax.stock_img()
ax.imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='inferno')
ax.set_title("Innacurate at but fast!")
plt.savefig('./outputs/ex1.png')
plt.tight_layout()
plt.show()

## Contourf  (slow but accurate)
print("Plotting....")
num_colors = 128
fig, ax = plt.subplots(1,1, figsize=(8,6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.contourf(lons, lats, myvar, num_colors, cmap='inferno', extent=extent)
ax.coastlines()
# ax.stock_img()
ax.set_title("Accurate but slow (and can't use stock img)")
plt.tight_layout()
plt.show()
print("Done!")

## Colorbar (fast but innacurateareas)
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
fig, ax = plt.subplots(1, 1, figsize=(8,6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
# ax.stock_img()
im = ax.imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='inferno')
ax.set_title("Imshow with colorbar!")
plt.colorbar(im, location='right', shrink=.6, pad=.02)
plt.tight_layout()
# plt.savefig('./outputs/ex1.png')
plt.show()

## Multiple maps
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
fig, axs = plt.subplots(1, 2, figsize=(10,4), subplot_kw={'projection': ccrs.PlateCarree()})
# Left plot
axs[0].stock_img()
img1 = axs[0].imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='inferno')
axs[0].set_title("Title 1 ")
fig.colorbar(img1, ax=axs[0], fraction=.032)
# Right plot
im = axs[1].imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='viridis')
axs[1].set_title("Title 2")
fig.colorbar(im, ax=axs[1], fraction=.032)
plt.tight_layout()
plt.suptitle("Multiple plots")
plt.show()

## Blue marble or TOpo
# https://visibleearth.nasa.gov/collection/1484/blue-marble
img = plt.imread(join(back_folder, 'bathymetry_3600x1800.jpg'))
img = plt.imread(join(back_folder, 'bluemarble_5400x2700.jpg'))
img = plt.imread(join(back_folder, 'bluemarble.png'))
img = plt.imread(join(back_folder, 'etopo.png'))
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
img_extent = (-180, 180, -90, 90)
fig, ax = plt.subplots(1, 1, figsize=(8,6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.stock_img()
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax.imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='viridis')
ax.set_title("Background image!")
plt.tight_layout()
plt.savefig('./outputs/exbluemarble.png')
plt.show()

## Grid manipulation
img = plt.imread(join(back_folder, 'bluemarble.png'))
extent = (lons.min() - 360, lons.max() - 360, lats.min(), lats.max())
img_extent = (-180, 180, -90, 90)
fig, ax = plt.subplots(1, 1, figsize=(8,5), subplot_kw={'projection': ccrs.PlateCarree()})
ax.stock_img()
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
im = ax.imshow(myvar, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='viridis')
ax.set_title("Innacurate at the borders but fast!")
gl = ax.gridlines(draw_labels=True, color='grey', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.left_labels = False
gl.xlabel_style = {'size': 10, 'color': '#0000FF', 'weight':'bold'}
plt.colorbar(im, location='right', shrink=.6, pad=.12)
plt.tight_layout()
plt.savefig('./outputs/final.png')
plt.show()
