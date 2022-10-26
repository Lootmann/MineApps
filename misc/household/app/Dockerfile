# building
FROM python:3.10-buster as builder

WORKDIR /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install -U pip && pip install -r /code/requirements.txt

# multi-staged builder
FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY . /code/
