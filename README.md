# Python Rock, Paper, Scissors Game

A classic, interactive, and lightweight Command Line Interface (CLI) game written in Python where a user plays against the computer.

---

## Repository Details
* **Suggested Repository Title:** `python-rps-game`
* **Suggested Description:** A fun Python CLI implementation of Rock, Paper, Scissors featuring random computer choices, inline comments, and robust input validation.

---

## Project Overview
This application allows the user to input one of three options (`rock`, `paper`, or `scissors`). The computer randomly selects its move using Python's `random` module, and the winner is determined using strict conditional logic rules. The codebase includes detailed inline comments to explain each logical step.

## Game Rules
* **Rock** beats Scissors (`rock > scissors`)
* **Scissors** beats Paper (`scissors > paper`)
* **Paper** beats Rock (`paper > rock`)
* If both choose the same option, it results in a tie.

## Features
* **Interactive Gameplay:** Play directly from your command line against a computerized opponent.
* **Strict Input Validation:** Ensures users can only enter valid game options, preventing crashes.
* **Randomized AI:** Uses `random.choice()` for dynamic and unpredictable computer moves.
* **Well-Commented Code:** Fully documented inline comments for easy learning and code review.

## Prerequisites
Ensure you have Python installed on your system. You can verify your installation by running:
```bash
python --version
