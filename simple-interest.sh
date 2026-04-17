#!/bin/bash

echo "=== Simple Interest Calculator ==="

read -p "Enter Principal amount: " principal
read -p "Enter Rate of interest (%): " rate
read -p "Enter Time (years): " time

si=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo "Simple Interest = $si"
