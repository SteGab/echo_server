# Echo Server

Ein einfacher Python-basierter Echo-Server, der GET und POST Requests verarbeitet und die empfangenen Daten an den Client zurücksendet. Alle Requests werden über einen Logger protokolliert.

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Testing](#testing)
- [API Dokumentation](#api-dokumentation)
- [Deployment](#deployment)
- [Projektstruktur](#projektstruktur)
- [Technologie-Stack](#technologie-stack)
- [Weitere Informationen](#weitere-informationen)
- [Entwicklung und Beitragen](#entwicklung-und-beitragen)
- [License](#license)

## Features

- 🔄 **Echo-Funktionalität**: Sendet empfangene Daten im gleichen Format zurück
- 📝 **Logging**: Alle Requests werden auf der Konsole geloggt
- 🚀 **FastAPI**: Modernes, asynchrones Python-Web-Framework
- 📚 **Auto-Dokumentation**: Swagger UI verfügbar unter `/docs`
- ⚡ **ASGI-Server**: Uvicorn für hohe Performance

## Installation

### Voraussetzungen
- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (schneller Python Package Manager)

### Schritt 1: uv installieren (falls noch nicht vorhanden)

```bash
# Auf Windows mit pip
pip install uv

# Oder über Homebrew (macOS/Linux)
brew install uv
```

### Schritt 2: Abhängigkeiten installieren

```bash
uv sync
```

## Verwendung

### Server starten (lokal)

```bash
# Mit uv run (mit Hot-Reload für Entwicklung)
uv run uvicorn app:app --reload

# Oder direkt mit Python
uv run python app.py
```

Der Server läuft dann auf `http://127.0.0.1:8000`

### Server starten mit Docker/Podman

Für detaillierte Informationen zur Docker/Podman-Einrichtung siehe [DOCKER.md](./DOCKER.md)

```bash
# Mit Docker Compose (empfohlen)
docker-compose up -d

# Mit Podman Compose
podman compose up -d

# Logs anschauen
docker-compose logs -f echo-server
```

## Testing

### Abhängigkeiten installieren

```bash
# Alle Test-Abhängigkeiten installieren
uv sync --extra test
```

### Tests ausführen

```bash
# Alle Tests ausführen
uv run pytest

# Tests mit Ausgabe
uv run pytest -v

# Tests mit Coverage-Report
uv run pytest --cov=app

# Nur einen spezifischen Test ausführen
uv run pytest tests/test_app.py::TestRootEndpoint::test_root_endpoint

# Tests mit Cache-Clearing
uv run pytest --cache-clear -v
```

### Test-Struktur

```
tests/
├── __init__.py          # Package initialization
├── conftest.py          # Shared fixtures und Konfiguration
├── test_app.py          # Tests für app.py
└── test_json.py         # Tests für JSON-Verarbeitung
```

**Test-Kategorien:**
- **TestRootEndpoint**: Tests für den Root-Endpoint (`/`)
- **TestEchoGetEndpoint**: Tests für GET-Endpoint mit verschiedenen Parametern
- **TestEchoPostEndpoint**: Tests für POST-Endpoint mit JSON-Daten
- **TestEndpointIntegration**: Integrationstests für mehrere Endpoints

### REST Client Testing

Die Datei `test.http` kann mit VS Code REST Client oder ähnlichen Tools verwendet werden:

```bash
# Mit VS Code REST Client Extension
# Einfach auf "Send Request" im Editor klicken
```

### API Endpoints

#### 1. GET Endpoint: `/echo-get`

Sendet Query-Parameter zurück:

```bash
curl "http://localhost:8000/echo-get?message=hello&value=123"
```

**Response:**
```json
{
  "method": "GET",
  "endpoint": "/echo-get",
  "query_params": {
    "message": "hello",
    "value": "123"
  },
  "received_data": {
    "message": "hello",
    "value": "123"
  }
}
```

**Mit Python requests:**
```python
import requests

response = requests.get(
    "http://localhost:8000/echo-get",
    params={"message": "hello", "value": "123"}
)
print(response.json())
```

#### 2. POST Endpoint: `/echo-post`

Sendet JSON-Daten zurück:

```bash
curl -X POST http://localhost:8000/echo-post \
  -H "Content-Type: application/json" \
  -d '{"key": "value", "name": "Echo Server"}'
```

**Response:**
```json
{
  "method": "POST",
  "endpoint": "/echo-post",
  "received_data": {
    "key": "value",
    "name": "Echo Server"
  }
}
```

**Mit Python requests:**
```python
import requests

payload = {"key": "value", "name": "Echo Server"}
response = requests.post(
    "http://localhost:8000/echo-post",
    json=payload
)
print(response.json())
```

#### 3. Root Endpoint: `/`

Welcome Message mit Übersicht aller Endpoints:

```bash
curl http://localhost:8000/
```

### Logging-Output

Die empfangenen Requests werden auf der Konsole geloggt:

```
2026-05-29 10:30:45,123 - __main__ - INFO - Received GET request to /echo-get with params: {'message': 'hello', 'value': '123'}
2026-05-29 10:30:46,456 - __main__ - INFO - Received POST request to /echo-post with body: {"key": "value"}
```
     # Hauptanwendung (FastAPI)
├── pyproject.toml              # Projekt-Konfiguration (uv)
├── pytest.ini                  # Pytest Konfiguration
├── Dockerfile                  # Docker Container Definition
├── docker-compose.yml          # Docker Compose Konfiguration
├── uv.lock                     # Lock-Datei (automatisch generiert)
├── README.md                   # Diese Dokumentation
├── DOCKER.md                   # Docker/Container Dokumentation
├── test.http                   # REST Client Tests
├── .gitignore                  # Git-Ignorierregeln
└── tests/                      # Test Suite
    ├── __init__.py
    ├── conftest.py             # Test Fixtures und Konfiguration
    ├── test_app.py             # App Tests
    └── test_json.py            # JSON Handling Tests
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Öffne diese URLs in deinem Browser, um alle Endpoints zu sehen und zu testen.

## Projektstruktur

```
echo_server/
├── app.py                 # Hauptanwendung (FastAPI)
├── pyproject.toml         # Projekt-Konfiguration (uv)
├── uv.lock                # Lock-Datei (automatisch generiert)
├── README.md             # Diese Dokumentation
└── .gitignore            # Git-Ignorierregeln
```

## Code-Struktur

- **Logging-Konfiguration**: Initialisiert Python-Standard-Logger
- **FastAPI App**: Erstellt die Haupt-API-Instanz
- **Root Endpoint** (`/`): Welcome-Page mit Endpoint-Übersicht
- **GET Endpoint** (`/echo-get`): Verarbeitet Query-Parameter
- **POST Endpoint** (`/echo-post`): Verarbeitet JSON-Body
- **Error Handling**: Fehlerbehandlung für ungültige JSON-Daten

## Technologie-Stack

| Komponente | Version | Beschreibung |
|-----------|---------|-------------|
| Python | 3.14+ | Programmiersprache |
| FastAPI | ≥0.100.0 | Web-Framework |
| Uvicorn | ≥0.23.0 | ASGI-Server |
| uv | Latest | Python Package Manager |
| pytest | ≥7.0.0 | Test Framework |

## Deployment

### Mit Docker/Podman

Dieses Projekt wird mit Docker- und Podman-Support ausgeliefert. Detaillierte Anweisungen finden Sie in der [DOCKER.md](./DOCKER.md) Dokumentation.

**Quick Start:**
```bash
# Docker Compose
docker-compose up -d

# oder mit Podman Compose
podman compose up -d
```

Der Server wird unter `http://localhost:8000` verfügbar sein.

## Weitere Informationen

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Python Logging Module](https://docs.python.org/3/library/logging.html)
- [Docker Support](./DOCKER.md)

## Entwicklung und Beitragen

Zum Beitragen zu diesem Projekt:

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit deine Änderungen (`git commit -m 'Add amazing feature'`)
4. Push zum Branch (`git push origin feature/amazing-feature`)
5. Öffne einen Pull Request

Stelle sicher, dass alle Tests bestehen:
```bash
uv run pytest -v
```

## License

MIT License - Frei verwendbar

## Author

Erstellt als Echo-Server-Vorlage
