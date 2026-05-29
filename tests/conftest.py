import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Füge das parent-Verzeichnis zum Python-Path hinzu
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app


@pytest.fixture
def client():
    """Erstellt einen TestClient für die FastAPI-Applikation"""
    return TestClient(app)
