

# History

catalunha@pop-os:~/myapp/pocs/poc_login_api$ python -m venv venv
criar git ignore
ativar git
catalunha@pop-os:~/myapp/pocs/poc_login_api$ source ./venv/bin/activate
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ 
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ pip install djangorestframework
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ pip freeze
asgiref==3.7.2
Django==4.2.4
djangorestframework==3.14.0
pytz==2023.3
sqlparse==0.4.4
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ django-admin startproject project .
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ django-admin startapp api
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ python manage.py makemigrations
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ python manage.py migrate
(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ python manage.py createsuperuser
Username (leave blank to use 'catalunha'): admin
Email address: 
Password: a
Password (again): a
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
