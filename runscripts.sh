#!/bin/bash

mkdir build
cd build

cmake ..
make

cd ..


handle_interrupt(){
    echo "closed applications"
    kill $CPP_PID
    rm "ss"
    kill $PYTHON_PID
    exit 1
}

trap handle_interrupt SIGINT

./build/random & 
CPP_PID=$!
python3 src/main.py &
PYTHON_PID=$!
wait

