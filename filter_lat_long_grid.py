import os
import xarray as xr


def filter_lat_long(lat_lims, long_lims, nc):
    # Returns the portion of nc between the given limits
    # lat_lims and long_lims are lists of the [minimum, maximum] values for latitude
    # and longitude desired from the netcdf file.
    # nc is the netcdf file.

    lats = nc.variables["lat"][:]
    longs = nc.variables["lon"][:]
    lat_inds = lats[
        (lats > lat_lims[0]) & (lats > lat_lims[1])
    ]
    long_inds = longs[
        (longs > long_lims[0]) & (longs < long_lims[1])
    ]
    return nc.sel(lat=lat_inds, lon=long_inds)

all_files = [
    "./data/tropomi/gridded/" + file for file in os.listdir("./data/tropomi/gridded/")
]
for file in all_files:
    savename = "output/filtered_" + file.split("/")[-1]
    all_data = xr.open_mfdataset(file)
    lat_lims = [32.4, 42.0]
    long_lims = [-124.6, -114.1]
    filtered_nc = filter_lat_long(lat_lims, long_lims, all_data)
    filtered_nc.to_netcdf(path=savename, mode="w")
