import csv

from datetime import datetime
from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from api.models import SpaceMissions

class Command(BaseCommand):
    help = 'Load the database from the file with information'

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument('--file', dest='file', type=str)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        file = options['file']
        with open(file, mode='r') as file:
            f = csv.DictReader(file)
            for line in f:
                rocketStatus = line['RocketStatus']
                success = line['success']
                SpaceMissions.objects.create(
                    mission=line['Mission'],
                    company=line['Company'],
                    location=line['Location'],
                    date=datetime.strptime(line['Date'], '%Y-%m-%d').date(),
                    time=datetime.strptime(line['Time'], '%H:%M:%S').time(),
                    rocket=line['Rocket'],
                    rocketStatus='A' if rocketStatus == 'Active' else 'R',
                    success=True if success == 'Success' else False
                )
