# Use Python image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev gcc python3-distutils \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# 👇 copy only the subdirectory that contains your Django project
COPY main/Code/HumanAction /app

# 👇 point to correct Django settings
ENV DJANGO_SETTINGS_MODULE=HumanAction.settings

# 👇 only needed if you're using collectstatic (can skip for now)
RUN python manage.py collectstatic --noinput || true

# Run app
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
