# SomnoTech
Backend para la aplicacion Somnotech desarrollada por el grupo TechSparks
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

