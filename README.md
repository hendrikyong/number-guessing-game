# Simple Python Number Guessing Game

## Overview

This is a simple Python number guessing game implemented using the `tkinter` library for the graphical user interface. The objective of the game is for the user to guess a randomly generated number between 1 and 100. The user has 5 lives to guess the number. Each incorrect guess reduces their lives by 1. If the user's lives reach 0 without guessing the correct number, the game ends and the number is revealed.

## Features

- **Start Game**: Begin a new game and generate a random number.
- **Guess Number**: Enter guesses and receive feedback on whether the guess is too high, too low, or correct.
- **Lives Management**: Track the number of lives remaining and update user after each guess.
- **End Game**: Inform the player if they have run out of lives or if they have guessed the number correctly.
- **Play Again**: Restart the game without closing the application.
- **Quit Game**: Exit the application.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)

## Installation

1. Ensure you have Python 3.x installed on your system. (If not, refer to the [official Python website](https://www.python.org/downloads/) for installation instructions.)
2. Save the game code into a file named `main.py`.


## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where the file is located.
3. Run the script with the command:
   ```bash
   python main.py
