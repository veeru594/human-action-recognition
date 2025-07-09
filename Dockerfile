# Use official slim Python base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc python3-distutils

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# Copy the entire project
COPY . /app/

# Tell Python where to find the Django project
ENV PYTHONPATH=/app/main/Code

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
