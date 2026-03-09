# Restaurant API

A FastAPI backend API for managing a restaurant menu, orders, and sales statistics.

## Installation
<details>
<summary>Click to expand</summary>
Clone the repository and install dependencies:

```bash
git clone https://github.com/wattox00/restaurantapi.git 
```

then create a virtual enviroment
<details>
<summary>Click to expand</summary>
  on linux
  
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

</details>
then run:

```
pip install -r requirements.txt
```
</details>

## Run the FastAPI server:

on linux:

```bash
main.sh
```

on windows:

```
main.ps1
```

CTRL+click the links shows on the terminal (it will show the index.html 's path that you can acces) or manually open:
## Open the APIs at:

Menu
```
http://127.0.0.1:8001
```

Orders
```
http://127.0.0.1:8002
```

Statistics
```
http://127.0.0.1:8003
```

## Interactive API docs:

/docs – Swagger UI

/redoc – ReDoc

## Useage:
There is the basic html that you can use to play around the routes, or you can make your own way..
Get the menu, Pick items to order, execute order, view order on the orders tab, finish orders, repeat...
Check statistics of the orders inside statistics and view the graphs.

## Authentication:

The app uses JWT authentication, its very basic setup.
The credentials are `admin` `admin` everywhere on the login pages by default. Feel free to change those
username: admin
password: admin

## Dependencies
<details>
<summary>Click to expand</summary>
- fastapi[standard]

- uvicorn

- sqlalchemy

- python-jose[cryptography]

- passlib[bcrypt]

- python-multipart

</details>

## API Endpoints
<details>
<summary>Click to expand</summary>
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
</details>

FEEL FREE TO MODIFY ANYTHING AND EVERYTHING INSIDE THE APP :)
