#!/bin/bash

python master-data/app/main.py &
python orders/app/main.py &
python statistics/app/main.py &

wait
