from itertools import product
from pprint import pprint 
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import colors
from pathlib import Path
from time import sleep 

# A Game of Life, played on a random grid as a test case

# rule 1: any live cell with fewer than two live neighbours dies
# rule 2: any live cell with two or three live neighbours lives on to the next turn
# rule 3: any live cell with more than three live neighbours dies
# rule 4: any dead cell with exactly three live neighbours becomes a live cell on the next turn

def create_random_row(grid_size):
    return [randint(0,1) for _ in range(grid_size)]

def create_random_grid(grid_size: int = 10):
    return [create_random_row(grid_size) for _ in range(grid_size)]

def get_cell(grid, row, column):
    return grid[row][column]

def is_alive(cell):
    return cell == 1

def get_neighbours_coords(cell_coords, grid_dim):

    modifiers = product([-1,0,1], [-1,0,1])
    x, y = cell_coords

    return [
        (x + a, y + b) 
        for [a, b] in modifiers 
        if (x + a, y + b) != cell_coords and 0 <= x + a < grid_dim and 0 <= y + b < grid_dim
    ]

def count_living_neighbours(neighbour_coords: list[tuple[int,int], ], grid: list[list[int,]]):
    return sum (
        [grid[x][y] for x,y in neighbour_coords]
    )   

def count_all_living_cells(grid):
    return  sum([sum(row) for row in grid])

def play_the_game(start_grid, max_generations=100):
    grid = start_grid
    generation = 1  

    while generation <= max_generations:

        if generation == 1:
            yield generation, grid
            generation += 1
            continue

        next_grid = []

        for x, row in enumerate(grid):
            new_row = []
            for y, cell in enumerate(row):

                cell: int = get_cell(grid=grid, row=x, column=y)
                neighbour_coords = get_neighbours_coords(cell_coords=(x,y), grid_dim=len(grid))
                num_neighbours_living = count_living_neighbours(neighbour_coords=neighbour_coords, grid=grid)

                if num_neighbours_living < 2 or num_neighbours_living >= 4 or (num_neighbours_living != 3 and not is_alive(cell)): #rule one or rule three
                    next_value = 0
                elif (num_neighbours_living in {2,3} and is_alive(cell)) or (num_neighbours_living == 3 and not is_alive(cell)): #rule two or rule four
                    next_value = 1

                new_row.append(next_value)

            next_grid.append(new_row)
        
        yield generation, next_grid
        
        if grid == next_grid:
            yield generation, f"the grid stablized after {generation} generations"
            break

        grid = next_grid

        if count_all_living_cells(grid) == 0:
            yield generation, f"the grid stablized after {generation} generations"
            break 

        if generation == max_generations:
            yield generation, f"the grid is still living after {generation} generation but it is not stable. Max generations reached, so the simulation has halted."
        generation += 1


def main():
    grid = create_random_grid(grid_size=25)

    turns = play_the_game(start_grid=grid, max_generations=250)

    for turn in turns:
        generation, state = turn
        print(f"generation {generation}")
        pprint(state)


def plot_grid(turns):
    filepath = Path(r"C:\Users\Daniel\projects\GameOfLife\testplot.mp4")
    figure, ax = plt.subplots()
    cmap = colors.ListedColormap(['w', 'b'])
    plots = []
    
    counter = 1
    
    for turn in turns:
        generation, grid = turn
        
        plot = ax.imshow(grid, cmap=cmap)
        # ax.set_title(f"Generation {generation}")
        
        plots.append([plot,])
        counter += 1

    animation = ani.ArtistAnimation(fig=figure, artists=plots, interval=100)
    
    writer = ani.FFMpegWriter(
        fps=12
    )
    animation.save(
        filename='test_anim.mp4'
        ,writer=writer
        )
    
    return animation




if __name__ == '__main__':
    # main()
    # print("~FIN~")

    grid = create_random_grid(grid_size=100)
    turns = play_the_game(start_grid=grid, max_generations=500)
    turns = [turn for turn in turns]
    turns.pop()
    plot_grid(turns)
    print("Done")