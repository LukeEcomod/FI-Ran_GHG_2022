This readme.txt describes eddy covariance (EC) and other environmental data from Ränskälänkorpi clearcut study site from the year 2022 that were used in the following research article:
Tikkasalo, O.-P., Peltola, O., Alekseychik, P., Heikkinen, J., Launiainen, S., Lehtonen, A., Li, Q., Martinez-García, E., Peltoniemi, M., Salovaara, P., Tuominen, V., and Mäkipää, R.: Eddy covariance fluxes of CO2, CH4 and N2O on a drained peatland forest after clearcutting, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2024-1994, 2024.

Update information: 
Added T_air_gapfilled.csv and theta_snow_free_period.csv (Tikkasalo, Olli-Pekka 2025-02-17)
updated (Peltola, Olli 2025-02-11)

DATA & FILES: GENERAL INFORMATION
=================================

EC_flux_L3_final_FI-Ran_2022.nc
Gapfilled and partitioned (NEE -> GPP and Reco) EC time series of CO2, CH4 and N2O fluxes and other variables measured at Ränskälänkorpi clearcut EC site during the year 2022 are saved in the NetCDF file EC_flux_L3_final_FI-Ran_2022.nc. The file contains the time series and metadata on the data. The fluxes were calculated with 30-min time step, the time stamp corresponds to the beginning of the averaging period and time zone is UTC. For detailed description on how the the gapfilled flux time series were derived from the turbulence data, see the publication cited above.

inference_data_ch4.csv & inference_data_n2o.csv
These files contain the CH4 and N2O fluxes observed with the EC system along with air temperature, soil moisture and relative contribution of each surface type on the flux footprint at each time step. Data from these files were used in the footprint analysis of the fluxes.
variable name,unit,long name
F_CH4,mumol m-2 s-1,methane flux
F_CH4_ln,ln(mumol m-2 s-1),ln(F_CH4+10)
F_N2O,mumol m-2 s-1,nitrous oxide flux
F_N2O_ln,ln(mumol m-2 s-1),ln(F_N2O)
T_air_K,K, Air temperature
T_air,C, Air temperature
soil_moisture_tomst_mean,%,mean of soil moisture measured at three locations in the clearcut
Dead wood,-,relative contribution of surface class "Dead wood" to the flux footprint
Harvest residue,-,relative contribution of surface class "Harvest residue" to the flux footprint
Exposed peat,-,relative contribution of surface class "Exposed peat" to the flux footprint
Litter,-,relative contribution of surface class "Litter" to the flux footprint
Bottom layer,-,relative contribution of surface class "Bottom layer" to the flux footprint
Field layer,-,relative contribution of surface class "Field layer" to the flux footprint
Ditch,-,relative contribution of surface class "Ditch" to the flux footprint
Living tree,-,relative contribution of surface class "Living tree" to the flux footprint
Plant covered ditch,-,relative contribution of surface class "Plant covered ditch" to the flux footprint
Dead wood and residue,-,relative contribution of surface class "Dead wood and residue" to the flux footprint
Green vegetation and trees,-,relative contribution of surface class "Green vegetation and trees" to the flux footprint
All ditches,-,relative contribution of surface class "All ditches" to the flux footprint
"Residue, ground and vegetation",-,relative contribution of surface class "Residue, ground and vegetation" to the flux footprint

TA_soil_moisture_2022.csv
Time series of air temperature and soil moisture at the Ränskälänkorpi clearcut.
variable name,unit,long name
TA_1_1_1,C,Air temperature
soil_moisture_tomst_mean,m3 m-3,mean of soil moisture measured at three locations in the clearcut
soil_moisture_tomst_std,m3 m-3,standard deviation of soil moisture measured at three locations in the clearcut

T_air_gapfilled.csv
Time series of gapfilled air temperature
variable name, unit, long name
time, YYYY-MM-DD, time of (gapfileld) air temperature observation
T_air, Celsius, (gapfilled) air temperature observation

theta_snow_free_period.csv
Time series of mean soil moisture
variable name, unit, long name
time, YYYY-MM-DD, time of (gapfileld) air temperature observation
soil_moisture_tomst_mean,m3 m-3,mean of soil moisture measured at three locations in the clearcut


In all the files, time stamp corresponds to the beginning of the averaging period and time zone is UTC.

The data have been derived from raw data stemming directly from the instruments in the field. See "Methods" for brief description of the methodology.

METHODS
=======

Eddy covariance data have been processed following best practises for processing eddy covariance data. These practises conform to standardised ICOS research infrastructure practises (see e.g. here: http://www.icos-etc.eu/icos/documents/instructions) when applicable. The processing procedure contains several steps which results in ecosystem-atmosphere flux time series with 30-min time step. The time series are cleaned and quality controlled.

Data files can be accessed with any software that is capable of handling netCDF or csv-files.

More information on the data processing and the data itself can be found in the netCDF files' attributes. Description of the methodology can be found in Tikkasalo et al. (2024).

Tikkasalo, O.-P., Peltola, O., Alekseychik, P., Heikkinen, J., Launiainen, S., Lehtonen, A., Li, Q., Martinez-García, E., Peltoniemi, M., Salovaara, P., Tuominen, V., and Mäkipää, R.: Eddy covariance fluxes of CO2, CH4 and N2O on a drained peatland forest after clearcutting, EGUsphere [preprint], https://doi.org/10.5194/egusphere-2024-1994, 2024.

INFORMATION RELATED TO THE DATASET
===============================

Data has been thoroughly described in the netCDF file attributes, for instance the attributes provide information on the site, instrumentation, measurement heights, variable descriptions etc. Information is also given in the publication cited above.