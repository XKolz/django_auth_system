# Django Project with Custom User Model and JWT Authentication

This project is a Python (Django) application that uses a custom user model with email authentication and JWT for secure authentication. The application is set up to be deployed on Render with Supabase as the PostgreSQL database.

## Table of Contents

- [Development Setup](#development-setup)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Database Migrations](#database-migrations)
  - [Running the Server](#running-the-server)
- [Production Deployment](#production-deployment)
  - [Environment Configuration](#environment-configuration)
  - [Render Setup](#render-setup)
- [Testing Endpoints](#testing-endpoints)
  - [Register User](#register-user)
  - [Login User](#login-user)
  - [Refresh Token](#refresh-token)
  - [Get User Details](#get-user-details)

## Development Setup

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/XKolz/django_auth_system
   cd django_auth_system

2. Create a virtual environment and activate it:
    ```bash
        python -m venv myenv
        source myenv/bin/activate  # On Windows, use (`myenv\Scripts\activate`)

3. Install the required packages:

        pip install -r requirements.txt

- N.B: Run 
        ```bash
            "pip install django" 
            "djangorestframework" 
            "djangorestframework-simplejwt" 
            "psycopg2-binary" 

-if you have installed the dependencies already.

4. Configuration
a. Create environment files:
-.env.development:
    ```bash
        SECRET_KEY=your_local_secret_key
        DEBUG=True
        ALLOWED_HOSTS=localhost,127.0.0.1
        DATABASE_URL=postgres://db_user:2415@localhost:5432/dn_name


-.env.production:
    ```bash
        SECRET_KEY=your_production_secret_key
        DEBUG=False
        ALLOWED_HOSTS=your-production-domain.com
        DATABASE_URL=postgres://your_db_user:your_db_password@db.your_supabase_project.supabase.co:5432/your_db_name

5. Update settings.py to use environment variables and also if you want to connect to one or the another
- For Development
        ```bash
        export ENV_FILE=.env.development

- For Production
        ```bash
        export ENV_FILE=.env.production   

6. Create a Procfile for deployment:
    ```bash
    web: gunicorn myproject.wsgi

7. Database Migrations
Make migrations and migrate:
        ```bash
        python manage.py makemigrations accounts
        python manage.py migrate

8. Collect static files:
    ```bash
        python manage.py collectstatic

## If you needd a superuser (which is good)
- Create a superuser to access the Django admin:
    ```bash
        python manage.py createsuperuser

9. Running the Server
Run the development server:
    ```bash
        python manage.py runserver

## Testing on your endpoints on POSTMAN/Swagger and likes:

- Register a users:POST
- http://127.0.0.1:8000/api/accounts/register/

        {
            "email": "34user@example.com",
            "password": "password123",
            "first_name": "3John",
            "last_name": "Doe"
        }

- Login existing users:POST
- http://127.0.0.1:8000/api/accounts/login/

            {
            "email": "34user@example.com",
            "password": "password123"
            }

- Get authenicated user's details:GET
- http://127.0.0.1:8000/api/accounts/user/

Response:

        {
            "id": 1,
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe"
        }


## For Production Setup

- Set environment variables in Render based on .env.production:

        SECRET_KEY=
        DEBUG=
        ALLOWED_HOSTS=
        DATABASE_URL=

Render Setup
Create a Render account and new web service:
1. Connect your GitHub repository.
2. Set the build command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
3. Set the start command: gunicorn myproject.wsgi

Deploy the application:
- Render will automatically build and deploy your application.

- Testing on your endpoints on POSTMAN/Swagger and likes
- POST
- https://djangotesting.onrender.com/api/accounts/register/

        {
        "email": "user@example.com",
        "password": "password123",
        "first_name": "John",
        "last_name": "Doe"
        }
- POST 
- https://djangotesting.onrender.com/api/accounts/login/

        {
        "email": "user@example.com",
        "password": "password123"
        }

- POST 
- https://djangotesting.onrender.com/api/accounts/token/refresh/

        {
        "refresh": "your_refresh_token"
        }

- GET 
- https://djangotesting.onrender.com/api/accounts/user/

- Authorization: Bearer your_access_token

        {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
        }


## FYI. Configure Django Settings
a. Update settings.py to include installed apps:

        INSTALLED_APPS = [
            ...
            'rest_framework',
            'rest_framework_simplejwt',
            'accounts',
        ]

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ),
        }

        AUTH_USER_MODEL = 'accounts.User'


pipreqs . for creating requirements.txt



<!-- Please discard this for now but they are useful information too -->
## To Get started with creating restful APIs with Django

1. first, Install/Configure Django Rest Framework (DRF), helps build the RESTful API:

        pip install django djangorestframework
        django-admin startproject <project_name>
        cd <project_name>
        django-admin startapp <app_name>

2. Add rest_framework & '<app_name>' & 'rest_framework.authtoken'  to INSTALLED_APPS:

        INSTALLED_APPS = [
            ...others
            'rest_framework',
            'myapp',
            'rest_framework.authtoken',
        ]

3. Database Configuration
We configured the project to use PostgreSQL instead of the default SQLite:
Install 

        pip install psycopg2-binary
        pip install psycopg

NB:You can choose between psycopg2-binary or psycopg.

Update DATABASES settings in  <project_name>/settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

## Important: If you don't have your python env 
If you are not already using a virtual environment, it is a good practice to create one to manage dependencies:

        python -m venv <myenv>
        source <myenv>/bin/activate

4. Run Migrations
We ran the migrations to create the necessary database tables:

        Generate migration files: 
            python manage.py makemigrations
        Apply migrations: 
            python manage.py migrate

5. Create Serializers
We created serializers to convert Django model instances to JSON and validate data:

        Check the serializers.py in <app_name> 

6. Create Views
We created views to handle user registration and login:

        Check the views.py in <app_name>

7. Set Up URLs
We defined URL patterns to route requests to the appropriate views:

        Check the urls.py in <app_name>

## Include <app_name> URLs in the main urls.py in <project_name>:
        Check the urls.py in <project_name>

8. Handle Root URL: To handle the root URL and prevent a 404 error:

        Create a simple root view in <app_name>/views.py:
        Check the views.py in <app_name>

        Update <project_name>/urls.py to include the root URL:
        Check the urls.py in <project_name>:


curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'

        {
            "username": 
            "testuser", 
            "email": "test@example.com", 
            "password": "password123"
        }


curl -X POST http://127.0.0.1:8000/api/login/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}'

        {
            "username": "testuser", 
            "password": "password123"
        }


if you clone my project, you need to run the
        pip install -r requirements.txt
to install the dependencies needed for this app

A common practice is to list all your project dependencies 
in a requirements.txt file. You can create this file by running:
        pip freeze > requirements.txt



Now to host your django project
Install Gunicorn:

Gunicorn is a Python WSGI HTTP Server for UNIX. It will serve your Django application.
pip install gunicorn

A Procfile is a text file in the root directory of your application that tells Render how to run your application.

web: gunicorn myproject.wsgi


4. Create a runtime.txt:

Specify the Python version you want to use by creating a runtime.txt file in the root directory of your project.


5.Configure settings.py:

Update your settings.py to support Render's environment:

Allow all hosts:
ALLOWED_HOSTS = ['*']

Configure static files:
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

Use dj-database-url to parse the database URL from environment variables:
pip install dj-database-url

import dj_database_url

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)




Set DEBUG to False for production:
DEBUG = False


Install whitenoise:

Whitenoise helps with serving static files.

pip install whitenoise


Update MIDDLEWARE in settings.py:
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware
]

Update STATICFILES_STORAGE:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'