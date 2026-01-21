# User-Activity-Data-Pipeline -> FastAPI Service

Production-style backend service built with **FastAPI**, demonstrating clean architecture, dependency injection, and robust error handling.

> Цель проекта — показать уровень **Middle Python Backend Developer** и умение строить масштабируемые сервисы.

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- Dependency Injection (FastAPI Depends)
- Middleware
- Custom Exception Handlers
- Logging
- External REST APIs
- Clean Architecture principles

---

## What This Project Demonstrates

- ✅ Clean separation of concerns  
- ✅ Dependency Injection without frameworks  
- ✅ Pure business logic isolated from IO  
- ✅ Centralized error handling  
- ✅ Health-checks for external dependencies  
- ✅ Production-style project structure  

---

## Business Logic Overview

The service aggregates data from external APIs:
- **Users API**
- **Posts API**

Based on this data, it provides:
- users list
- posts list
- users activity analytics
- top active users
- health and dependency checks

External APIs:
- `jsonplaceholder.typicode.com/users`
- `jsonplaceholder.typicode.com/posts`

---

## 🏗 Architecture Overview

app/
├── api/ # HTTP layer (FastAPI routers)
│ └── routes/
├── core/ # Config & Dependency Injection
├── services/
│ ├── clients.py # External API clients
│ ├── processor.py # Pure business logic (no IO)
│ └── service.py # Use cases / orchestration
├── exceptions/ # Domain exceptions & handlers
├── middleware/ # Custom middleware
├── models/ # Pydantic schemas
├── utils/ # Logging
└── main.py # Application entrypoint


## Architectural Principles

### Separation of Concerns

| Layer | Responsibility |
|-----|----------------|
| `clients` | Fetch data from external APIs |
| `processor` | Pure business logic |
| `service` | Use-case orchestration |
| `dependencies` | Dependency composition |
| `routes` | HTTP transport layer |

➡️ **Business logic does not depend on FastAPI, HTTP, or external services.**

---

## 🔌 Dependency Injection

Dependencies are composed explicitly via FastAPI `Depends`.

```python
@router.get("/activity")
def get_activity(
    service: UserActivityService = Depends(get_user_activity_service)
):
    return service.get_users_activity()

## Error Handling

# Custom domain exceptions
class ExternalServiceUnavailable(Exception):
    pass

class DataProcessingError(Exception):
    pass

# Centralized handlers

All domain errors are converted into HTTP responses outside of routers, keeping controllers thin.

## Middleware

# Timing middleware

Custom timing middleware:

- logs each request
- adds execution time to response headers
Example:

Пример: X-Process-Time: 0.0123

## Health-check

# Dependencies health
    GET /health/dependencies

Response:
    {
  "status": "ok",
  "dependencies": {
    "users_api": "unavailable",
    "posts_api": "ok"
  }
}
Health-check никогда не падает, даже если внешние сервисы недоступны.

## Pydantic v2

Используются:

- BaseModel
- EmailStr
- field_validator

Пример схемы:
    class UserActivity(BaseModel):
        user_id: int
        name: str
        email: EmailStr
        city: str
        posts_count: int

## Configuration

Environment variables are loaded via pydantic-settings.
.env (project root):

    URL_USER=https://jsonplaceholder.typicode.com/users
    URL_POSTS=https://jsonplaceholder.typicode.com/posts

Загрузка конфигурации через pydantic-settings.

## Run Locally

    pip install -r requirements.txt
    uvicorn app.main:app --reload

Swagger UI:
    http://127.0.0.1:8000/docs


## API Endpoints

Метод	URL	Описание
GET	/users	Получить пользователей
GET	/posts	Получить посты
GET	/users/activity	Активность пользователей
GET	/users/activity/top?limit=5	Топ активных пользователей
GET	/health	Health-check
GET	/health/dependencies	Проверка внешних API


## Project Goal

This project was built to demonstrate:
- backend architectural thinking
- clean Python code
- production-ready FastAPI patterns
- readiness for real-world backend development