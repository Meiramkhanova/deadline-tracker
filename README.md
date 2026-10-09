# Deadline Tracker

A small Django REST API for keeping track of study deadlines, running in Docker Compose with PostgreSQL.

## Services

| Service   | Image / build           | Description                                   |
|-----------|-------------------------|-----------------------------------------------|
| `backend` | `./backend/Dockerfile`  | Django + Django REST Framework, served by gunicorn on port 8000 |
| `db`      | `postgres:16-alpine`    | PostgreSQL database, data stored in the `pgdata` named volume |

Both services share the `app-net` network. The backend reaches the database by its service name `db` and starts only after the database passes its healthcheck.

## Run

```bash
cp .env.example .env   # then put your own secret key and password into .env
docker compose up --build
```

API: http://localhost:8000/api/deadlines/

## API

| Method | URL                | Description                                  |
|--------|--------------------|----------------------------------------------|
| GET    | `/api/deadlines/`  | List deadlines, nearest first, with `days_left` |
| POST   | `/api/deadlines/`  | Create a deadline                            |

Example request body:

```json
{
  "title": "Docker Compose homework",
  "subject": "Web Development",
  "due_at": "2026-10-17T23:59:00+05:00"
}
```

## Persistence check

```bash
docker compose down     # containers are removed, the pgdata volume stays
docker compose up -d
```

Previously created deadlines are still returned by `GET /api/deadlines/`. `docker compose down -v` removes the volume and the data with it.
