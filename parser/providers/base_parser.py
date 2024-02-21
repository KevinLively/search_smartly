from point_of_interest.models import PointOfInterest, Rating
import asyncio
import re
from abc import abstractmethod
from tqdm import tqdm


class BaseParser:

    def __init__(self):
        self.point_of_interests = []
        self.ratings = []

    @abstractmethod
    def parse(self, file_path):
        pass

    def build_data(self, poi_external_id, poi_name, poi_latitude, poi_longitude, poi_category, poi_ratings):
        point_of_interest = PointOfInterest(
            poi_external_id=poi_external_id,
            poi_name=poi_name,
            poi_latitude=poi_latitude,
            poi_longitude=poi_longitude,
            poi_category=poi_category
        )
        self.point_of_interests.append(point_of_interest)

        for rating in poi_ratings:
            rating = Rating(score=float(rating))
            rating.point_of_interest = point_of_interest
            self.ratings.append(rating)

    def save_data_helper(self, parsed_data, fun):
        chunk_size = 10000
        chunks = [
            parsed_data[i: i + chunk_size]
            for i in range(0, len(parsed_data), chunk_size)
        ]

        loop = asyncio.new_event_loop()

        tasks = [
            loop.run_in_executor(None, fun, chunk) for chunk in chunks
        ]

        with tqdm(total=len(chunks), desc="Processing chunks") as pbar:
            async def process_tasks():
                for task in asyncio.as_completed(tasks):
                    await task
                    pbar.update(1)

            loop.run_until_complete(process_tasks())

    def save_data(self):
        self.save_data_helper(self.point_of_interests, PointOfInterest.objects.bulk_create)

        for rating in self.ratings:
            rating.poi_id = rating.point_of_interest.poi_id

        self.save_data_helper(self.ratings, Rating.objects.bulk_create)

        self.output_message()

    def output_message(self):
        class_name = re.findall(r'[A-Z]', self.__class__.__name__)[:-1]
        class_name = ''.join(class_name)
        print(f"{class_name} Data has been parsed and saved.")
