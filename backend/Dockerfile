# Базовый образ
FROM python:3.12-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей проекта
COPY backend/requirements.txt /app/requirements.txt

# Установка Python-зависимостей
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Копирование кода приложения
COPY backend /app/backend

# Команда по умолчанию
CMD ["gunicorn", "backend.ecommerce_project.wsgi:application", "--bind", "0.0.0.0:8000"]
