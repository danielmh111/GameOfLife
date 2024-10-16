import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from pprint import pprint
from main import create_random_grid



data = create_random_grid(grid_size=50)

cmap = colors.ListedColormap(['w', 'b'])

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap)

plt.show()