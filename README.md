Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

Install project dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Create a superuser account:
python manage.py createsuperuser

Start the development server:
python manage.py runserver

 Django project should now be up and running at http://127.0.0.1:8000/.

Usage:

particularly the three templates: Register, Login, and Home.

Features

The main features of your Django project:

User registration and authentication.
User login and session management.

Technologies Used
Python
Django
HTML/CSS
