def solve_puzzle(board):
    """
    Uses the backtracking algorithm to solve the sudoku puzzle
    Essentially tries each number that can go in the puzzle one by one moving through empty cells until there is a problem
    When there is a problem, the algorithm backtracks to try the next number recursively trying all valid numbers to find a solution
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, len(board) + 1):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve_puzzle(board):
                return True
            board[row][col] = 0
    return False

def valid(board, num, pos):
    """Checks if inserting num at pos in the board is a valid move given the rules of sudoku"""
    if  valid_in_row_and_column(board, num, pos) and valid_in_box(board, num, pos):
        return True
    return False

def valid_in_box(board, num, pos):
    """Check box; If num already exists, return False"""
    box_size = int(len(board) ** .5)
    box_x = pos[1] // box_size
    box_y = pos[0] // box_size

    for i in range(box_y * box_size, box_y * box_size + box_size):
        for j in range(box_x * box_size, box_x * box_size + box_size):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def valid_in_row_and_column(board, num, pos):
    """Checks the row and column where the num will be inserted. If it exists in either, returns False. Otherwise, True"""
    for i in range(len(board)):
        # Check row; If num already exists, return False
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        # Check column; If num already exists, return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    return True

def print_board(board):
    """Prints out a formatted version of a sudoku board"""
    box_size = int(len(board) ** .5)
    print("--" * (len(board) + box_size + 2))
    for i in range(len(board)):
        if i % box_size == 0 and i != 0:
            print("==" * (len(board) + box_size + 2))
        for j in range(len(board)):
            if j == 0:
                print("| ", end="")
            if j % box_size == 0 and j != 0:
                print("|| ", end="")

            output_num = chr(ord('@') + board[i][j] - 9) if board[i][j] > 9 else str(board[i][j])
            if j == len(board) - 1:
                print(output_num.upper() + " |")
            else:
                print(output_num.upper() + " ", end="")
    print("--" * (len(board) + box_size + 2))

def find_empty(board):
    """Returns the next empty cell in the board or None if there are no empty cells"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None

def load_puzzles():
    import os
    import re
    all_puzzles = []
    dirname = os.path.dirname(__file__)
    puzzle_folder = os.path.join(dirname, 'puzzles')
    for filename in os.listdir(puzzle_folder):
        if not filename.endswith('.txt'):
            continue

        with open(os.path.join(puzzle_folder, filename), 'r') as f:
            puzzle = [
            list(map(int, re.findall(r'\b\d+\b', line)))
            for line in f]
            all_puzzles.append((filename, puzzle))
    return all_puzzles

def solve_puzzles(puzzles):
    for tuple in all_puzzles:
        puzzle_name = tuple[0]
        puzzle = tuple[1]
        puzzle_name = puzzle_name[:-4]
        print("\n\nStarting puzzle " + puzzle_name + ":\n" + "#" * (len(puzzle) * 3))
        print_board(puzzle)
        if not solve_puzzle(puzzle):
            print("No solution was found for " + puzzle_name)
        else:
            print("\nsolution for " + puzzle_name + " is:")
            print("#"*(len(puzzle)*3))
            print_board(puzzle)

######################################################################
#                           RUN TEST CASES                           #
######################################################################

if __name__ == '__main__':
    import time
    start_time = time.time()
    all_puzzles = load_puzzles()
    solve_puzzles(all_puzzles)
    print("time spent: " + str(time.time() - start_time))