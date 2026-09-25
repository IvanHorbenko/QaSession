# QA Session Demo Project

Demo project for a QA team training session on using Claude Code (Jira MCP, Qase MCP, Postgres MCP, Playwright).

## Stack

- **Backend**: Python 3.12 + FastAPI + SQLAlchemy, connects to a local PostgreSQL database.
- **Frontend**: static HTML/JS pages (login, register, profile) that call the backend API.
- **Database**: PostgreSQL database `qa_session`, running on the local Homebrew Postgres service (no Docker required).

## Setup

### 1. Database

Requires a local PostgreSQL server already running (e.g. via `brew services start postgresql@16`).

```bash
createdb qa_session
python3.12 db/seed.py
```

### 2. Backend

```bash
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at http://localhost:8000, interactive docs at http://localhost:8000/docs.

### 3. Frontend

```bash
cd frontend
python3.12 -m http.server 5500
```

Open http://localhost:5500 in the browser.

## Seeded test users

| email                     | password       |
|---------------------------|----------------|
| john.doe@example.com      | Password123!   |
| jane.smith@example.com    | Password123!   |

User `john.doe@example.com` has id=1 in a fresh database.
