# Sudoku Solver

A simple Sudoku solver using Python and Tkinter. This application allows users to input a Sudoku puzzle, solve it using a backtracking algorithm, and display the solution on the graphical interface.

## Features
- User-friendly GUI built with Tkinter
- Supports 9x9 Sudoku puzzles
- Uses backtracking algorithm to find solutions
- Highlights 3x3 subgrids for better visualization
- Provides error messages for invalid inputs

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
   ```
2. Install dependencies (if required):
   ```sh
   pip install tk
   ```
3. Run the application:
   ```sh
   python sudoku_solver.py
   ```

## Usage
1. Enter the Sudoku puzzle in the provided 9x9 grid.
2. Click the **Solve** button to compute the solution.
3. The solved puzzle will be displayed in the grid.

## Algorithm
The solver uses the **backtracking algorithm**, which:
- Finds an empty cell in the grid.
- Tries numbers 1-9, checking if the placement is valid.
- Recursively continues until the board is solved.
- Backtracks if a number leads to an invalid solution.


## Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License.

---
Made with ❤️ using Python and Tkinter.

