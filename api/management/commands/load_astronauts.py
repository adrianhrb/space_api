import csv
from datetime import datetime
from typing import Any

import pytz
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from tqdm import tqdm

from api.models import Astronauts


class Command(BaseCommand):
    help = 'Load the database with all the astronauts from a given file'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('--file', dest='file', type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        Astronauts.objects.all().delete()
        file_from = options['file']
        with open(file_from, mode='r') as file:
            f = csv.DictReader(file)
            astronauts_bulk = []
            for line in tqdm(f, total=644):
                birthdate = pytz.utc.localize(datetime.strptime(line['Date'], '%Y-%m-%d'))
                new_astronaut = Astronauts(
                    fullname=line['Name'],
                    birthdate=birthdate,
                    nationality=line['Nationality'],
                    mission=line['Flight'],
                )
                astronauts_bulk.append(new_astronaut)
            Astronauts.objects.bulk_create(astronauts_bulk)
