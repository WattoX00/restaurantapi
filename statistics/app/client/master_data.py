import httpx

MENU_SERVICE_URL = "http://127.0.0.1:8001"

def get_menu_items():
    response = httpx.get(f"{MENU_SERVICE_URL}/get_menu")
    response.raise_for_status()
    return response.json()
