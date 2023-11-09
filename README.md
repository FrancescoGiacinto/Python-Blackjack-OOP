# Python OOP Blackjack Simulation

Welcome to my repository where I demonstrate my coding skills through a Python Object-Oriented Programming (OOP) Blackjack Simulation.

## Introduction

Blackjack, a classic card game of strategy and skill, serves as the foundation for this project. The simulation is crafted with Python, utilizing OOP principles to create an engaging and interactive game environment.

## Purpose of This Project

This exercise is published to illustrate my problem-solving capabilities and my approach to structuring a programming project, demonstrating proficiency with fundamental programming concepts in a simple yet effective manner.

## Game Features

- **Object-Oriented Design**: Structures the game with classes representing the deck, dealer, and player.
- **Interactive Gameplay**: Engage in a game of Blackjack against a computer-controlled dealer.
- **Strategic AI**: The dealer AI uses standard Blackjack strategies for gameplay decisions.
- **Console Interface**: Provides a clear and intuitive console-based user interface for gameplay.

## Demonstrated Skills

- **Class-Based Architecture**: Showcases effective use of classes and object methods in Python.
- **Modularity**: Code is organized for easy readability, future maintainability, and potential scalability.
- **Robust Exception Handling**: Ensures smooth program execution and management of unexpected user inputs.
- **Adherence to Python Standards**: Follows PEP 8 guidelines for writing clean and idiomatic Python code.

## Running the Game

To dive into the Blackjack simulation:
1. Clone the repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Execute the game with the command: 
   ```bash
   python blackjack.py
   ```

## Unit Testing: Ensuring Code Integrity

### The Importance of Testing

Unit tests are integral to the development of this simulation, providing a method to verify functionality and detect issues early. They offer a documentation of expected behavior and are key to maintaining code reliability.

### Test Suite Features

The `unittest` framework is employed to construct tests that assess:

1. **Blackjack Detection**: Accuracy of Blackjack hand recognition.
2. **Validation of Non-Blackjack Hands**: Correct identification of hands that do not constitute a Blackjack.
3. **Multi-Card Hands**: Confirmation that hands with more than two cards, totaling 21, are not falsely recognized as Blackjack.

### Executing the Tests

To perform the tests:
1. Open the terminal.
2. Navigate to the directory containing `test.py`.
3. Run the tests with the command:
   ```shell
   python -m unittest test.py
   ```
