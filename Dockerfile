# Use an official Python runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
