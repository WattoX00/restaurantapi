# Restaurant API – Orders

This API manages orders using its own database and validates items against the Master Data API. It supports basic CRUD operations for order management.

## Base URL

```
http://localhost:8002
```

## Orders Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | `/add_order` | Create a new order (JSON: `food_names: List[str]`) |
| GET    | `/view_orders` | Get all orders |
| GET    | `/view_order/{id}` | Get a specific order |
| PATCH  | `/update_odrder/{id}` | Update an order |
| PATCH  | `/finish_order/{id}` | Mark an order as finished |
