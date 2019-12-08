# notable_test


**This project was built using python 3.7.4 and Django 2.2.3. The database used is PostgreSQL **

1. Please create a virtualenv and install the requirements in reqs.txt
2. Please check the DATABASES in settings.py for setting up the Postgres connection accordingly
    1. createdb notable_test
    2. createuser -d -l -P -r -s notable_user
            Set `password` as the password
            
3. Clone the project from github
    1. Clone the project using
        git clone https://github.com/sahithi403/notable_test.git
    2. Install the project requirements
        1. cd notable_test
        2. pip install -r reqs.txt
    3. Run migrations
        python manage.py migrate
    4. Create a superuser for the django server using
            python manage.py createsuperuser
            username: django_admin
            password: password
    
4. Run the project
    python manage.py runserver
    You should see django server running at http://127.0.0.1:8000/
    
5. API endpoints
    1. For creating/deleting doctors, go to
    http://127.0.0.1:8000/rest/physicians/
    2. For creating/deleting appoinments go to
    http://127.0.0.1:8000/rest/appointments/
