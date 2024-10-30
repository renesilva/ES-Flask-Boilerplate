# syntax=docker/dockerfile:1

FROM python:3.10.14-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# CMD [ "python3", "run.py"]
CMD gunicorn --bind 0.0.0.0:8888 run:app
