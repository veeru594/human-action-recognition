# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc python3-distutils \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# Copy all files
COPY ./main/Code /app/HumanAction


# 👇 Set the correct DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=HumanAction.HumanAction.settings

# 👇 Skip collectstatic temporarily (optional, to avoid breaking)
RUN python manage.py collectstatic --noinput || true

# 👇 WSGI run path updated properly
CMD gunicorn HumanAction.wsgi:application --bind 0.0.0.0:$PORT
