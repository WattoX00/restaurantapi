import httpx

MENU_SERVICE_URL = "http://127.0.0.1:8002"

def get_order_items():
    response = httpx.get(f"{MENU_SERVICE_URL}/view_orders")
    response.raise_for_status()
    return response.json()
