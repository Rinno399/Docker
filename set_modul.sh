#!/bin/bash


echo -e"\e[1;31m[++]Starting[++]\e[0m"
echo -e"\e[1;31m[++]pleae wait and patient[++]\e[0m"
pkg install python -y>/dev/null 2>&1
pkg install pip
python3 -m pip install requests
python3 -m pip install BeautifulSoup
