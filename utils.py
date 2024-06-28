import xarray as xr
import numpy as np
import pandas as pd
import pytz
from datetime import datetime,timedelta
from typing import List, Dict, Callable


def epoch_time_to_datetime64(ds: xr.Dataset, old_time_label: str) -> xr.Dataset:
    # Set timezone to Finland
    helsinki_tz = pytz.timezone('Europe/Helsinki')
    new_time = datetime(1970,1,1)+pd.to_timedelta(pd.Series(ds[old_time_label].data),unit='D')
    
    #new_time = np.array([datetime.fromtimestamp(int(t*24*60*60), tz=helsinki_tz) for t in ds[old_time_label]])

    ds[old_time_label] = new_time

    return ds

def datetime64_to_timestamp(ds: xr.Dataset, old_time_label: str) -> xr.Dataset:
    helsinki_tz = pytz.timezone('Europe/Helsinki')
    new_time = np.array([pd.Timestamp(t).tz_localize(helsinki_tz, ambiguous=True, nonexistent='shift_forward') for t in ds[old_time_label].values])
    ds[old_time_label] = new_time

    return ds

def df_to_dataset(dataframes: List[pd.DataFrame], concat_dim=None, renamer: Dict = None):
    ds = xr.Dataset.from_dataframe(dataframes[0])
    if len(dataframes) > 1 and concat_dim is not None:
        for i, df in enumerate(dataframes[1:]):
            ds = xr.concat((ds, xr.Dataset.from_dataframe(df)), dim=concat_dim)
    if renamer is not None:
        ds = ds.rename(renamer)

    return ds


def load_dataset(path: Callable, years, concat_dim=None):
    dataset = xr.open_dataset(path(years[0]))
    if len(years) > 1 and concat_dim is not None:
        for year in years[1:]:
            dataset = xr.concat((dataset, xr.open_dataset(path(year))), dim=concat_dim)

    return dataset


def load_csv(path: Callable, years: List[int]):
    dataframes = []
    dataframes.append(pd.read_csv(path(years[0]), skiprows=[1], index_col=0, date_parser=lambda x: pd.to_datetime(x)))
    if len(years) > 1:
        for year in years[1:]:
            dataframes.append(pd.read_csv(path(year), skiprows=[1], index_col=0, date_parser=lambda x: pd.to_datetime(x)))
    return dataframes


def load_Ran_ec_data(onedrive_path: str, years: List[int]) -> xr.Dataset:

    def path(x): return f'{onedrive_path}EC/EC_flux_L2_final_FI-Ran_{x}.nc'

    ec_data = load_dataset(path, years, concat_dim='time')
    ec_data = epoch_time_to_datetime64(ec_data, 'time')

    return ec_data


def load_Ran_biomet_data(onedrive_path: str, years: List[int]) -> xr.Dataset:
    def path(x): return f'{onedrive_path}biomet/biomet_final_30min_FI-Ran_{x}.csv'

    csv_data = load_csv(path, years)
    biomet_data = df_to_dataset(csv_data, concat_dim='TIMESTAMP_1', renamer={'TIMESTAMP_1': 'time'})
    
    # Replace -9999 with NaN
    biomet_data = biomet_data.where(biomet_data != -9999, np.nan)

    return biomet_data
