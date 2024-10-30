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


## Instalación de Todo sqlite file

data_db/ToDo.sqlite
```sqlite
create table Todo
(
    id       integer not null
        constraint Todo_pk
            primary key autoincrement,
    text     TEXT,
    complete INT
);
```
## Correr localmente
    
```bash
flask run
```


## Parámetros .env
 
```bash
NINJA_FORM_SOURCE=XXXXXXXXXXXXXXXX
NINJA_FORM_KEY=XXXXXXXXXXXXXXXX
USER_1=XXXXXXXXXx
PASSWORD_1=XXXXXXXX
```
### Descripción de los parámetros:
NINJA_FORM_SOURCE: Es la URL de Ninja Forms ex. https://ninjaforms.com/wp-json/ninja-forms-scheduled-exports/v1/submission-export/
NINJA_FORM_KEY: Es la Key de acceso a Ninja Forms
USER_1: Es el usuario de Basic HTTP Auth
PASSWORD_1: Es la contraseña de Basic HTTP Auth


## Correr con Docker en producción

Construye y ejecuta la imagen de Docker
```bash
docker-compose -p flask_app_24e_app up -d
```

## Parar Docker

```bash
docker-compose -p flask_app_24e_app down
```
