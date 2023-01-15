import datashader as ds
import cartopy.crs as ccrs
import pandas as pd
import numpy as np
import colorcet as cc
import matplotlib.pyplot as plt
from pyproj import CRS
from pyproj import Transformer
from os.path import join
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


## Define the 'Canvas' or area where we want to plot our data
# https://datashader.org/api.html?highlight=dataarray#datashader.Canvas
agg = ds.Canvas().points(df, 'lon', 'lat')  # Data to pixels

## ------------ Simplest plot (convert dataarray to an image)--------------
# plt.imshow(agg.data, cmap=cc.cm.fire)
back_folder = './map_backgrounds/'
# img = plt.imread(join(back_folder, 'bluemarble.png'))
img = plt.imread(join(back_folder, 'bluemarble_5400x2700.jpg'))
extent = (lon.min(), lon.max(), lat.min(), lat.max())
img_extent = (-180, 180, -90, 90)
fig, ax = plt.subplots(1, 1, figsize=(8,5), subplot_kw={'projection': ccrs.PlateCarree()})
ax.stock_img()
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
im = ax.imshow(agg.data, origin='lower', extent=extent, transform=ccrs.PlateCarree(), cmap='viridis', alpha=(agg.data == 1).astype(float))
ax.set_title("Main example to use!")
gl = ax.gridlines(draw_labels=True, color='grey', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.left_labels = False
gl.xlabel_style = {'size': 10, 'weight':'bold'}
# plt.colorbar(im, location='right', shrink=.6, pad=.12)
plt.tight_layout()
plt.show()
##

