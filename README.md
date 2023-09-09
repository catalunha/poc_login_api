# poc_login_api

Backend do POC para testar login

Usando:
* JWT

O frontend deste app é poc_login

## Requisitos desta api

### [Ok] register
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

### [Ok] login
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

### reset password
* ações sem autenticação
* frontend envia POST para ~/user/resetpassword/
```json
{
  "username":"u1@gmail.com",
}
```
* api registra username e numero no bd de numeros
* api envia email com numero para conferencia
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
* api registra ate 3 tentativas se numero e username nao conferem. status = 406 Not Acceptable
status = 406 Not Acceptable
```json
{
  "attempt":1
}
```
* api retorna status = 400 Bad Request se username e numero inexistentes no bd ou maior que tentativas. 
status = 400 Bad Request
```json
{}
```
* frontend tem q enviar username novamente

### get me
* ações com autenticação
* frontend envia token para get /me
```json
{
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODM3NTE1LCJpYXQiOjE2OTM4MzM5MTUsImp0aSI6IjViNzllYzhkOGM2ZDRlYTE4YzRiMGY2ZjkyZjA4YjY3IiwidXNlcl9pZCI6MTJ9.NMkzD8JyC5hM7WV18Tc3Ej8zBLla1dAbCccnQtrDzbI"
}
```
* api responde com dados de user logado
```json
{
  "id":1,
  "username":"u1@gmail.com",
}
```

### get profile
* ações com autenticação
* frontend envia token e get profile/:id/
* api responde com dados
```json
{
  "id":1,
  "user":10,
  "username":"u1@gmail.com",
  "is_active":true,
  "office":["boss","sec"],
  "nickname":"a",
  "photo":"bucket/a.png",
  "phone":"63992304757",
}
```
* frontend envia token e POST para profile/:id/edit
* apenas usuario owner pode atualizar [nickname, photo, phone, name,] 
```json
{
  "id":1,
  "nickname":"a",
  "photo":"~/a.png",
  "phone":"123",
  "name":"A",
}
```
* frontend envia token e POST para profile/:id/config
* apenas profile com office=boss pode atualizar outro profile em [is_active, office(boss,sec,fin,admin),]
```json
{
  "id":1,
  "is_active":true,
  "office":["boss","sec"],
}
```
## Getting Started
$
python manage.py runserver 192.168.10.113:8000