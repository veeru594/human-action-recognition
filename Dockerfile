# Use an official Python runtime with slim image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    python3-dev \
    python3-distutils \
    libatlas-base-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy Django project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (optional but useful if running locally)
EXPOSE 8000

# Start Gunicorn server
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
