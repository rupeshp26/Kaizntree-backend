# Backend

## Overview

This project is a Django-based application with features including [provide a brief overview of the project]. Below are the setup steps and relevant information for developers.

### Pre-requisite

Make sure you have Postgres (version 16 or above) installed on your system. Optionally, you can use PgAdmin tool to interact with the database and tables.

### Local Setup Steps

1. **Create Python Virtual Environment:**
    ```bash
    python -m venv env
    ```

2. **Activate Virtual Environment:**
    ```bash
    source env/bin/activate
    ```

3. **Install the project requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Database Migrations:**
    Before running the server, make sure your database contains the latest migrations applied.
    ```bash
    python manage.py migrate
    ```

5. **Run the Django Server locally:**
    ```bash
    python manage.py runserver
    ```

6. **Create a new migration file:**
    ```bash
    python manage.py makemigrations
    ```

### Tests

- **Run all tests:**
    ```bash
    pytest
    ```

- **Check coverage for the code:**
    ```bash
    pytest --cov=dashboard
    ```

### API Documentation

- **Check the API Specs:**
    [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

- **Check the Swagger Doc:**
    [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

### Remote API Endpoints

You can use the following endpoints on the remote server:

- [https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/items](https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/items)

- User login: [https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/login/](https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/login/)

- User registration: [https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/register/](https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/register/)

- Create new category: [https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/categories/create/](https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/categories/create/)

- Create new item: [https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/items/create/](https://desolate-cliffs-97298-f04975de2abc.herokuapp.com/api/items/create/)

