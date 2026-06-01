# Docker Setup für Echo Server

## Übersicht

Dieses Projekt enthält alles Notwendige, um den Echo Server als Docker-Container zu starten.

### Dateien

- **Dockerfile**: Multi-stage build für optimale Größe und Performance
- **.dockerignore**: Schließt unnötige Dateien vom Build aus
- **docker-compose.yml**: Vereinfachte Konfiguration für Docker Compose

## Schnellstart

### Option 1: Docker Compose (Empfohlen)

```bash
# Image bauen und Container starten
docker-compose up -d

# Logs anschauen
docker-compose logs -f echo-server

# Container stoppen
docker-compose down
```

### Option 2: Docker CLI

#### Image bauen
```bash
docker build -t echo-server:latest .
```

#### Container starten
```bash
docker run -d \
  --name echo-server \
  -p 8000:8000 \
  echo-server:latest
```

#### Logs anschauen
```bash
docker logs -f echo-server
```

#### Container stoppen
```bash
docker stop echo-server
docker rm echo-server
```

## Verwendung

Der Server läuft auf `http://localhost:8000`

### Endpunkte

- **GET `/`**: Welcome-Nachricht und verfügbare Endpunkte
- **GET `/echo-get?param1=value1&param2=value2`**: Echo von Query-Parametern
- **POST `/echo-post`**: Echo von JSON-Body
- **GET `/docs`**: Swagger UI Dokumentation

### Beispiele

```bash
# GET Request
curl "http://localhost:8000/echo-get?message=hello&value=123"

# POST Request
curl -X POST "http://localhost:8000/echo-post" \
  -H "Content-Type: application/json" \
  -d '{"message": "hello", "value": 123}'

# Dokumentation
curl http://localhost:8000/docs
```

## Image-Details

- **Base Image**: python:3.13-slim (klein und sicher)
- **Python Version**: 3.13
- **Benutzer**: Non-root Benutzer (appuser, UID 1000) für bessere Sicherheit
- **Port**: 8000
- **Health Check**: Eingebaut für automatische Überwachung
- **Größe**: Optimiert durch Multi-stage Build

## Umgebungsvariablen

Keine erforderlich, aber folgende sind optional:

- `LOG_LEVEL`: Logging Level (default: INFO)

## Sicherheit

- Non-root Benutzer läuft den Container
- Slim Python Image mit minimalen Dependencies
- Health Check für automatische Fehlerbehandlung

## Development mit Docker

Für Development mit Hot-Reload aktivieren Sie das Volume in `docker-compose.yml`:

```yaml
volumes:
  - ./app.py:/app/app.py
```

Und verwenden Sie das reload flag:

```yaml
command: python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Troubleshooting

### Port bereits in Verwendung
```bash
# Andere Port verwenden
docker run -p 9000:8000 echo-server:latest
```

### Container startet nicht
```bash
# Logs prüfen
docker logs echo-server

# Container in interaktivem Modus starten
docker run -it echo-server:latest bash
```

### Health Check schlägt fehl
- Stelle sicher, dass `requests` installiert ist (ist in den Dependencies)
- Prüfe die logs mit `docker logs`
