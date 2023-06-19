# Core Advertisement




### Setup & Installation
To clone this respository, run the following command in you terminal
``` bash
git clone https://github.com/EpicAp-AppinApp/CoreAdvertisement.git
```

```bash
cd CoreAdvertisement 
```

#### Creating vitual environment
```bash
python3 -m venv venv
```
Activating virtual environment on linux

```bash
source venv/bin/activate
```
Installing dependency

```bash 
pip install -r requirements.txt
```

Adding environment variable(advertisement/settings/.env)

```bash 
SECRET_KEY =
DATABASE_NAME= 
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

```

#### starting the server
In Develoment 

```bash 
python manage.py runserver --settings=advertisement.settings.dev
```

In production

```bash
python manage.py runserver 0.0.0.0:8000 --settings=advertisement.settings.prod
```

### Usage
To use the API, make HTTP requests to the appropriate endpoint with the desired parameters. The API will return a JSON response with the requested data.

