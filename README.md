# Mudassar First Project

This is a slim Dockerized two-tier web application built with Flask and PostgreSQL.

## Run locally with Docker

1. Build and start services:
   ```bash
docker-compose up --build
```

2. Open the app:
   ```
http://localhost:3000
```

## API endpoints

- `GET /` — returns a welcome message and stored messages count
- `GET /messages` — returns all saved messages
- `POST /messages` — create a message with JSON `{ "text": "Hello" }`
- `GET /health` — basic service health check
