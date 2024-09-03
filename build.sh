#!/bin/bash
pip3 install pyautogui

mkdir build
cd build

cmake ..
make

cd ..
