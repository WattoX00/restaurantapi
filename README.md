# Restaurant API

A FastAPI backend API for managing a restaurant menu, orders, and sales statistics.

## Installation

Clone the repository and install dependencies:

```
pip install -r requirements.txt
```

## Run the FastAPI server:

```bash
main.sh
```

## Open the APIs at:

```
http://127.0.0.1:8001
```

```
http://127.0.0.1:8002
```

```
http://127.0.0.1:8003
```

## Interactive API docs:

/docs – Swagger UI

/redoc – ReDoc

## Dependencies

- fastapi[standard]

- uvicorn

- sqlalchemy

- python-jose[cryptography]

- passlib[bcrypt]

- python-multipart

## API Endpoints

### Menu Management

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | `/get_menu` | Get all menu items |
| POST   | `/new_item` | Add a new menu item |
| DELETE | `/delete_item/{id}` | Delete a menu item |
| PATCH  | `/patch_item/{id}` | Update a menu item |

### Orders

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | `/add_order` | Create a new order (JSON: `food_names: List[str]`) |
| GET    | `/view_orders` | Get all orders |
| GET    | `/view_order/{id}` | Get a specific order |
| PATCH  | `/update_odrder/{id}` | Update an order |
| PATCH  | `/finish_order/{id}` | Mark an order as finished |

### Statistics

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | `/most_items_sold` | Get most sold menu items |
| GET    | `/least_items_sold` | Get least sold menu items |
| GET    | `/monthly_data` | Get monthly sales data |
