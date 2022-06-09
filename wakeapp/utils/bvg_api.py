import json
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple

import requests

BVGLocationId = int

@dataclass
class bvg_api:
    __base_url: str

    def fetch_location_id(self, location: str, poi:bool = False) -> BVGLocationId:
        """Takes a stop and returns id from BVG Api"""
        params = {
            'poi': poi,
            'addresses': False,
            'query': location
        }
        response = requests.get(self.__base_url+'/locations', params=params)
        first_location_id = int(json.loads(response.text)[0]['id'])
        return first_location_id

    def fetch_depature_arrival_time(self, origin: BVGLocationId, destination: BVGLocationId, arrival_time: datetime) -> Tuple[str, str]:
        """Takes the ids from the origin and destination location and the wanted arrival time and returns the depature and arrival time
            as a Tuple in an ISO 8601 datetime string format
        """
        params = {
            "from": origin,
            "to": destination,
            "arrival": arrival_time
        }

        response = requests.get(self.__base_url + "/journeys", params=params)
        first_leg = json.loads(response.text)["journeys"][0]["legs"]
        return (first_leg[0]['departure'], first_leg[-1]['arrival'])
    
