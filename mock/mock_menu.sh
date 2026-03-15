#!/bin/bash

BASE_URL="http://127.0.0.1:8001"

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

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Tomato Basil Soup",
    "category": "Soup",
    "price": 6.5,
    "ingredients": ["tomato","basil","garlic","cream"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "French Onion Soup",
    "category": "Soup",
    "price": 7.0,
    "ingredients": ["onion","beef broth","bread","cheese"],
    "allergies": ["gluten","dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Miso Soup",
    "category": "Soup",
    "price": 5.5,
    "ingredients": ["miso paste","tofu","seaweed","scallions"],
    "allergies": ["soy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Chicken Noodle Soup",
    "category": "Soup",
    "price": 6.8,
    "ingredients": ["chicken","noodles","carrot","celery"],
    "allergies": ["gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Grilled Salmon",
    "category": "Main Dish",
    "price": 18.5,
    "ingredients": ["salmon","lemon","olive oil","herbs"],
    "allergies": ["fish"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Steak with Garlic Butter",
    "category": "Main Dish",
    "price": 22.0,
    "ingredients": ["beef steak","garlic","butter","parsley"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Vegetable Stir Fry",
    "category": "Main Dish",
    "price": 14.0,
    "ingredients": ["broccoli","carrot","soy sauce","tofu"],
    "allergies": ["soy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Spaghetti Carbonara",
    "category": "Main Dish",
    "price": 15.5,
    "ingredients": ["spaghetti","egg","pancetta","parmesan"],
    "allergies": ["gluten","egg","dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Chocolate Lava Cake",
    "category": "Dessert",
    "price": 7.5,
    "ingredients": ["chocolate","butter","egg","sugar"],
    "allergies": ["egg","dairy","gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Cheesecake",
    "category": "Dessert",
    "price": 7.0,
    "ingredients": ["cream cheese","sugar","egg","biscuit"],
    "allergies": ["dairy","egg","gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Tiramisu",
    "category": "Dessert",
    "price": 7.8,
    "ingredients": ["mascarpone","coffee","egg","ladyfingers"],
    "allergies": ["dairy","egg","gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Vanilla Ice Cream",
    "category": "Dessert",
    "price": 5.0,
    "ingredients": ["milk","cream","sugar","vanilla"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Fresh Lemonade",
    "category": "Drink",
    "price": 3.5,
    "ingredients": ["lemon","water","sugar"],
    "allergies": [],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Iced Tea",
    "category": "Drink",
    "price": 3.0,
    "ingredients": ["black tea","water","lemon"],
    "allergies": [],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Cappuccino",
    "category": "Drink",
    "price": 4.0,
    "ingredients": ["espresso","milk","milk foam"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Orange Juice",
    "category": "Drink",
    "price": 3.8,
    "ingredients": ["orange"],
    "allergies": [],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Pumpkin Soup",
    "category": "Soup",
    "price": 6.2,
    "ingredients": ["pumpkin","onion","cream","nutmeg"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Beef Goulash",
    "category": "Main Dish",
    "price": 17.5,
    "ingredients": ["beef","paprika","onion","potato"],
    "allergies": [],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Chicken Alfredo",
    "category": "Main Dish",
    "price": 16.2,
    "ingredients": ["chicken","fettuccine","cream","parmesan"],
    "allergies": ["gluten","dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Apple Pie",
    "category": "Dessert",
    "price": 6.8,
    "ingredients": ["apple","flour","butter","sugar"],
    "allergies": ["gluten","dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Strawberry Milkshake",
    "category": "Drink",
    "price": 4.5,
    "ingredients": ["strawberry","milk","sugar","ice cream"],
    "allergies": ["dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Garlic Bread",
    "category": "Appetizer",
    "price": 4.5,
    "ingredients": ["bread","garlic","butter","parsley"],
    "allergies": ["gluten","dairy"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Bruschetta",
    "category": "Appetizer",
    "price": 5.0,
    "ingredients": ["bread","tomato","garlic","olive oil","basil"],
    "allergies": ["gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Mozzarella Sticks",
    "category": "Appetizer",
    "price": 6.2,
    "ingredients": ["mozzarella","breadcrumbs","egg","flour"],
    "allergies": ["dairy","gluten","egg"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Stuffed Mushrooms",
    "category": "Appetizer",
    "price": 5.8,
    "ingredients": ["mushroom","cream cheese","garlic","breadcrumbs"],
    "allergies": ["dairy","gluten"],
    "availability": true
  }'

curl -s -X POST "$BASE_URL/new_item" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "food_name": "Chicken Wings",
    "category": "Appetizer",
    "price": 7.5,
    "ingredients": ["chicken wings","hot sauce","butter","spices"],
    "allergies": ["dairy"],
    "availability": true
  }'

echo ""
echo "Done."
