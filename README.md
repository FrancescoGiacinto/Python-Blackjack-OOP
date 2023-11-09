# Python OOP Blackjack Simulation

Welcome to my Python OOP Blackjack Simulation repository! This project is a simple yet illustrative demonstration of my programming and code organization skills.

## Introduction

Blackjack is one of the most popular card games in the world, known for its blend of chance, strategy, and skill. I chose to simulate this game using Python and Object-Oriented Programming (OOP) to showcase my ability to model real-world scenarios and my understanding of OOP principles.

## Why This Project?

The purpose of publishing this exercise is to provide a tangible example of my approach to problem-solving and project structuring. While the application itself is straightforward, it incorporates a range of programming fundamentals that are critical in a developer's toolkit.

## Features

- **OOP Design**: The game is built using classes and objects, mirroring real-life components of a Blackjack game such as the deck, the dealer, and the player.
- **Interactive Gameplay**: Run the script, and play against the computer in a simulated Blackjack environment.
- **Strategic AI**: The dealer, controlled by the computer, follows traditional Blackjack strategies to make decisions.
- **User-Friendly Interface**: The game is played in the console, with clear prompts and easy-to-understand messages.

## Skills Demonstrated

- **Class-Based Structure**: Exhibiting how to effectively use classes and methods in Python.
- **Modular Code**: Organized for readability, maintainability, and scalability.
- **Exception Handling**: Ensuring the program runs smoothly and handles unexpected inputs gracefully.
- **Python Best Practices**: Adhering to PEP 8 standards and Pythonic principles for clean code.

## How to Run

To play the Blackjack simulation, simply clone this repository, navigate to the directory in your terminal, and run the following command:

```bash
python blackjack.py
´´´

## Unit Testing

### Why Unit Testing?

In developing this Blackjack simulation, I've implemented unit tests to ensure that each part of the code functions as expected. Unit testing is crucial because it helps to identify bugs early in the development process, simplifies integration, and provides documentation of each function's intended behavior. It's a foundational practice in writing reliable and maintainable code.

### About the Tests

The unit tests included in this project are designed to validate the core functionality of the Blackjack game. Using Python's `unittest` framework, I've created a series of tests that verify whether the game's logic correctly identifies different hand compositions—specifically, testing for the following conditions:

1. **Blackjack Detection**: Confirms that a hand is recognized as a Blackjack (an Ace and a 10-value card) correctly.
2. **Non-Blackjack Hands**: Ensures that hands not meeting the Blackjack criteria are not falsely identified as such.
3. **More Than Two Cards**: Validates that a hand containing more than two cards, even if the total is 21, does not qualify as a Blackjack.

### Running the Tests

To run the tests, you can execute the `unittest` module in the command line. Navigate to the directory containing the test file and run:

```bash
python -m unittest test.py
´´´
