import random


def Monty_Hall(switch_doors: bool) -> bool:
    """
    Simulate one round of the Monty Hall problem.

    Args:
        switch_doors: Whether the player switches to the remaining door.

    Returns:
        True if the player wins the car, otherwise False.
    """

    doors: list[str] = ['Car', 'Goat', 'Goat']
    random.shuffle(doors)

    initial_choice: int = random.choice(range(len(doors)))

    if switch_doors:
        doors_revealed: list[int] = [i for i in range(3) if i != initial_choice and doors[i] == 'Goat']
        door_revealed: int = random.choice(doors_revealed)

        final_choice: int = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
        
    else:
        final_choice: int = initial_choice

    return doors[final_choice] == 'Car'


def simulate_game(num_games: int) -> tuple[float, float]:
    """
    Simulate multiple Monty Hall games with and without switching.

    Args:
        num_games: Number of games to simulate.

    Returns:
        A tuple containing:
        - Win rate without switching.
        - Win rate with switching.
    """

    num_games_without_switching: int = sum([Monty_Hall(False) for _ in range(num_games)])

    num_games_with_switching: int = sum([Monty_Hall(True) for _ in range(num_games)])

    return (
        num_games_without_switching / num_games,
        num_games_with_switching / num_games
    )


if __name__ == "__main__":
    num_games: int = 1000

    win_percent_without_switching: float
    win_percent_with_switching: float

    win_percent_without_switching, win_percent_with_switching = simulate_game(num_games)

    print(f"Without Switching Win rate: "f"{win_percent_without_switching:.2%}")
    print(f"With Switching Win rate: "f"{win_percent_with_switching:.2%}")