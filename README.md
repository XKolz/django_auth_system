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
