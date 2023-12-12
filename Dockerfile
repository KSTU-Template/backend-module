FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./web /code/web