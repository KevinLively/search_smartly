import json
from .base_parser import BaseParser


class JSONParser(BaseParser):
    def parse(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for entry in data:
                poi_external_id = entry["id"]
                poi_name = entry["name"]
                poi_category = entry["category"]
                poi_latitude = entry["coordinates"]["latitude"]
                poi_longitude = entry["coordinates"]["longitude"]
                poi_description = entry["description"]
                poi_ratings = entry["ratings"]

                self.build_data(poi_external_id=poi_external_id, poi_name=poi_name, poi_category=poi_category,
                                poi_latitude=poi_latitude, poi_longitude=poi_longitude, poi_ratings=poi_ratings)

        self.save_data()
