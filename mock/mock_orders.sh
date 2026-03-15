#!/bin/bash

BASE_URL="http://127.0.0.1:8002"

echo "Logging in..."

TOKEN=$(curl -s -X POST "$BASE_URL/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin"}' |
  sed -E 's/.*"access_token":"([^"]+)".*/\1/')

if [ -z "$TOKEN" ]; then
  echo "Login failed"
  exit 1
fi

echo "Token received."

echo "Pushing mock item..."

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Tomato Basil Soup","Garlic Bread"],
  "table_number": 1,
  "description": "Lunch order",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Chicken Wings","Chicken Wings","Iced Tea"],
  "table_number": 2,
  "description": "Shared appetizer",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Beef Goulash","Garlic Bread","Fresh Lemonade"],
  "table_number": 3,
  "description": "Dinner",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Chicken Alfredo","Orange Juice"],
  "table_number": 4,
  "description": "Quick meal",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["French Onion Soup","Bruschetta","Cappuccino"],
  "table_number": 5,
  "description": "Light lunch",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Steak with Garlic Butter","Steak with Garlic Butter","Iced Tea"],
  "table_number": 6,
  "description": "Two steaks",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Pumpkin Soup","Garlic Bread","Garlic Bread"],
  "table_number": 7,
  "description": "Soup and sides",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Apple Pie","Vanilla Ice Cream"],
  "table_number": 8,
  "description": "Dessert",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Chicken Noodle Soup","Bruschetta","Fresh Lemonade"],
  "table_number": 9,
  "description": "Lunch combo",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Strawberry Milkshake","Apple Pie","Apple Pie"],
  "table_number": 10,
  "description": "Sweet order",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Stuffed Mushrooms","Chicken Wings","Iced Tea"],
  "table_number": 11,
  "description": "Appetizers",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Steak with Garlic Butter","Beef Goulash","Fresh Lemonade"],
  "table_number": 12,
  "description": "Large meal",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Cappuccino","Apple Pie"],
  "table_number": 13,
  "description": "Coffee break",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Chicken Alfredo","Garlic Bread","Garlic Bread","Orange Juice"],
  "table_number": 14,
  "description": "Family meal",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Pumpkin Soup","Bruschetta","Iced Tea"],
  "table_number": 15,
  "description": "Afternoon meal",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Vanilla Ice Cream","Vanilla Ice Cream","Strawberry Milkshake"],
  "table_number": 16,
  "description": "Desserts",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Chicken Wings","Chicken Wings","Chicken Wings","Fresh Lemonade"],
  "table_number": 17,
  "description": "Wings table",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Beef Goulash","Pumpkin Soup","Garlic Bread"],
  "table_number": 18,
  "description": "Hearty order",
  "time": "2026-03-15T16:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Tomato Basil Soup","Chicken Noodle Soup","Orange Juice"],
  "table_number": 19,
  "description": "Soup combo",
  "time": "2026-03-15T12:00:00Z",
  "finished": true
}'

curl -X 'POST' \
  'http://127.0.0.1:8002/add_order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "food_names": ["Steak with Garlic Butter","Apple Pie","Cappuccino"],
  "table_number": 20,
  "description": "Dinner and dessert",
  "time": "2026-03-15T08:00:00Z",
  "finished": true
}'

echo ""
echo "Done."
