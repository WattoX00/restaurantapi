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

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Cappuccino"
  ],
  "table_number": 1,
  "description": "Morning coffee",
  "time": "2026-03-15T08:12:33Z",
  "finished": true
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Tomato Basil Soup",
    "Grilled Salmon"
  ],
  "table_number": 2,
  "description": "Customer allergic to gluten",
  "time": "2026-03-15T12:21:10Z",
  "finished": true
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Fresh Lemonade",
    "Vegetable Stir Fry",
    "Vanilla Ice Cream"
  ],
  "table_number": 3,
  "description": "Avoid dairy",
  "time": "2026-03-15T16:05:44Z",
  "finished": false
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "French Onion Soup"
  ],
  "table_number": 4,
  "description": "Gluten allergy",
  "time": "2026-03-15T08:47:12Z",
  "finished": true
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Spaghetti Carbonara",
    "Cappuccino",
    "Cheesecake"
  ],
  "table_number": 5,
  "description": "Contains dairy and gluten",
  "time": "2026-03-15T12:09:51Z",
  "finished": false
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Miso Soup",
    "Vegetable Stir Fry"
  ],
  "table_number": 6,
  "description": "Customer avoiding dairy",
  "time": "2026-03-15T16:31:22Z",
  "finished": false
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Chicken Noodle Soup",
    "Steak with Garlic Butter",
    "Orange Juice"
  ],
  "table_number": 7,
  "description": "Gluten allergy noted",
  "time": "2026-03-15T12:55:18Z",
  "finished": true
}'

curl -s -X POST "$BASE_URL/add_order" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "food_names": [
    "Iced Tea",
    "Chocolate Lava Cake"
  ],
  "table_number": 8,
  "description": "Contains dairy",
  "time": "2026-03-15T16:44:03Z",
  "finished": false
}'

echo ""
echo "Done."
