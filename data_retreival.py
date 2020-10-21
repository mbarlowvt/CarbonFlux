from flux_tower import extract_towers, FluxTower

# Get towers from file
from grid_api import GridApi

# Load towers from file
towers = extract_towers('cali_towers.csv')

# Extract for years that have data
filtered_towers = filter(FluxTower.useful_tower, towers)

# Set up grid api (optionally add precision here)
grid_api = GridApi()

# Pick variables for the grid API
grid_vars = [
    "co2_column_strong_band_idpCO2",
    "co2_column_weak_band_idp",
    "aerosol_aod",
    "co2_grad_del",
    "co2_profile",
    "wind_speed",
    "retrieval_land_water_indicator",
    "retrieved_wet_air_column_layer_thickness",
    "retrieved_dry_air_column_layer_thickness",
    "albedo_o2a",
    "albedo_wco2",
    "albedo_sco2",
]

resp = grid_api.get_tower_query(towers[1], grid_vars)
print(resp.text)
print(resp.content)
