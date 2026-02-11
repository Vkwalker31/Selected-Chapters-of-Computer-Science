# Dockerfile для MuseumApp (production)
# Сборка: docker build -t museumapp .
# Запуск: docker run -p 8000:8000 -e DJANGO_DEBUG=0 museumapp

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG=0
WORKDIR /app

# Зависимости системы (для сборки, если понадобятся)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Статика (для WhiteNoise)
RUN python manage.py collectstatic --noinput --clear 2>/dev/null || true

EXPOSE 8000

# Миграции и запуск gunicorn в production режиме
CMD sh -c "python manage.py migrate --noinput && gunicorn MuseumApp.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2"
