import xarray as xr
import matplotlib.pyplot as plt
from os.path import join
import os
import numpy as  np

folder_32= "/home/olmozavala/TEMP/32"
folder_8 = "/home/olmozavala/TEMP/8"
files_32 = os.listdir(folder_32)
files_32.sort()

rmse = []
for i, c_file in enumerate(files_32):
    if i > 0:
        ds = xr.load_dataset(join(folder_32,c_file))
        ds_8 = xr.load_dataset(join(folder_8,c_file))
        predds = xr.load_dataset(join(folder_32,files_32[i-1]))
        fig, axes = plt.subplots(1,4, figsize=(20,6))
        axes[0].imshow(ds['assh'][0,0,:,:])
        axes[0].set_title(c_file)
        axes[0].set_title(f"32 {c_file}")
        axes[1].imshow(ds_8['assh'][0,0,:,:])
        axes[1].set_title(c_file)
        axes[0].set_title(f"8 {c_file}")
        axes[2].imshow(ds['assh'][0,0,:,:].data - ds_8['assh'][0,0,:,:].data)
        axes[2].set_title(f"Diff {c_file}")
        axes[3].imshow(ds['assh'][0,0,:,:].data - predds['assh'][0,0,:,:].data)
        axes[3].set_title(f"Diff {c_file}")

        plt.tight_layout()
        plt.show()

        rmse_val = np.sqrt(np.nanmean((ds['assh'][0,0,:,:].data - predds['assh'][0,0,:,:].data)**2))
        rmse.append(rmse_val)

plt.scatter(range(len(rmse)), rmse)
plt.show()