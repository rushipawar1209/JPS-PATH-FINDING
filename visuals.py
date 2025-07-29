import numpy as np, matplotlib.pyplot as plt

def visualize_path(maze, path, start, goal, figsize=(15, 15)):
    maze_array = np.array(maze)
    nrows, ncols = maze_array.shape

    # Adjust the figure size with figsize parameter
    fig, ax = plt.subplots(figsize=figsize)

    # Plot the maze grid (no axis inversion needed for top-left origin)
    ax.matshow(maze_array, cmap='gray_r')

    # Mark the start in green
    ax.plot(start[1], start[0], 'gs', label='Start')  # 'gs' is for green square

    # Mark the goal in red
    ax.plot(goal[1], goal[0], 'rs', label='Goal')  # 'rs' is for red square

    # Extract path coordinates
    path_x = [y for x, y in path]  # Columns (X axis)
    path_y = [x for x, y in path]  # Rows (Y axis)

    # Plot the final path in blue
    ax.plot(path_x, path_y, 'b-', label='Path')  # 'b-' is for blue line

    # Set the grid
    ax.set_xticks(np.arange(-0.5, ncols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, nrows, 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

    # Set tick marks and labels to visualize the grid cells correctly
    ax.set_xticks(np.arange(ncols))
    ax.set_yticks(np.arange(nrows))

    # Add labels and legend
    ax.legend(loc='upper left')

    # Use tight layout to minimize padding
    plt.tight_layout()

    # Optionally adjust margins to control the area used by the plot
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # Adjust the values as needed

    # Display the grid with larger size and more plotting area
    plt.show()

