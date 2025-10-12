# Backend

## Overview

The `backend/` directory contains a REST API server for a thread application built with FastAPI and SQLModel.  
It exposes CRUD endpoints for two main resources—threads (`Thread`) and posts (`Post`)—supporting creation, retrieval, search, and deletion operations that serve requests coming from the frontend.  
Data is stored in a relational database accessed through SQLModel, and connections are configured via the `DATABASE_URL` environment variable.

## Setup

1. **Prerequisites**  
   - Python 3.13 or later  
   - A database reachable via `DATABASE_URL` (e.g., PostgreSQL, SQLite)

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: `.venv\Scripts\activate`
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**  
   Set `DATABASE_URL` to point to your development database. Example (SQLite):  
   ```bash
   export DATABASE_URL="sqlite:///./keijiban.db"
   ```

5. **Start the development server**  
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Verify the server**  
   Open `http://127.0.0.1:8000/health` in a browser or with `curl` and confirm the response is `{"status": "healthy"}`.
