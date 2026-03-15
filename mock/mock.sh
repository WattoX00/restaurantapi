#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "$SCRIPT_DIR/mock_menu.sh"
bash "$SCRIPT_DIR/mock_orders.sh"
