# Taski

A full-stack task management app — Django REST Framework backend + React frontend.

> **Note:** This is the local development version without Docker. For the containerised deployment version see [taski-docker](https://github.com/Shipovmax/taski-docker).

---

## Features

- **Task CRUD** — create, read, update, delete tasks via REST API
- **Completion toggle** — mark tasks as done/undone
- **Tab filtering** — All / Active / Completed tabs in the UI
- **Inline editing** — edit task title and description in a modal without page reload
- **CORS configured** — `django-cors-headers` enabled for local frontend dev

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django 3.2, DRF 3.12 |
| Frontend | React 18, JavaScript |
| Database | SQLite3 (dev) |

---

## Quick Start

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

API at `http://127.0.0.1:8000/api/tasks/`

### Frontend

```bash
cd frontend
npm install
npm start
```

UI at `http://localhost:3000`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/` | List all tasks |
| `POST` | `/api/tasks/` | Create task |
| `GET` | `/api/tasks/{id}/` | Get task |
| `PUT/PATCH` | `/api/tasks/{id}/` | Update task |
| `DELETE` | `/api/tasks/{id}/` | Delete task (returns deleted object) |

**Task model:**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

---

## Project Structure

```
taski/
├── backend/
│   ├── api/
│   │   ├── models.py       # Task model
│   │   ├── serializers.py  # TaskSerializer
│   │   └── views.py        # TaskView (ModelViewSet)
│   ├── backend/
│   │   └── settings.py     # Django config + CORS
│   └── requirements.txt
└── frontend/
    └── src/
        ├── App.js
        └── components/
            ├── TabList.js        # All / Active / Completed tabs
            ├── Task.js           # Single task item
            └── TaskEditModal.js  # Edit modal
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
