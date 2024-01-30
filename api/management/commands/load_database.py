import csv
from datetime import datetime
from typing import Any

import pytz
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from api.models import SpaceMissions


class Command(BaseCommand):
    help = 'Load the database from the file with information'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('--file', dest='file', type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        def build_mission_launch_datetime(date: str, time: str) -> datetime:
            ctime = time or '00:00:00'
            cdate = date
            cdatetime = f'{cdate} {ctime}'
            launch_datetime = datetime.strptime(cdatetime, '%Y-%m-%d %H:%M:%S')
            return pytz.utc.localize(launch_datetime)

        SpaceMissions.objects.all().delete()
        file = options['file']
        with open(file, mode='r') as file:
            f = csv.DictReader(file)
            bulk_list = []
            for line in f:
                success = line['MissionStatus']
                new_mission = SpaceMissions(
                    mission=line['Mission'],
                    company=line['Company'],
                    location=line['Location'],
                    launched=build_mission_launch_datetime(line['Date'], line['Time']),
                    rocket=line['Rocket'],
                    rocketStatus=line['RocketStatus'],
                    success=success == 'Success',
                )
                bulk_list.append(new_mission)
            SpaceMissions.objects.bulk_create(bulk_list)


# import csv
# from datetime import datetime
# from typing import Any

# import pytz
# from django.core.management import BaseCommand
# from django.core.management.base import CommandParser
# from tqdm import tqdm

# from api.models import SpaceMissions


# class Command(BaseCommand):
#     help = 'Load the database from the file with information'

#     def add_arguments(self, parser: CommandParser) -> None:
#         return parser.add_argument('--file', dest='file', type=str)

#     def handle(self, *args: Any, **options: Any) -> str | None:
#         def build_mission_launch_datetime(date: str, time: str) -> datetime:
#             ctime = time or '00:00:00'
#             cdate = date
#             cdatetime = f'{cdate} {ctime}'
#             launch_datetime = datetime.strptime(cdatetime, '%Y-%m-%d %H:%M:%S')
#             return pytz.utc.localize(launch_datetime)

#         SpaceMissions.objects.all().delete()
#         file = options['file']
#         with open(file, mode='r') as file:
#             f = csv.DictReader(file)
#             for line in tqdm(f, total=4630):
#                 success = line['MissionStatus']
#                 SpaceMissions.objects.create(
#                     mission=line['Mission'],
#                     company=line['Company'],
#                     location=line['Location'],
#                     launched=build_mission_launch_datetime(line['Date'], line['Time']),
#                     rocket=line['Rocket'],
#                     rocketStatus=line['RocketStatus'],
#                     success=success == 'Success',
#                 )
