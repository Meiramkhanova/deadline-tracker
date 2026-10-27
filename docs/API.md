# Deadline Tracker API Documentation

Base URL: `http://localhost:8000/api`

All request and response bodies use JSON (`Content-Type: application/json`).

## Resource: Deadline

| Field        | Type     | Writable | Description                                      |
|--------------|----------|----------|--------------------------------------------------|
| `id`         | integer  | no       | Auto-generated primary key                       |
| `title`      | string   | yes      | Deadline title (max 200 characters)              |
| `subject`    | string   | yes      | Course / subject name (max 100 characters)       |
| `due_at`     | datetime | yes      | Due date-time in ISO 8601 format                 |
| `is_done`    | boolean  | yes      | Whether the deadline is completed (default `false`) |
| `days_left`  | integer  | no       | Days remaining until `due_at` (can be negative)  |
| `created_at` | datetime | no       | Timestamp when the record was created            |

---

## Endpoints

### 1. List deadlines

- **Method:** `GET`
- **URL:** `/api/deadlines/`
- **Description:** Returns all deadlines ordered by `due_at` (nearest first).

**Response `200 OK`:**

```json
[
  {
    "id": 1,
    "title": "Docker Compose homework",
    "subject": "Web Development",
    "due_at": "2026-10-17T23:59:00+05:00",
    "is_done": false,
    "days_left": 5,
    "created_at": "2026-10-10T12:00:00+05:00"
  }
]
```

---

### 2. Get deadline by ID

- **Method:** `GET`
- **URL:** `/api/deadlines/{id}/`
- **Description:** Returns a single deadline by its ID.

**Response `200 OK`:** same object shape as above.

**Response `404 Not Found`:** deadline with the given ID does not exist.

---

### 3. Create deadline

- **Method:** `POST`
- **URL:** `/api/deadlines/`
- **Description:** Creates a new deadline.

**Request body:**

```json
{
  "title": "Docker Compose homework",
  "subject": "Web Development",
  "due_at": "2026-10-17T23:59:00+05:00",
  "is_done": false
}
```

`is_done` is optional (defaults to `false`).

**Response `201 Created`:** the created deadline object (includes `id`, `days_left`, `created_at`).

**Response `400 Bad Request`:** validation error (missing/invalid fields).

---

### 4. Update deadline (full)

- **Method:** `PUT`
- **URL:** `/api/deadlines/{id}/`
- **Description:** Replaces all writable fields of an existing deadline.

**Request body:**

```json
{
  "title": "Docker Compose homework (updated)",
  "subject": "Web Development",
  "due_at": "2026-10-20T23:59:00+05:00",
  "is_done": false
}
```

**Response `200 OK`:** the updated deadline object.

**Response `404 Not Found`:** deadline does not exist.

---

### 5. Partial update deadline

- **Method:** `PATCH`
- **URL:** `/api/deadlines/{id}/`
- **Description:** Updates only the fields provided in the request body.

**Request body example:**

```json
{
  "is_done": true
}
```

**Response `200 OK`:** the updated deadline object.

---

### 6. Delete deadline

- **Method:** `DELETE`
- **URL:** `/api/deadlines/{id}/`
- **Description:** Deletes a deadline by ID.

**Response `204 No Content`:** successfully deleted (empty body).

**Response `404 Not Found`:** deadline does not exist.
