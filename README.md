# Space Missions and Astronauts API REST 🪐

An API REST about space missions and astronauts
<div style='width:520px'>
    <img src='img/astronaut.jpg'>
</div>

_Image from <a href='https://unsplash.com/es/fotos/fotografia-de-un-astronauta-junto-al-satelite-OLlj17tUZnU'>Unplash</a>_

This project is an API REST with django (using [django-rest-framework](https://www.django-rest-framework.org)) about all Space missions and Astronauts that have been in space from 1957 to 2023. In this Readme you will find an explanation, some examples and the endpoints to make queries.
<br>
<br>

> [!NOTE]
> The project is not deployed yet so you can´t use it whithout running the project on your local machine

## Starting 🚀

_This section will help you to have a copy of the project in your local computer in case you want to work, change or test something_


### Installation and requirements 🔧

_You can check requirements of the project on the [requirements.txt file](requirements.txt)_

Because the project will be done with Django-Python, we will need a Python Virtual Enviroment to install all dependencies. You can run in a terminal the following commands:

```console
$ python -m venv .venv --prompt mysite
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

If something goes wrong make sure you have Python installed or or else try to launch the command indicating the version of Python:

```console
$ python3.X -m venv .venv --prompt mysite
```

> [!TIP]
> In case of doubts you can see [the documentation](https://docs.python.org/3/library/venv.html)

Some functionalities will involve the use of sensitive information, so we will use a `.env` file for this purpose. This file must be out of version control so you will need to create one. In the project (mostly in the settings.py file) there will be calls to a config function of the prettyconf library, all these calls are the information that the `.env` file must contain.

To streamline some repetitive processes on terminal we are using [Justfile](https://github.com/casey/just), a handy way to run and save commands. For example, in case of make the migrations of an app in django, instead of using `python manage.py makemigrations app` we are using `just makemigrations app`

### API endpoints 📩 (All endpoints are Insensitive Case, so looking for NASA or nasa will retrieve same JSON)
> [!NOTE]
> Endpoints are build with __icontains method, so you can use urls whithout writting full names.
The API response is in JSON format. You have the following endpoints:  
- ```/api/missions/``` -> Retrieve all missions from database
- ```/api/missions/success/``` -> Retrieve all successfull missions
- ```/api/missions/unsuccess/``` -> Retrieve all unsuccessfull missions
- ```/api/missions/1(pk)/``` -> Retrieve a single mission looking by Id, in this example, mission with id 1
- ```/api/missions/company/Nasa(company_name)``` -> Retrieve all missions by company name, in this example, all missions made by company Nasa
- ```/api/missions/name/Sputnik(mission_name)``` -> Retrieve all missions by mission name, in this example, all missiones named Sputnik
- ```/api/missions/rocket/Falcon1(rocket_name)``` -> Retrieve all missions by rocket name, in this example, all missions made by Falcon rocker
- ```/api/missions/location/Florida(location_name)``` -> Retrieve all missions by location name, in this example, all mission launched from Florida
- ```/api/astronauts/``` -> Retrieve all astronauts
- ```/api/astronauts/1(pk)``` -> Retrieve a single astronaut by id, in this example, astronaut with id 1.
- ```/api/astronauts/nationality/Soviet(nationality)``` -> Retrieve astronauts by their nationality, in this example, all the Soviet astronauts
- ```/api/astronauts/name/Armstrong(name)``` -> Retrieve astronauts by theit name, in this example, all astronauts with surname Armstrong
- ```/api/astronauts/mission/Gemini(name)``` -> Retrieve astronauts by mission name, in this example, all astronauts that went to the space in a mission with name Gemini

> [!IMPORTANT]
> Base url will be http://127.0.0.1:8000 if you are running project locally. This will be updated with the deployment.

## Contribution 🖇️

Feel free to contribute to the project in any way you want <3. I will be happy to receive help from experienced people to correct mistakes and learn because this is one of my firsts API REST with django. 😊

## License 📄

The project is under MIT License - you can see [LICENSE](LICENSE) for more details

---

⌨️ with ❤️ by Adrián ✌️
