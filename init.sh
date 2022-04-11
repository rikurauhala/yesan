#!/bin/bash

dir="./src/data"
mkdir $dir
echo "Database directory created at $dir"

file="./src/data/database.sqlite"
touch $file
echo "Database file created at $file"
