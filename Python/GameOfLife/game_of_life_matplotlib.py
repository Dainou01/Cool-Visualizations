import numpy as np
import matplotlib.pyplot as plt

def create_board(N=100, alive_chance=0.3):
    """Create a board with alive_chance percent filled white."""

    # Create NxN array with values [0,1)
    board = np.random.rand(N,N)

    # Set whites to every number less than alive chance.
    board = (board < alive_chance).astype("int32")
    return board
    
def update_board(board):
    # Get size of board
    w, h = board.shape

    # Create a new board based on old board
    new_board = board.copy()

    ## We want to update every cell with the rules.
    # Rule 1: If a cell is alive and has 2 or 3 neighbours, it stays alive
    # Rule 2: If a cell is alive and has 4 or more neighbours, it dies
    # Rule 3: If a cell is alive and has less than 2 neighbours, it dies
    # Rule 4: If a cell is dead and has exactly 3 live neighbours, it comes alive

    # Loop over each cell in the board
    for x, y in np.ndindex(board.shape):
        # Wrap indexing when out of bounds
        xp1 = (x+1) % w
        yp1 = (y+1) % h

        # Get number of live neighbours
        neighbours = (
            board[x-1,yp1] + board[x, yp1] + board[xp1,yp1] +
            board[x-1, y ] +       0       + board[xp1, y ] +
            board[x-1,y-1] + board[x, y-1] + board[xp1,y-1]
        )

        # Now we update each cell based on the number of neighbours
        cell = board[x,y]
        if cell == 1 and 2 <= neighbours <= 3:  # Rule 1
            new_board[x, y] = 1
        elif cell == 1 and neighbours >= 4:     # Rule 2
            new_board[x, y] = 0
        elif cell == 1 and neighbours < 2:      # Rule 3
            new_board[x, y] = 0
        elif cell == 0 and neighbours == 3:     # Rule 4
            new_board[x, y] = 1

    # Now return the new board
    return new_board


################# MAIN PROGRAM #################

#### Make some constants
# Number of frames before reset
NUM_FRAMES = 500
# Size of board
BOARD_SIZE = 100
# Chance for cell to start as white
CHANCE_WHITE = 0.3

# Create the board
board = create_board(BOARD_SIZE, CHANCE_WHITE)

# Get the pyplot axis
fig, ax = plt.subplots(figsize = (12,12))
img_plot = ax.imshow(board, cmap='plasma')

# Style the board so it looks good
ax.set_axis_off()
ax.set_title(f"Game Of Life")
fig.tight_layout()

# Do some stuff to make the thing animated
plt.show(block=False)
plt.pause(0.1)
bg = fig.canvas.copy_from_bbox(fig.bbox)
ax.draw_artist(img_plot)
fig.canvas.blit(fig.bbox)

i = 1
# Loop while figure is open / exit when window close
while plt.fignum_exists(fig.number):
    # Now we want to get a new board and set the image data
    board = update_board(board)
    img_plot.set_data(board)

    # Reset figure
    fig.canvas.restore_region(bg)
    # Redraw the image with new data
    ax.draw_artist(img_plot)
    # Put image in figure
    fig.canvas.blit(fig.bbox)
    # Now update figure to show image
    fig.canvas.flush_events()

    # Count frames and reset :)
    i += 1
    if i > NUM_FRAMES:
        i = 0
        board = create_board(BOARD_SIZE, CHANCE_WHITE)

