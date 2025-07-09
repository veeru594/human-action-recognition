# Use official Python image
FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install required OS packages
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev gcc python3-distutils

# Install Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

# Copy full project into container
COPY . /app/

# 🔥 THIS is the fix
ENV DJANGO_SETTINGS_MODULE=Code.HumanAction.settings
ENV PYTHONPATH=/app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the server
CMD gunicorn Code.HumanAction.wsgi:application --bind 0.0.0.0:$PORT
