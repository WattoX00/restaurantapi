# Restaurant API – Master Data

This API manages the restaurant's menu and items with its own database. It does **not** connect to external APIs. It does basic CRUD operations for menu management.

## Base URL

```
http://localhost:8001/
```

### Menu Management

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | `/get_menu` | Get all menu items |
| POST   | `/new_item` | Add a new menu item |
| DELETE | `/delete_item/{id}` | Delete a menu item |
| PATCH  | `/patch_item/{id}` | Update a menu item |
