# Flask App Atención al Cliente

## Instalación

Programas necesarios:

- Python 3.8 o superior

### Instalación con PyCharm

1. Descargar el proyecto e iniciar un nuevo proyecto utilizando la carpeta. PyCharm generará el ambiente venv.
2. Instalar los paquetes utilizados en requirements.txt

### Instalación con Visual Studio Code

https://code.visualstudio.com/docs/python/environments

### Instalación con otra herramienta

1. Descargar el proyecto.
2. Generar el ambiente con `python -m venv ./venv`
3. Activar el ambiente con `source ./venv/bin/activate`
4. Instalar los requerimientos con `pip install -r requirements.txt`


## Instalación de Todo sqlite file en caso de usar Models

data_db/ToDo.sqlite
```sqlite
create table Todo
(
    id integer not null
        constraint Todo_pk
            primary key autoincrement,
    text TEXT,
    complete INT
);
```
## Correr localmente
    
```bash
flask run
```


## Parámetros .env
 
```bash
USER_1=XXXXXXXXXx
PASSWORD_1=XXXXXXXX
```
### Descripción de los parámetros:
USER_1: Es el usuario de Basic HTTP Auth
PASSWORD_1: Es la contraseña de Basic HTTP Auth


## Correr con Docker en producción

Construye y ejecuta la imagen de Docker
```bash
docker-compose -p flask_app up -d
```

## Parar Docker

```bash
docker-compose -p flask_app down
```
