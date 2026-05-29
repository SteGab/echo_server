# Echo Server

Ein einfacher Python-basierter Echo-Server, der GET und POST Requests verarbeitet und die empfangenen Daten an den Client zurücksendet. Alle Requests werden über einen Logger protokolliert.

## Features

- 🔄 **Echo-Funktionalität**: Sendet empfangene Daten im gleichen Format zurück
- 📝 **Logging**: Alle Requests werden auf der Konsole geloggt
- 🚀 **FastAPI**: Modernes, asynchrones Python-Web-Framework
- 📚 **Auto-Dokumentation**: Swagger UI verfügbar unter `/docs`
- ⚡ **ASGI-Server**: Uvicorn für hohe Performance

## Installation

### Voraussetzungen
- Python 3.8+
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

### Server starten

```bash
# Mit uv run
uv run uvicorn app:app --reload

# Oder direkt mit Python
uv run python app.py
```

Der Server läuft dann auf `http://127.0.0.1:8000`

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
```

### Test-Struktur

```
tests/
├── conftest.py          # Shared fixtures und Konfiguration
└── test_app.py          # Alle Tests für app.py
```

**Test-Kategorien:**
- **TestRootEndpoint**: Tests für den Root-Endpoint (`/`)
- **TestEchoGetEndpoint**: Tests für GET-Endpoint mit verschiedenen Parametern
- **TestEchoPostEndpoint**: Tests für POST-Endpoint mit JSON-Daten
- **TestEndpointIntegration**: Integrationstests für mehrere Endpoints

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

## API Dokumentation

FastAPI generiert automatisch interaktive API-Dokumentation:

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
| FastAPI | ≥0.100.0 | Web-Framework |
| uv | Latest | Python Package Manager |
| Uvicorn | ≥0.23.0 | ASGI-Server |
| Python | 3.8+ | Programmiersprache |

## Weitere Informationen

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Python Logging Module](https://docs.python.org/3/library/logging.html)

## License

MIT License - Frei verwendbar

## Author

Erstellt als Echo-Server-Vorlage
