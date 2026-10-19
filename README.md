# Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game written in Python. It supports two play modes and tracks round results.

## Features

- Player vs Player mode
- Player vs Computer mode
- Input validation
- Quit option during move selection
- Round-by-round score
- Final statistics, including total rounds and draws
- Unit tests for the game-winning rules
- No third-party dependencies

## Requirements

- Python 3.10 or newer recommended

## Run the game

Open a terminal in the project folder and run:

```bash
python rock_paper_scissors.py
```

On Windows, if `python` is not recognized, try:

```powershell
py rock_paper_scissors.py
```

## Run tests

```bash
python -m unittest -v
```

On Windows:

```powershell
py -m unittest -v
```

## How to play

1. Select Player vs Player, Player vs Computer, or Exit.
2. Enter the player name(s).
3. Enter `1` for Rock, `2` for Paper, or `3` for Scissors.
4. Enter `Q` to stop the current game.
5. Choose whether to play another round.

In Player vs Player mode, both players use the same terminal. The first player's move may remain visible in terminal history; this is a simple console game, not a secure hidden-choice interface.

## Project structure

```text
rock-paper-scissors/
├── rock_paper_scissors.py
├── test_rock_paper_scissors.py
├── README.md
└── .gitignore
```

## Concepts demonstrated

- Functions and modular design
- Dictionaries and loops
- Input validation
- Random selection
- Basic game state and statistics
- Automated unit testing

## License

This project is available for learning and portfolio demonstration. Add a formal license if you want others to reuse it under specific terms.
