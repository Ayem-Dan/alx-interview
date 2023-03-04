#!/usr/bin/env python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Parameters:
    grid (List[List[int]]): A rectangular grid of 0s and 1s, where 0\
          represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    # Define the directions for checking adjacent cells.
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize the perimeter and visited sets.
    perimeter = 0
    visited = set()

    # Iterate through the grid to find the island.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                # Use depth-first search to find the perimeter of the island.
                stack = [(row, col)]
                visited.add((row, col))
                while stack:
                    r, c = stack.pop()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                            if grid[nr][nc] == 0:
                                perimeter += 1
                            elif (nr, nc) not in visited:
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                        else:
                            perimeter += 1
    return perimeter
