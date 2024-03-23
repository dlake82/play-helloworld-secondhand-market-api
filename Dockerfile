# Use an official Python runtime as a parent image
FROM python:3.12.2-slim-bullseye

# Set work directory
WORKDIR /app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y curl vim netcat
RUN apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Install poetry
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy project
COPY ./app /app/

ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE ${DJANGO_SETTINGS_MODULE}

EXPOSE 8000