1. Set Up Django Project
a. Create a new Django project:
        django-admin startproject myproject
        cd myproject

b. Create a new Django app:
python manage.py startapp accounts

##Important
 python -m venv myenv 
 source myenv/bin/activate 
 pip install django 

2. Install Necessary Packages
a. Install Django REST framework and Simple JWT:
pip install djangorestframework djangorestframework-simplejwt

b. Install PostgreSQL adapter for Python:
pip install psycopg2-binary


3. Configure Django Settings
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

b. Configure PostgreSQL database settings in settings.py:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'your_db_host',
                'PORT': 'your_db_port',
            }
        }

5. Create Serializers
a. Define serializers in accounts/serializers.py:
python


8. Apply Migrations
Run migrations to create the necessary database tables:

        python manage.py makemigrations accounts
        python manage.py makemigrations admin
        python manage.py migrate


10. Verify the Setup
Create a superuser to access the Django admin:
python manage.py createsuperuser

b. Start the Django development server and verify the setup:
python manage.py runserver


11. Test Endpoints
Register a new user:
        curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
        -H "Content-Type: application/json" \
        -d '{
            "email": "user@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe"
            }'

login
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{
      "email": "user@example.com",
      "password": "password123"
    }'

refresh
curl -X POST http://127.0.0.1:8000/api/accounts/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
      "refresh": "your_refresh_token_here"
    }'


get user profile
curl -X GET http://127.0.0.1:8000/api/accounts/user/ \
-H "Authorization: Bearer your_access_token_here"
