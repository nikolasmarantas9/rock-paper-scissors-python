# Rock, Paper, Scissors — Python

A command-line Rock, Paper, Scissors game built with Python. Play against another player or challenge a computer opponent that adapts to your previous moves.

## Features

- **Two Game Modes:** Player vs Player and Player vs Computer.
- **Best of 3 and Best of 5:** Choose the match format.
- **Adaptive Computer Opponent:** Uses previous player moves to make simple predictions.
- **Input Validation:** Handles invalid menu selections and moves.
- **Live Scoreboard:** Displays round-by-round results and scores.
- **Session Statistics:** Tracks completed matches and round wins, losses, and draws.
- **Quit Option:** Cancel the current match during move selection.
- **Unit Tests:** Automated tests for the game's winning rules.
- **No Third-Party Dependencies:** Uses Python's standard library.

## Requirements

- Python 3.10 or newer recommended.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nikolasmarantas9/rock-paper-scissors-python.git
cd rock-paper-scissors-python
```

### 2. Run the game

```bash
python rock_paper_scissors.py
```

On Windows, you can also use:

```powershell
py rock_paper_scissors.py
```

### 3. Run the tests

```bash
python -m unittest -v
```

On Windows:

```powershell
py -m unittest -v
```

## How to Play

1. Choose Player vs Player, Player vs Computer, View Session Statistics, or Exit.
2. Enter the player name or names.
3. Select the match format: Best of 3 or Best of 5.
4. Enter `1` for Rock, `2` for Paper, or `3` for Scissors.
5. Follow the round results and scoreboard until the match ends.
6. Enter `Q` during move selection to cancel the current match.

In Player vs Player mode, both players use the same terminal. Moves may remain visible in terminal history, so this is a simple console game rather than a secure hidden-choice interface.

## Project Structure

```text
rock-paper-scissors-python/
├── rock_paper_scissors.py
├── test_rock_paper_scissors.py
├── README.md
└── .gitignore
```

## Concepts Demonstrated

- Python functions and modular design
- Dictionaries, loops, and conditional logic
- Input validation
- Random selection
- Basic prediction using previous moves
- Game state and session statistics
- Automated unit testing

## Notes

Session statistics are stored in memory and reset when the program closes. The computer opponent uses a simple heuristic; it is not a machine-learning model.

## License

This project is intended for learning and portfolio demonstration. No formal open-source license has been added.
