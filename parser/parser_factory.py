from .providers.csv_parser import CSVParser
from .providers.json_parser import JSONParser
from .providers.xml_parser import XMLParser


class ParserFactory:
    @staticmethod
    def create_parser(file_path):
        if file_path.endswith(".csv"):
            return CSVParser()
        elif file_path.endswith(".json"):
            return JSONParser()
        elif file_path.endswith(".xml"):
            return XMLParser()
        else:
            return None
