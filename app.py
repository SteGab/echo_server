import logging
import json
from fastapi import FastAPI, Request
from typing import Any, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Echo Server",
    description="Ein einfacher Echo-Server, der GET und POST Requests zurücksendet",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Welcome endpoint"""
    logger.info("Received GET request to root endpoint")
    return {
        "message": "Welcome to Echo Server",
        "endpoints": {
            "echo-get": "/echo-get?param1=value1&param2=value2",
            "echo-post": "/echo-post (JSON body)",
            "docs": "/docs"
        }
    }


@app.get("/echo-get")
async def echo_get(request: Request) -> Dict[str, Any]:
    """
    Echo GET endpoint - returns all query parameters
    
    Example: GET /echo-get?message=hello&value=123
    """
    # Extract query parameters
    query_params = dict(request.query_params)
    
    # Log the received request
    logger.info(f"Received GET request to /echo-get with params: {query_params}")
    
    return {
        "method": "GET",
        "endpoint": "/echo-get",
        "query_params": query_params,
        "received_data": query_params
    }


@app.post("/echo-post")
async def echo_post(request: Request) -> Dict[str, Any]:
    """
    Echo POST endpoint - returns the received JSON data
    
    Example: POST /echo-post with JSON body {"key": "value"}
    """
    try:
        # Read the request body
        body = await request.json()
        
        # Log the received request
        logger.info(f"Received POST request to /echo-post with body: {json.dumps(body)}")
        
        return {
            "method": "POST",
            "endpoint": "/echo-post",
            "received_data": body
        }
    except json.JSONDecodeError as e:
        logger.error(f"Error processing POST request: {str(e)}")
        return {
            "error": "Invalid JSON",
            "details": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Echo Server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
