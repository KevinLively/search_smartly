from django.core.management.base import BaseCommand
from parser.parser_factory import ParserFactory
import asyncio


class Command(BaseCommand):
    help = "Import Point of Interest data"

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+", type=str)

    def parse_file(self, file_path):
        parser = ParserFactory.create_parser(file_path)
        if parser:
            parser.parse(file_path)
        else:
            self.stderr.write(
                self.style.ERROR(f"Unsupported file format for {file_path}")
            )

    def handle(self, *args, **options):
        files = options["files"]
        loop = asyncio.new_event_loop()
        tasks = [
            loop.run_in_executor(None, self.parse_file, file_path)
            for file_path in files
        ]
        loop.run_until_complete(asyncio.gather(*tasks))
