# Reproduce Ränskälänkorpi clearcut EC 2024 manuscript results

Order of notebooks
1. Create surface type specific contribution for each EC 30 min measurement point from EC footprint data [create_footprint_soilclass_data.ipynb](create_footprint_soilclass_data.ipynb)
2. Combine all the measurement data into one netcdf file [create_biomet_ec_fpr_dataset_all_time_points.ipynb](create_biomet_ec_fpr_dataset_all_time_points.ipynb)
3. Create heatmap of flux correlation between environmental variables [GHG_env_correlation.ipynb](GHG_env_correlation.ipynb) 
4. Create inference data files for CH<sub>4</sub> and N<sub>2</sub>O [create_inference_data.ipynb](create_inference_data.ipynb)
5. Check the prior selection is adequate at [GHG_models_prior_selection.ipynb](GHG_models_prior_selection.ipynb)
6. Fit statistical models for CH<sub>4</sub> and N<sub>2</sub>O [GHG_models_fit.ipynb](GHG_models_fit.ipynb)
7. Run model comparison [GHG_model_comparison.ipynb](GHG_model_comparison.ipynb)
8. Run [create_annual_and_temperature_predictions.ipynb](create_annual_and_temperature_predictions.ipynb) to get model simulations for surface type specific fluxes and annual GHG budget
9. Visualize the surface type specific fluxes and annual GHG budget [GHG_st_T_response.ipynb](GHG_st_T_response.ipynb)
10. Calculate annual GHG emission balance [GHG_site_level_annual_flux.ipynb](GHG_site_level_annual_flux.ipynb)
11. Calculate map parameter contribution to overall measured flux [GHG_map_parameter_contribution.ipynb](GHG_map_parameter_contribution.ipynb)