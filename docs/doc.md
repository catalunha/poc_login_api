ultima aula 305

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

(venv) catalunha@pop-os:~/myapp/pocs/poc_login_api$ python manage.py runserver 192.168.10.113:8000

nao esqueça de habilitar a leitura do .env colocando em manage.py
```
from dotenv import load_dotenv
def main():
    load_dotenv()
    ...
```


ToRead:
Outra forma de criar profile sem usar signals
https://stackoverflow.com/questions/50204365/django-drf-create-user

https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8
https://medium.com/django-rest/logout-django-rest-framework-eb1b53ac6d35
https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
https://medium.com/django-rest/many-to-many-relationship-manytomanyfield-9b8201d879ab
https://medium.com/django-rest

Read:


# .vscode/settings.json

```json
{
  "python.analysis.typeCheckingMode": "basic",
  "python.defaultInterpreterPath": "venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8", // ms-python.python
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.formatOnType": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "editor.defaultFormatter": "ms-python.autopep8", // ms-python.python
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.formatOnType": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```