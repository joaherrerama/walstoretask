import os

import requests
from pyproj import Geod
from shapely import geometry, wkt


class POILookUp:
    def get_nearby_poi(point):
        new_point = wkt.loads(point)
        geojson = geometry.mapping(new_point)
        coords = geojson["coordinates"]
        latitude = coords[1]
        longitude = coords[0]
        radius = 100
        secret_key = os.getenv("ggl_place_key")  # secret key
        print(secret_key)
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&key={secret_key}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        list = response.json()
        result = list["results"]
        poi_list = []
        for poi in result:
            lat = poi["geometry"]["location"]["lat"]
            lon = poi["geometry"]["location"]["lng"]
            format = {}

            format["name"] = poi["name"]

            try:
                format["bussines_status"] = poi["bussines_status"]
            except Exception:
                format["bussines_status"] = "No Data"

            try:
                format["rate"] = poi["rate"]
            except Exception:
                format["rate"] = "No Data"

            format["type"] = (poi["types"],)
            format["location"] = f"POINT ({lon} {lat})"

            poi_list.append(format)

        return poi_list

    def get_distance(store, poi):
        store = wkt.loads(store)
        poi = wkt.loads(poi)

        line_string = geometry.LineString([store, poi])
        geod = Geod(ellps="WGS84")

        distance = geod.geometry_length(line_string)

        return distance
