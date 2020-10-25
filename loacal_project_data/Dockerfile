FROM python:3.6

WORKDIR /usr/src/app
RUN mkdir volume

COPY ./docker_data . 

RUN pip install -r requirements.txt




CMD  python fahla.py
