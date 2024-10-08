#!/bin/bash

handle_interrupt(){
    echo "closed applications"
    kill $CPP_PID
    rm "ss.png"
    kill $PYTHON_PID
    exit 1
}

trap handle_interrupt SIGINT

./build/random & 
CPP_PID=$!
python3 src/main.py &
PYTHON_PID=$!
wait

