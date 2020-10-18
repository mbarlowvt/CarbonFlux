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
grid_vars = ['xco2', 'wind_speed']

resp = grid_api.get_tower_query(towers[1], grid_vars)
print(resp.text)
print(resp.content)
