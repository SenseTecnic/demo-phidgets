#!/bin/sh

# Initialization script to run wotkitdemo

cd /
cd /home/sensetecnic/wotkitdemo/phidgets
sudo python phidgetrelay.py > logs/log 2>&1 &
cd /


