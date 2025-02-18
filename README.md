# Reproduce results of "Eddy-covariance fluxes of CO2, CH4 and N2O in a drained peatland forest after clear-cutting" by Tikkasalo et al.

The data that is needed to run the notebooks is in the data folder. To run model parameter estimation the inference data csvs are needed. The netcdf files and TA_soil_moisture_2022.csv are needed to reproduce Fig. 2 of the manuscript. 
The data does not include water table depth data or EC flux wind direction and for that matter the model comparison results cannot be reproduced.

## To reproduce the modelled surface-type-specific flux estimates
0. Create python virtual environment with requirements either from [requirements.txt](requirements.txt) or from [pyproject.toml](pyproject.toml)
e.g. on mac,
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
1. Create folder "models"
2. Check the prior selection is adequate at [GHG_models_prior_selection.ipynb](GHG_models_prior_selection.ipynb)
3. Fit statistical models for CH<sub>4</sub> and N<sub>2</sub>O
    - [GHG_models_fit.ipynb](GHG_models_fit.ipynb) (simple and Full ST models)
    - [GHG_models_fit_theta.ipynb](GHG_models_fit_theta.ipynb) (Simple $\theta$ and Full $\theta$ ST models)
    - [GHG_models_fit_no_st_T_theta.ipynb](GHG_models_fit_no_st_T_theta.ipynb) (Full $\theta$ no $\delta$ ST models)
    - [GHG_models_fit_no_st_T.ipynb](GHG_models_fit_no_st_T.ipynb) (Full no $\delta$ ST models)
4. Run model comparison [GHG_model_comparison_all.ipynb](GHG_model_comparison_all.ipynb)
5. Run detailed model comparison for $\theta$ models [GHG_model_comparison_theta.ipynb](GHG_model_comparsin_theta.ipynb)
6. Run [create_annual_predictions.ipynb](create_annual_predictions.ipynb) to get model simulations for surface type specific fluxes and annual GHG budget
7. Visualize the surface type specific fluxes and annual GHG budget [GHG_st_T_response.ipynb](GHG_st_T_response.ipynb)
8. Calculate annual GHG emission balance [GHG_site_level_annual_flux.ipynb](GHG_site_level_annual_flux.ipynb)