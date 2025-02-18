import xarray as xr
import pandas as pd
import pytz
from datetime import datetime
from typing import List, Callable

def epoch_time_to_datetime64(ds: xr.Dataset, old_time_label: str) -> xr.Dataset:
    # Set timezone to Finland
    helsinki_tz = pytz.timezone('Europe/Helsinki')
    new_time = datetime(1970,1,1)+pd.to_timedelta(pd.Series(ds[old_time_label].data),unit='D')
    
    #new_time = np.array([datetime.fromtimestamp(int(t*24*60*60), tz=helsinki_tz) for t in ds[old_time_label]])

    ds[old_time_label] = new_time

    return ds

def load_dataset(path: Callable, years, concat_dim=None):
    dataset = xr.open_dataset(path(years[0]))
    if len(years) > 1 and concat_dim is not None:
        for year in years[1:]:
            dataset = xr.concat((dataset, xr.open_dataset(path(year))), dim=concat_dim)

    return dataset

def load_Ran_gapfilled_ec_data(filepath: str, years: List[int]) -> xr.Dataset:

    def path(x): return f'{filepath}EC_flux_L3_final_FI-Ran_{x}.nc'

    ec_data = load_dataset(path, years, concat_dim='time')
    ec_data = epoch_time_to_datetime64(ec_data, 'time')

    return ec_data
