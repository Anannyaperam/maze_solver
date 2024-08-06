def is_valid_move(maze, x, y, visited):
    """Check if (x, y) is a valid move."""
    return (0 <= x < len(maze) and 0 <= y < len(maze[0]) and
            maze[x][y] == 0 and not visited[x][y])

def solve_maze(maze, x, y, end_x, end_y, path, visited):
    """Recursive function to solve the maze using backtracking."""
    # If reached the end point
    if x == end_x and y == end_y:
        path.append((x, y))
        return True

    # Check if the current move is valid
    if is_valid_move(maze, x, y, visited):
        # Mark the cell as visited and add it to the path
        visited[x][y] = True
        path.append((x, y))

        # Explore all possible directions: down, right, up, left
        if solve_maze(maze, x + 1, y, end_x, end_y, path, visited):
            return True
        if solve_maze(maze, x, y + 1, end_x, end_y, path, visited):
            return True
        if solve_maze(maze, x - 1, y, end_x, end_y, path, visited):
            return True
        if solve_maze(maze, x, y - 1, end_x, end_y, path, visited):
            return True

        # Backtrack: unmark the cell and remove it from the path
        visited[x][y] = False
        path.pop()

    return False

def find_path_in_maze(maze, start, end):
    """Find a path from start to end in the maze."""
    start_x, start_y = start
    end_x, end_y = end
    path = []
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    if solve_maze(maze, start_x, start_y, end_x, end_y, path, visited):
        return path
    else:
        return None

def print_maze(maze, path=None):
    """Print the maze with the path marked."""
    if path:
        path_set = set(path)
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if (i, j) in path_set:
                    print('P', end=' ')
                elif cell == 1:
                    print('#', end=' ')
                else:
                    print('.', end=' ')
            print()
    else:
        for row in maze:
            for cell in row:
                print('#' if cell == 1 else '.', end=' ')
            print()

def main():
    # Get maze dimensions and input from user
    rows = int(input("Enter number of rows in the maze: "))
    cols = int(input("Enter number of columns in the maze: "))

    print("Enter the maze row by row (0 for open path, 1 for wall):")
    maze = []
    for _ in range(rows):
        row = list(map(int, input().strip().split()))
        if len(row) != cols:
            print("Error: Number of columns does not match the specified width.")
            return
        maze.append(row)

    # Get start and end points from user
    start_x, start_y = map(int, input("Enter start point (x y): ").strip().split())
    end_x, end_y = map(int, input("Enter end point (x y): ").strip().split())

    # Check if start and end points are valid
    if (not (0 <= start_x < rows and 0 <= start_y < cols and
             0 <= end_x < rows and 0 <= end_y < cols)):
        print("Error: Start or end point is out of maze bounds.")
        return

    # Find and print the path
    path = find_path_in_maze(maze, (start_x, start_y), (end_x, end_y))
    print("\nMaze with Path:")
    print_maze(maze, path)
    if path:
        print("\nPath found:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
