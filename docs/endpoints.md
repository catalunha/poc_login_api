## Requisitos desta api

### ~/user/create/
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

### ~/user/token/
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

### ~/user/resetpassword/
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

### ~/user/newpassword/
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

### ~/user/me/
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

### ~/profile/:id/
* ações com autenticação
* frontend envia Token JWT e REST para profile/
* frontend envia Token JWT e REST para profile/:id/
* api responde com dados