import requests
from typing import List

from flux_tower import FluxTower


# Loose mapping of https://co2.jpl.nasa.gov/developer/grid_api
def beginning_date(tower: FluxTower):
    return str(tower.data_start) + r'-01-01T00:00:00+00:00'


def end_date(tower: FluxTower):
    return str(tower.data_end) + r'-12-31T23:59:59+00:00'


def latitude_min(tower: FluxTower, precision=.0001):
    return str(tower.latitude - precision)


def latitude_max(tower: FluxTower, precision=.0001):
    return str(tower.latitude + precision)


def longitude_min(tower: FluxTower, precision=.0001):
    return str(tower.longitude - precision)


def longitude_max(tower: FluxTower, precision=.0001):
    return str(tower.longitude + precision)


def variables(vs: List[str]):
    v = r''
    for var in vs:
        v = v + 'variable=' + var + r';'
    return v


class GridApi:
    url = 'http://co2.jpl.nasa.gov/wps/'

    def __init__(self, precision=.0001):
        self.precision = precision

    # Going the route of string formed query params. Requests seems to be fighting me on the param parsing a bit
    def generate_grid_query_params(self, tower: FluxTower, vs: List[str]):
        return r'?service=wps&version=1.0.0&request=execute&identifier=grid&datainputs=dataset=OCO2L2Stdv10;' + \
           beginning_date(tower) + r';' + end_date(tower) + r';' + longitude_min(tower) + r';' + longitude_max(tower) + \
           latitude_min(tower) + r';' + latitude_max(tower) + r';' + \
           variables(vs) + \
           r'format=netcdf;&status=true&storeExecuteResponse=true'

    def get_tower_query(self, tower, vs: List[str]):
        query_params = self.generate_grid_query_params(tower, vs)
        return requests.get(self.url + query_params)
