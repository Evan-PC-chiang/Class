# import libraries
import matplotlib
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import cartopy
import cmocean
import os

matplotlib.use('agg')
""" Make a function to plot and save the data at a given timestep. """

def generate_frame(
        i : int,
        input_file = "/N/project/obrienta_startup/datasets/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc",
        output_dir = './img'):
        data = xr.open_dataset(input_file, chunks = -1)

        # copy the code from above here; have this function return the output file name

        # get the variable at the requested timestep
        tcw = data['TCW'].isel(time=i)
        # plot the variable on an orthographic projection centered on
        # Bloomington, IN
        lat = 39.16
        lon = -86.52
        projection = cartopy.crs.Orthographic(lon, lat)
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection=projection))

        # TURN OFF INLINE PLOTTING
        plt.ioff()

        # plot the data
        tcw.plot(
        ax = ax,
        transform = cartopy.crs.PlateCarree(),
        cmap = cmocean.cm.rain,
        cbar_kwargs = dict(label = f'Precipitable Water [mm]'),
        vmin = 0,
        vmax = 60,
        )

        # get the time of the timestep
        time = tcw.time.values
        # convert it to a datetime object
        time = pd.to_datetime(time)
        # add a title with a nicely formatted date
        ax.set_title(f'{time} UTC')
        # add coastlines
        ax.coastlines(alpha = 0.2)

        # save the plot
        output_file = os.path.join(output_dir, f"tcw_{i:05d}.png")
        fig.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()

        return output_file

