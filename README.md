# Flask Base App

Este es un proyecto base de Flask con las siguientes características:

- Estructura de carpetas y archivos
- Configuración de Flask
- Configuración de Basic HTTP Auth
- Configuración de Models
- Configuración de Docker Compose

Los archivos están organizados basado en https://lepture.com/en/2018/structure-of-a-flask-project

## Instalación

Programas necesarios:

- Python 3.10 o superior

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

```bash
sqlite3 data_db/database.sqlite
```

```sqlite
CREATE TABLE ToDo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0
);
```

```
sqlite> .quit
```

## Correr localmente
    
```bash
python3 run.py
```


## Parámetros .env
 
```bash
FLASK_SECRET_KEY=XXXXXXXXXx
USER_1=XXXXXXXXXx
PASSWORD_1=XXXXXXXXXx

APP_CONTAINER_NAME=XXXXXXXXXx
NGINX_CONTAINER_NAME=XXXXXXXXXx
```
### Descripción de los parámetros:

USER_1: Es el usuario de Basic HTTP Auth
PASSWORD_1: Es la contraseña de Basic HTTP Auth
APP_CONTAINER_NAME: Es el nombre del contenedor de la aplicación
NGINX_CONTAINER_NAME: Es el nombre del contenedor de Nginx


## Correr con Docker en producción

Construye y ejecuta la imagen de Docker

```bash
docker-compose -p flask_app up -d
```

## Parar Docker

```bash
docker-compose -p flask_app down
```
