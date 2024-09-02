pip install django
pip install djangorestframework
pip install psycopg2

Commands to create project and app
--------------------------------------
django-admin startproject <project name>
python manage.py startapp <REST API>


## DB connections
------------------
// Just create a postgre database and give 'NAME' here.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Crud_app', 
        'USER': 'postgres',
        'PASSWORD': '9658',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

## Model creation steps
-------------------------
python manage.py makemigrations <API APP name>
python manage.py migrate


## Run App API
python manage.py runserver

