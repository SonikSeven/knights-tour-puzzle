# Knight's Tour Puzzle

This project presents a Python-based solution for solving the Knight's Tour Puzzle, utilizing the Warnsdorff's rule for chess. The Knight's Tour is a sequence of moves by a knight on a chessboard such that the knight visits every square only once. Warnsdorff's rule is a heuristic for finding such tours.

## Features

- **Dynamic Board Creation:** Users can create a chessboard of custom dimensions.
- **Interactive Gameplay:** Users can choose to solve the puzzle themselves or let the program find a solution.
- **Warnsdorff's Rule:** Utilizes Warnsdorff's heuristic to efficiently find a knight's tour.

## Project Structure

- `field.py`: Contains the `Field` class that represents the chessboard.
- `main.py`: The main driver script that interacts with the user and manages the game flow.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/knights-tour-puzzle.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## How to Use

1. Follow the on-screen instructions to input the board dimensions and the knight's starting position.
2. Decide whether you want to attempt solving the puzzle yourself or have the program find a solution for you.

## How It Works

- The program first asks the user to specify the chessboard dimensions and the knight's starting position.
- Based on the user's choice, it either:
  - Lets the user solve the puzzle while suggesting possible moves.
  - Finds a solution automatically using the Warnsdorff's rule and displays the completed tour.

## Technical Details

### The `Field` Class

- Represents the chessboard, storing details like dimensions and cell states.
- Overrides special methods for item assignment, access, and string representation to facilitate board manipulation and rendering.

### Solving the Puzzle

- The `find_solution` and `move` functions utilize recursive backtracking, testing all possible moves according to Warnsdorff's heuristic.
- The board dynamically updates to reflect the knight's traversal.

## Conclusion

This project demonstrates the application of Warnsdorff's rule in solving the Knight's Tour Puzzle, offering both an interactive and automated approach to the problem.

Enjoy challenging yourself with different board sizes or observe how the algorithm tackles the puzzle!

## License

This project is licensed under the [MIT License](LICENSE.txt).
