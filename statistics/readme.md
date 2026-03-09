# Restaurant API – Statistics

This API calculates statistics from your restaurant's master data and orders. It analyzes **finished orders**, matches ordered items with master data (including prices), and computes the total revenue and item counts accordingly.

## Base URL

```
https://localhost:8003
```

## Available Routes

| Method | Endpoint              | Description                     |
| ------ | -------------------- | ------------------------------- |
| GET    | `/most_items_sold`    | Retrieve the most sold menu items |
| GET    | `/least_items_sold`   | Retrieve the least sold menu items |
| GET    | `/monthly_data`       | Retrieve monthly sales statistics |
