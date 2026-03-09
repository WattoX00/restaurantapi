#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRONTEND="$SCRIPT_DIR/frontend/index.html"

python master-data/app/main.py &
python orders/app/main.py &
python statistics/app/main.py &

echo ""
echo "Servers started."
echo "Open the frontend:"
echo "file://$FRONTEND"
echo ""

wait
