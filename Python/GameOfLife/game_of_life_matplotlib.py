import numpy as np
import matplotlib.pyplot as plt
from time import sleep


def create_board(N=100, alive_chance=0.3):
    board = np.random.rand(N,N)
    board = np.round(board < alive_chance).astype("int32")
    return board


board = create_board()

fig, ax = plt.subplots(figsize = (12,12))

img_plot = ax.imshow(board, cmap='gray')

ax.set_axis_off()
ax.set_title("Game Of Life")


plt.ion()
plt.show()

i = 0
while plt.fignum_exists(fig.number):
    fig.canvas.flush_events()

    board[i] = 1
    img_plot.set_data(board)

    fig.canvas.draw()
    
    i += 1
    if i == 100: 
        break
    # sleep(0.1)