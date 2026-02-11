# Развёртывание MuseumApp (дополнительное задание)

## 1. Параллельный код (asyncio)

В проекте есть модуль **`museum/parallel_module.py`**: запросы к двум внешним API (JSONPlaceholder и Quotable) выполняются **параллельно** через `asyncio` и `aiohttp`. На странице «Внешние API» при установленном пакете `aiohttp` используется эта реализация; иначе — последовательный вызов из `services.py`.

Установка: `pip install aiohttp` (уже в `requirements.txt`).

---

## 2. Запуск API в production режиме

Локально (без Docker):

```bash
# Переменные для production
export DJANGO_DEBUG=0
export ALLOWED_HOSTS=localhost,127.0.0.1
export DJANGO_SECRET_KEY=ваш-секретный-ключ

python manage.py collectstatic --noinput
gunicorn MuseumApp.wsgi:application --bind 0.0.0.0:8000 --workers 2
```

Статика отдаётся через **WhiteNoise** (уже в `settings.py`). Для продакшена задайте `DJANGO_DEBUG=0` и свой `DJANGO_SECRET_KEY`.

---

## 3. Dockerfile

Сборка и запуск образа:

```bash
docker build -t museumapp .
docker run -p 8000:8000 -e DJANGO_DEBUG=0 -e DJANGO_SECRET_KEY=ваш-ключ museumapp
```

Внутри контейнера выполняются `migrate` и запуск **gunicorn**.

---

## 4. docker-compose (локальный запуск)

Запуск проекта с сохранением БД в volume:

```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000

**Публикация образа для преподавателя (Docker Hub):**

```bash
docker-compose build
docker tag museumapp_web:latest ВАШ_ЛОГИН/museumapp:latest
docker push ВАШ_ЛОГИН/museumapp:latest
```

Преподаватель может запустить так:

```bash
docker run -p 8000:8000 ВАШ_ЛОГИН/museumapp:latest
```

(при необходимости передать `-e DJANGO_SECRET_KEY=...` и т.п.)

---

## 5. Развёртывание в облаке

Рекомендуется сначала изучить бесплатные квоты, чтобы не выходить на платные тарифы.

### Бесплатные квоты (ориентировочно)

| Провайдер | Бесплатный уровень |
|-----------|--------------------|
| **Heroku** | Нет бесплатного tier с 2022; платные планы от ~$5/мес |
| **Railway** | Около $5 кредитов в месяц, затем оплата |
| **Render** | Бесплатный web-сервис (spin down при неактивности), бесплатная БД |
| **Fly.io** | Небольшие бесплатные ресурсы (VM, объём) |
| **AWS** | Free tier 12 месяцев (EC2, RDS и др. — с ограничениями) |
| **GCP** | Кредиты при регистрации, бесплатный tier с лимитами |
| **Azure** | Кредиты при регистрации, бесплатные сервисы с лимитами |

### Heroku (если используете платный план)

1. Установите [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. В корне проекта создайте **Procfile**:
   ```
   web: gunicorn MuseumApp.wsgi:application --bind 0.0.0.0:$PORT
   ```
3. Укажите версию Python в **runtime.txt**:
   ```
   python-3.12.0
   ```
4. В админке Heroku задайте переменные: `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS` (ваш домен и `*.herokuapp.com`), `DJANGO_DEBUG=0`.
5. Деплой: `git push heroku main` (или через GitHub интеграцию).

### Render

1. Подключите репозиторий на [render.com](https://render.com).
2. New → Web Service, укажите репозиторий и корень проекта (папка с `manage.py`).
3. Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput`.
4. Start: `gunicorn MuseumApp.wsgi:application --bind 0.0.0.0:$PORT`.
5. В Environment добавьте `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS`, `DJANGO_DEBUG=0`.

### Railway

1. [railway.app](https://railway.app) → New Project → Deploy from GitHub.
2. Укажите корень проекта, добавьте переменные окружения.
3. В настройках сервиса задайте команду запуска: `gunicorn MuseumApp.wsgi:application --bind 0.0.0.0:$PORT`.

Во всех вариантах в **ALLOWED_HOSTS** нужно указать хост, который выдаёт облако (например, `yourapp.render.com`, `yourapp.railway.app`).
