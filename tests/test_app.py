import pytest
from fastapi.testclient import TestClient
from app import app


class TestRootEndpoint:
    """Tests für den Root-Endpoint"""
    
    def test_root_endpoint(self, client):
        """Test GET / - Welcome Message"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to Echo Server"
        assert "endpoints" in response.json()


class TestEchoGetEndpoint:
    """Tests für den GET /echo-get Endpoint"""
    
    def test_echo_get_single_param(self, client):
        """Test GET /echo-get mit einem Parameter"""
        response = client.get("/echo-get?message=hello")
        assert response.status_code == 200
        data = response.json()
        assert data["method"] == "GET"
        assert data["endpoint"] == "/echo-get"
        assert data["query_params"]["message"] == "hello"
        assert data["received_data"]["message"] == "hello"
    
    def test_echo_get_multiple_params(self, client):
        """Test GET /echo-get mit mehreren Parametern"""
        response = client.get("/echo-get?message=hello&value=123&name=test")
        assert response.status_code == 200
        data = response.json()
        assert data["query_params"]["message"] == "hello"
        assert data["query_params"]["value"] == "123"
        assert data["query_params"]["name"] == "test"
    
    def test_echo_get_no_params(self, client):
        """Test GET /echo-get ohne Parameter"""
        response = client.get("/echo-get")
        assert response.status_code == 200
        data = response.json()
        assert data["method"] == "GET"
        assert data["query_params"] == {}
    
    def test_echo_get_special_characters(self, client):
        """Test GET /echo-get mit Sonderzeichen"""
        response = client.get("/echo-get?message=hello%20world&special=test%2Fvalue")
        assert response.status_code == 200
        data = response.json()
        assert data["query_params"]["message"] == "hello world"
        assert data["query_params"]["special"] == "test/value"


class TestEchoPostEndpoint:
    """Tests für den POST /echo-post Endpoint"""
    
    def test_echo_post_json_data(self, client):
        """Test POST /echo-post mit JSON-Daten"""
        payload = {"key": "value", "number": 42}
        response = client.post("/echo-post", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["method"] == "POST"
        assert data["endpoint"] == "/echo-post"
        assert data["received_data"]["key"] == "value"
        assert data["received_data"]["number"] == 42
    
    def test_echo_post_empty_object(self, client):
        """Test POST /echo-post mit leerem Objekt"""
        response = client.post("/echo-post", json={})
        assert response.status_code == 200
        data = response.json()
        assert data["received_data"] == {}
    
    def test_echo_post_nested_json(self, client):
        """Test POST /echo-post mit verschachtelten Daten"""
        payload = {
            "user": {
                "name": "John",
                "age": 30
            },
            "tags": ["test", "echo"]
        }
        response = client.post("/echo-post", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["received_data"]["user"]["name"] == "John"
        assert data["received_data"]["tags"] == ["test", "echo"]
    
    def test_echo_post_invalid_json(self, client):
        """Test POST /echo-post mit ungültigem JSON"""
        response = client.post(
            "/echo-post",
            content="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
        assert data["error"] == "Invalid JSON"


class TestEndpointIntegration:
    """Integrationstests für die Endpoints"""
    
    def test_get_and_post_different_data(self, client):
        """Test GET und POST mit unterschiedlichen Daten"""
        # GET Request
        get_response = client.get("/echo-get?test=data")
        assert get_response.status_code == 200
        
        # POST Request
        post_response = client.post("/echo-post", json={"test": "data"})
        assert post_response.status_code == 200
        
        # Beide sollten unterschiedliche Strukturen haben
        assert get_response.json()["method"] == "GET"
        assert post_response.json()["method"] == "POST"
