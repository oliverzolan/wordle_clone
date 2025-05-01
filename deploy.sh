#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🚀 Starting Wordle Clone deployment process..."

# Run tests
echo -e "${GREEN}Running tests...${NC}"
coverage run -m unittest discover tests
if [ $? -ne 0 ]; then
    echo -e "${RED}Tests failed! Aborting deployment.${NC}"
    exit 1
fi

# Generate coverage report
echo -e "${GREEN}Generating coverage report...${NC}"
coverage report -m

# Build the executable
echo -e "${GREEN}Building executable...${NC}"
pyinstaller --onefile run_game.py --name wordle

echo -e "${GREEN}✅ Deployment completed successfully!${NC}"
echo "Executable is available at: ./dist/wordle"

# Run the executable
read -p "Do you want to run the game now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    ./dist/wordle
fi 