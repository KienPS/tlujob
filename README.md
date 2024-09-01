# TLU JOB API
This is for demo only

## Requirements
1. Python 3
2. SQLite3

## Setup

1. Clone the repository
2. Open a terminal in that directory
3. Create a virtual environment (recommended)
4. Install the requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`

## Start the server:
```commandline
python manage.py runserver
```
Now go to https://localhost:8000/api/schema/swagger-ui/ to see the API schema