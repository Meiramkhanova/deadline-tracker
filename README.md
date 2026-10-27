# Deadline Tracker

A Django REST API for tracking study deadlines, containerized with Docker Compose and PostgreSQL.

## Architecture

| Service   | Image / build          | Description |
|-----------|------------------------|-------------|
| `backend` | `./backend/Dockerfile` | Django + DRF, served by gunicorn on port 8000 |
| `db`      | `postgres:16-alpine`   | PostgreSQL; data in the named volume `pgdata` |

Both services use the custom bridge network `app-net`. The backend connects to the database by the Compose service name `db` and starts only after the DB healthcheck passes.

Configuration is loaded from environment variables (see `.env.example`).

## Quick start

```bash
cp .env.example .env
# edit .env: set DJANGO_SECRET_KEY and POSTGRES_PASSWORD

docker compose up --build
```

API base: http://localhost:8000/api/deadlines/

## REST API

Full documentation: [docs/API.md](docs/API.md)

| Method | URL                     | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/api/deadlines/`       | List all deadlines       |
| GET    | `/api/deadlines/{id}/`  | Get deadline by ID       |
| POST   | `/api/deadlines/`       | Create a deadline        |
| PUT    | `/api/deadlines/{id}/`  | Full update              |
| PATCH  | `/api/deadlines/{id}/`  | Partial update           |
| DELETE | `/api/deadlines/{id}/`  | Delete a deadline        |

Example create body:

```json
{
  "title": "Docker Compose homework",
  "subject": "Web Development",
  "due_at": "2026-12-01T23:59:00+05:00",
  "is_done": false
}
```

## Postman

Import [`postman/Deadline_Tracker_API.postman_collection.json`](postman/Deadline_Tracker_API.postman_collection.json) into Postman.  
Collection variable `baseUrl` defaults to `http://localhost:8000/api`.  
**Create deadline** saves the new `id` into `deadlineId` for the other requests.

Suggested demo order: Create → List → Get by ID → PUT → PATCH → Delete.

## Project structure

```
deadline-tracker/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/          # Django settings, URLs, WSGI
│   └── deadlines/       # Model, serializers, views, migrations
├── docs/
│   └── API.md
├── postman/
│   └── Deadline_Tracker_API.postman_collection.json
├── compose.yaml
├── .env.example
└── README.md
```

## Docker concepts used

- **Dockerfile** — custom image for the backend (Python, dependencies, migrate + gunicorn)
- **Compose** — orchestrates `backend` + `db`
- **Network `app-net`** — service-to-service communication (`POSTGRES_HOST=db`)
- **Named volume `pgdata`** — persistent PostgreSQL data
- **Environment variables** — secrets and config via `.env` / `env_file`
- **Ports** — backend published as `${BACKEND_PORT:-8000}:8000`

## Persistence check

```bash
docker compose down      # containers removed; pgdata volume kept
docker compose up -d
```

Previously created deadlines remain. `docker compose down -v` removes the volume and the data.

## Submission note

Do **not** commit real `.env` files to a public GitHub repo. Submit working `.env` files separately as a zip, as required by the assignment. Use `.env.example` in the repository as a template.
