# Используем официальный образ Python
FROM python:3.12-slim

# Установим необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория в контейнере
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем зависимости проекта через Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копируем исходный код проекта
COPY . .

# Укажем команду запуска сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]