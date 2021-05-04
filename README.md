# test_task_course
Завдання для Yalantis Python School 

Deploying project on Windows
  - python -m pip install virtualenv
  - virtualenv .env
  - cd .env/Scripts/
  - ./activate
  - cd ../../
  - python -m pip install -r requirements.txt
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver

For tests run:
  - python manage.py test
