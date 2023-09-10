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
9T#2C7F+W$NAmq+10
123456qwerty!@#$%&
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


## Requisitos desta api

### [Ok] User Create
* ações sem autenticação
* frontend envia POST para ~/user/create/
```json
{
  "username":"u1@gmail.com",
  "password":"123qwe!@#"
}
```
* api check
  * se ja existe username
  * se username é email válido. Pois username tem q ser email
  * se senha maior que 6 digitos e diferente de username
* api cria usuario
* api cria profile, veja que nickname é parte do username=email
* api retorna
```json
{
  "user":1
}
```

### [Ok] User Login
* ações sem autenticação
* frontend envia POST para ~/token/
```json
{
  "username":"u1@gmail.com",
  "password":"123qwe!@#"
}
```
* api retorna
```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzkyMDMxNSwiaWF0IjoxNjkzODMzOTE1LCJqdGkiOiIyYjYyMmNjNDQ1Mzk0YTI1YmFkMDAzMjUzNmUyODU3MiIsInVzZXJfaWQiOjEyfQ.SqOByEBzC0lW1q-uDBwgGPOIZBRAImKyC-uk7K2gO00",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODM3NTE1LCJpYXQiOjE2OTM4MzM5MTUsImp0aSI6IjViNzllYzhkOGM2ZDRlYTE4YzRiMGY2ZjkyZjA4YjY3IiwidXNlcl9pZCI6MTJ9.NMkzD8JyC5hM7WV18Tc3Ej8zBLla1dAbCccnQtrDzbI"
}
```

### User Reset password
* ações sem autenticação
* frontend envia POST para ~/user/resetpassword/
```json
{
  "username":"u1@gmail.com",
}
```
* api registra userId, username e numero no bd de numeros
* api envia email com numero para conferencia
* api responde vazio com http=200
```json
{}
```
* cliente confere seu email e anota numero
* frontend envia POST para ~/user/newpassword/
```json
{
  "username":"u1@gmail.com",
  "number":123,
  "password":"123qwe!@#",
}
```
* api atualiza senha se numero e username conferem. apaga o obj do bd de numeros
* api retorna sucesso status = 200
status = 200 OK
```json
{}
```
* api registra ate 3 tentativas se numero e username nao conferem. status = 412 se ultrapassar 3 tentativas
```json
{}
```
* api retorna status = 400 Bad Request se username e numero inexistentes no bd ou maior que tentativas. 
status = 400 Bad Request
```json
{}
```
* frontend tem q enviar username novamente

### [Ok] User Me
* ações com autenticação
* frontend envia GET para /user/me/
```json
{
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODM3NTE1LCJpYXQiOjE2OTM4MzM5MTUsImp0aSI6IjViNzllYzhkOGM2ZDRlYTE4YzRiMGY2ZjkyZjA4YjY3IiwidXNlcl9pZCI6MTJ9.NMkzD8JyC5hM7WV18Tc3Ej8zBLla1dAbCccnQtrDzbI"
}
```
* api responde com dados
```json
{
	"user": {
		"id": 9,
		"username": "a1@gmail.com",
		"is_active": true
	},
	"profile": {
		"id": 1,
		"user": 9,
		"username": "a1@gmail.com",
		"nickname": null,
		"name": null,
		"photo": null,
		"phone": null,
		"is_active": false
	}
}
```

### Profile
* ações com autenticação
* frontend envia Token JWT e REST para profile/
* frontend envia Token JWT e REST para profile/:id/
* api responde com dados