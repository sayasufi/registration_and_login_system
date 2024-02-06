# pull official base image
FROM python:3.11.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# install psycopg2 dependencies
RUN apk update && apk --no-cache add postgresql-dev gcc python3-dev musl-dev

# copy project
COPY . .

