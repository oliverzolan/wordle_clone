# Wordle Clone

A Python implementation of the popular word-guessing game Wordle.

## Features

- Guess a 5-letter word within 6 attempts
- Color-coded feedback: green for correct letter in correct position, yellow for correct letter in wrong position, grey for incorrect letter
- Player statistics tracking
- Command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/wordle_clone.git
cd wordle_clone

# Install dependencies
pip install -r requirements.txt
```

## How to Play

```bash
python run_game.py
```

## Development

### Running Tests

```bash
# Run tests
python -m unittest discover tests

# Run tests with coverage
coverage run -m unittest discover tests
coverage report -m
```

## Continuous Integration and Deployment

This project uses GitHub Actions for CI/CD:

1. **Automated Testing**: Every push and pull request to main/master branch triggers the test workflow.
2. **Automated Deployment**: When code is pushed to main/master branch and passes tests, a new release is automatically created.

### One-Click Deployment

To deploy a new version:

1. Make your changes and ensure tests pass locally
2. Commit and push to the main/master branch
3. GitHub Actions will automatically:
   - Run all tests
   - Generate a coverage report
   - Build an executable
   - Create a new release
   - Upload the executable to the release

You can download the latest executable from the [Releases](https://github.com/yourusername/wordle_clone/releases) page.

## Project Structure

```
wordle_clone/
├── wordle/               # Main package
│   ├── __init__.py
│   ├── game.py           # Game logic
│   ├── word_list.py      # Word list management
│   ├── game_state.py     # Game state management
│   ├── player.py         # Player statistics
│   └── display.py        # Display handling
├── tests/                # Test suite
│   ├── test_game_logic.py
│   ├── test_word_validation.py
│   ├── test_display.py
│   ├── test_game_state.py
│   ├── test_player.py
│   ├── test_word_list.py
│   └── test_integration.py
├── run_game.py           # Entry point
├── requirements.txt      # Dependencies
└── .github/workflows/    # CI/CD configuration
    └── ci-cd.yml
```

