#!/bin/bash

color1="\033[0;33m"
color2="\033[0;32m"

echo -e "${color1}[!] This is a demonstration."
echo -e "[!] Make sure to use the import function in both the account view and the transaction view."
echo -e "[!] To use the application normally, run ${color2}$ poetry run invoke start${color1} !"

ACCOUNTS_FILENAME=accounts-demo.csv TRANSACTIONS_FILENAME=transactions-demo.csv poetry run python3 src/index.py
