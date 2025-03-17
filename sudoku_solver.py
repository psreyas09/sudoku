import tkinter as tk
from tkinter import messagebox

# Backtracking algorithm to solve Sudoku
def solve_sudoku(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle solved
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            print(f"Placing {num} at ({row}, {col})")  # Debugging statement

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Reset on backtrack
            print(f"Backtracking from ({row}, {col})")  # Debugging statement

    return False


# Find an empty cell in the board (denoted by 0)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


# Check if placing a number in a specific cell is valid
def is_valid(board, num, row, col):
    # Check row
    if num in board[row]:
        print(f"Invalid: {num} already in row {row}")  # Debugging statement
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        print(f"Invalid: {num} already in column {col}")  # Debugging statement
        return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                print(f"Invalid: {num} already in subgrid starting at ({start_row}, {start_col})")  # Debugging
                return False

    return True


# Function to get user input from the GUI and solve the Sudoku
def solve_puzzle():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            try:
                value = int(entries[i][j].get()) if entries[i][j].get() else 0
                if value < 0 or value > 9:
                    messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 9.")
                    return
                row.append(value)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers.")
                return
        board.append(row)

    print("Initial Board:")  # Debugging statement
    for row in board:
        print(row)

    if solve_sudoku(board):
        print("Solved Board:")  # Debugging statement
        for row in board:
            print(row)

        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("No Solution", "The given Sudoku puzzle has no solution.")


# Create the GUI with enhanced 3x3 subgrid visualization
def create_gui():
    global entries
    root = tk.Tk()
    root.title("Sudoku Solver")

    entries = [[None for _ in range(9)] for _ in range(9)]

    # Create a main frame to hold all 3x3 subgrids
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    # Create 3x3 subgrids
    for subgrid_row in range(3):
        for subgrid_col in range(3):
            # Create a frame for each 3x3 subgrid
            subgrid_frame = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2)
            subgrid_frame.grid(row=subgrid_row, column=subgrid_col, padx=2, pady=2)

            # Add 3x3 Entry widgets inside the subgrid frame
            for i in range(3):
                for j in range(3):
                    row = subgrid_row * 3 + i
                    col = subgrid_col * 3 + j
                    entry = tk.Entry(subgrid_frame, width=2, font=("Arial", 18), justify="center")
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    entries[row][col] = entry

    # Add a Solve button
    solve_button = tk.Button(root, text="Solve", command=solve_puzzle, font=("Arial", 14))
    solve_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()