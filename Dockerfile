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
    && apt-get install -y build-essential libpq-dev gcc python3-distutils \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# Copy project
COPY . /app/

# Set Django settings module explicitly (corrected)
ENV DJANGO_SETTINGS_MODULE=HumanAction.settings

# Collect static files (allow failure during build)
RUN python manage.py collectstatic --noinput || true

# Run the application
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
