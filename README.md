# Веб-сервис, хранящий информацию о сотрудниках компании в базе данных и реализующий CRUD эндпоинты.

## Фреймворк: FastAPI, сервер баз данных: PostgreSQL, Docker-контейнеризация.

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

Проект доступен по адресу http://0.0.0.0:8000

#### Документация API доступна по адресу http://0.0.0.0:8000/redoc