
## Kaizntree Challenge (Back end) 

### Pre-requisite
Make sure you have Postgres (version 16 or above) install on your system.
Optinally, you can use PgAdmin tool to interact with database and tables.

### Local Setup Steps

Create Python Virtual Environment
```python -m venv env```

Activate Virtual Environment
```source env/bin/activate```

Install the project requirements
```pip install -r requirements.txt```


Before running the server, make sure your database contains latest migrations applied,
```python manage.py migrate```
To server the Django Server on Local
```python manage.py runserver```

To create a new migration file
```python manage.py makemigrations```

### Tests
To run all tests present in the codebase: ```pytest```
To check coverage for the code: ```pytest --cov=dashboard```

### API Documentation

To check the API Specs: ```http://127.0.0.1:8000/redoc/```
To check the Swagger Doc: ```http://127.0.0.1:8000/swagger/```