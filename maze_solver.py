def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    print()

def is_valid_move(maze, x, y, solution):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and solution[x][y] == 0

def solve_maze(maze, x, y, solution):
    # If (x, y) is the goal
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        return True

    if is_valid_move(maze, x, y, solution):
        solution[x][y] = 1  # Mark x, y as part of the solution path

        # Move right
        if solve_maze(maze, x, y + 1, solution):
            return True

        # Move down
        if solve_maze(maze, x + 1, y, solution):
            return True

        # Move left
        if solve_maze(maze, x, y - 1, solution):
            return True

        # Move up
        if solve_maze(maze, x - 1, y, solution):
            return True

        solution[x][y] = 0  # Backtrack: unmark x, y as part of solution path
        return False

    return False

def find_path_in_maze(maze):
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    if solve_maze(maze, 0, 0, solution):
        return solution
    else:
        return None

# Example maze (0 represents open path, 1 represents blocked path)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

print("Maze:")
print_maze(maze)

solution = find_path_in_maze(maze)
if solution:
    print("Solution path:")
    print_maze(solution)
else:
    print("No solution found")



