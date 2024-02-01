FROM python:3.12.1-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py load_missions --file=api/management/data/missions.csv
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
