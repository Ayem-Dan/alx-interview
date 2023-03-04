#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Parameters:
    grid (List[List[int]]): A rectangular grid of 0s and 1s, where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    # Define the directions for checking adjacent cells.
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize the perimeter variable.
    perimeter = 0

    # Iterate through the grid to find the island.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Add 4 to the perimeter for each land cell.
                perimeter += 4
                # Subtract 2 for each adjacent land cell.
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        perimeter -= 2
  
    return perimeter
