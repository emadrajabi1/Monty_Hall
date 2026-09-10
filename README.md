# Monty Hall Problem Simulation

A Python simulation of the Monty Hall problem that compares winning
probabilities when the player keeps the initial choice versus switching
doors.

## Overview

The program simulates the Monty Hall problem using random door selection
and calculates the win rate for two strategies:

-   **Without switching:** The player keeps the original door.
-   **With switching:** The player switches to the remaining unopened
    door.

The simulation runs multiple games and compares the results of both
strategies.

## Features

-   Simulates the Monty Hall problem with Python.
-   Compares switching and non-switching strategies.
-   Calculates win rates from multiple simulated games.
-   Uses type hints for clearer and more maintainable code.
-   Includes docstrings to document functions, parameters, and return
    values.

## Technologies

-   Python
-   `random` module
-   Type Hinting
-   Docstrings

## Example Output

``` text
Without Switching Win rate: 32.00%
With Switching Win rate: 67.00%
```

The exact results vary between runs because the simulation uses random
choices.

## How It Works

Each game contains three doors:

``` text
[Car, Goat, Goat]
```

1.  The doors are randomly shuffled.
2.  The player randomly selects one door.
3.  Monty reveals a different door containing a goat.
4.  The player either:
    -   keeps the original choice, or
    -   switches to the remaining door.
5.  The program records whether the player wins the car.
6.  After many games, the program calculates the win rate for each
    strategy.

## Running the Project

Run the Python file from the terminal:

``` bash
python run.py
```

The program currently simulates **1,000 games**.

## Project Purpose

This project demonstrates practical Python programming concepts
including functions, type hints, list comprehensions, randomization,
simulation, and basic probability analysis.
