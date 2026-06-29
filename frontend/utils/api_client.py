# frontend/utils/api_client.py
# frontend/utils/api_client.py
import requests

# 1. Base URL of your live FastAPI backend
BACKEND_URL = "http://127.0.0.1:8000"

def send_query_to_backend(text: str) -> dict:
    """
    Sends the user input to the backend using the exact key name ('message') required.
    """
    try:
        endpoint = f"{BACKEND_URL}/api/v1/chat"
        
        # FIXED: Changing the key from "text" to "message" to match your ChatRequest schema
        payload = {"message": text}
        
        response = requests.post(endpoint, json=payload, timeout=5)
        
        if response.status_code == 200:
            return response.json()
            
        return {"error": f"Server error: Status code {response.status_code}. Details: {response.text}"}
        
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to backend server. Ensure Uvicorn is running."}