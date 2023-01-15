import datashader as ds
import pandas as pd
import colorcet as cc
import matplotlib.pyplot as plt
from pyproj import CRS
from pyproj import Transformer
from functools import partial
# Shader pipepline https://datashader.org/getting_started/Pipeline.html

## Read data
df = pd.read_csv('./test_data/nyc_taxi.csv', usecols=['dropoff_x', 'dropoff_y'])
df.head()

# Transform to lat lon
transformer = Transformer.from_crs(3857, 4326)
lat, lon = transformer.transform(df['dropoff_x'],df['dropoff_y'])
# Remake df and store data
df = pd.DataFrame({'lat':lat, 'lon':lon})
agg = ds.Canvas().points(df, 'lon', 'lat')  # sets the locations

## ------------ Simplest plot --------------
myimg = ds.tf.shade(agg, cmap=cc.fire)


##  Select the points from the dataframe and make the image with datashader
myimg = ds.tf.shade(agg, cmap=cc.fire)
tf_df = ds.tf.set_background(ds.tf.shade(agg, cmap=cc.fire), "black")  # Creates a transfer function (xarray with property imag)
# https://datashader.org/api.html#datashader.transfer_functions.Image

## Plot the image
# The transfer function returns a quadmesh
plt.imshow(agg.data, cmap=cc.cm.fire)
plt.show()
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
plt.show()