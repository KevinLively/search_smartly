import csv
from tqdm import tqdm
from .base_parser import BaseParser


class CSVParser(BaseParser):
    def parse(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            total_rows = len(list(reader))

            file.seek(0)
            next(reader)  # skipping  header

            for row in tqdm(reader, total=total_rows, desc="Processing Rows", unit="row"):
                poi_external_id = row["poi_id"]
                poi_name = row["poi_name"]
                poi_category = row["poi_category"]
                poi_latitude = float(row["poi_latitude"])
                poi_longitude = float(row["poi_longitude"])
                poi_ratings = row["poi_ratings"].strip("{}").split(",")

                self.build_data(poi_external_id=poi_external_id, poi_name=poi_name, poi_category=poi_category,
                                poi_latitude=poi_latitude, poi_longitude=poi_longitude, poi_ratings=poi_ratings)

        self.save_data()
