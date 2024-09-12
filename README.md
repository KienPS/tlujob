# TLU JOB API
This is for demo only

## Requirements
1. Python 3
2. SQLite3

## Setup

1. Clone the repository
2. Create a virtual environment (recommended)
3. Install the requirements: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser (for access to admin site): `python manage.py createsuperuser` (If there's warning about weak password, ignore it by typing `y` and then `Enter`)

## Start the server:
```commandline
python manage.py runserver
```
Now go to https://localhost:8000/api/schema/swagger-ui/ to see the API schema
Go to https://localhost:8000/admin/ for admin site

## When repo got update(s)
Be sure to re-install the requirements and run migrations again