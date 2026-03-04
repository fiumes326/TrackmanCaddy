#!/usr/bin/env bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

#See if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "python3 could not be found, please install it."
    exit 1
fi

#see if poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "poetry could not be found, please install it."
    exit 1
fi

#install dependencies using poetry
poetry config virtualenvs.create false --local
poetry install

# Put script in local bin 
[[ -d "$HOME/.local/bin" ]] || mkdir -p "$HOME/.local/bin"
cp TrackmanCaddy.py "$HOME/.local/bin/trackman-caddy"


# See if local bin is in PATH, if not add it
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    export PATH="$HOME/.local/bin:$PATH"
fi

passed_checks=true
#Check dependencies and print success message
if [[ $(pip3 show pyautogui &> /dev/null) ]]; then
    echo -e "${GREEN}[SUCCESS] pyautogui is installed.${NC}"
else
    echo -e "${RED}[ERROR] pyautogui is not installed.${NC}"
    passed_checks=false
fi

if [[ $(pip3 show pyttsx3 &> /dev/null) ]]; then
    echo -e "${GREEN}[SUCCESS] pyttsx3 is installed.${NC}"
else
    echo -e "${RED}[ERROR] pyttsx3 is not installed.${NC}"
    passed_checks=false
fi

if [[ $(pip3 show keyboard &> /dev/null) ]]; then
    echo -e "${GREEN}[SUCCESS] keyboard is installed.${NC}"
else
    echo -e "${RED}[ERROR] keyboard is not installed.${NC}"
    passed_checks=false
fi

if $passed_checks; then
    echo -e "${GREEN}Setup complete! You can now run 'trackman-caddy' from anywhere.${NC}"
else
    echo -e "${RED}Setup incomplete. Please install the missing dependencies.${NC}"
fi
