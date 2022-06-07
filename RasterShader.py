from netCDF4 import Dataset
import matplotlib.pyplot as plt
import xarray as xr

file_name = "/nexsan/people/abozec/GLBb0.08/XIAOBIAO/expt_03.9/mld_0.03/mld_thk_039_d0.03_glbb008_2018_01.nc"
ds = Dataset(file_name)
##
rs = 10
mld = ds['mld'][0,0,-1:0:-rs,::rs]
lat = ds['Latitude'][::rs,::rs]
lon = ds['Longitude'][::rs,::rs]

##
# fig, axs = plt.subplots(1,3, figsize=(15,5))
# axs[0].imshow(lat)
# axs[1].imshow(lon)
# axs[2].imshow(mld)
# plt.show()
##
plt.pcolormesh(mld, lat, lon)
plt.show()

# ##
# da = xr.DataSet(
#     {
#         "mld": (("lat","lon"), mld[0,0,:,:]),
#     },
#     {"lon",
#                           ('lat',lat)],
#                   name='mld')
#
# kkkkkkkkkkk