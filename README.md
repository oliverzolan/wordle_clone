# Wordle Clone

A Python implementation of Wordle.

## Features

- Guess a 5-letter word within 6 attempts
- Color-coded feedback: green for correct letter in correct position, yellow for correct letter in wrong position, grey for incorrect letter
- Player statistics tracking
- Command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/oliverzolan/wordle_clone.git
cd wordle_clone

# Install dependencies
pip install -r requirements.txt
```

## How to Play

```bash
# Windows
python run_game.py
```
```bash
# macOS/Linux
python3 run_game.py
```

## Development

### Running Tests

```bash
# Run tests (Windows)
python -m unittest discover tests

# If on macOS/Linux
python3 -m unittest discover tests

# Run tests with coverage
coverage run -m unittest discover tests
coverage report -m
```

## Continuous Integration and Deployment

This project uses GitHub Actions:

1. **Automated Testing**: Every push and pull request to main branch triggers the test workflow.
2. **Automated Deployment**: When code is pushed to the main branch and passes tests, a new release is automatically created.

Created by Oliver Zolan ☕
