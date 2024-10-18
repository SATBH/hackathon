# SomnoTech
Backend para la aplicacion Somnotech desarrollada por el grupo TechSparks.
Se encuentra escrito en fastapi con python 3.12. La base de datos principal
esta escrita en postgresql, y la base de datos que manejara las mediciones del
dipositivo en nosql para poder ofrecer un servicio en tiempo real usando estos datos.

![Alt text](./logo.svg)

## Requerimientos del backend
    Nix
## Como iniciar en desarrollo
Dentro de la raiz del repositorio usar el comando
``` bash
nix-shell
```
Con esto accedera a una shell en el ambiente con las versiones de python y paquetes adecuada.
Una vez hecho esto, corra
``` bash
fastapi dev main.py
```
para correr la aplicacion

## Para crear la version de produccion
Correr

```bash
nix-build
```

# Librerias en Uso
* fastapi
* smtplib
* websockets
* uvicorn
* rich
* pyjwt
* passlib
* bcrypt
