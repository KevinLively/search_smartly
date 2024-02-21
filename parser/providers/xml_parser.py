from .base_parser import BaseParser
import xml.etree.ElementTree as ET


class XMLParser(BaseParser):
    def parse(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for data_record in root.findall("DATA_RECORD"):
            poi_external_id = data_record.find("pid").text
            poi_name = data_record.find("pname").text
            poi_category = data_record.find("pcategory").text
            poi_latitude = float(data_record.find("platitude").text)
            poi_longitude = float(data_record.find("plongitude").text)
            poi_ratings = data_record.find("pratings").text.split(",")

            self.build_data(poi_external_id=poi_external_id, poi_name=poi_name, poi_category=poi_category,
                            poi_latitude=poi_latitude, poi_longitude=poi_longitude, poi_ratings=poi_ratings)

        self.save_data()
