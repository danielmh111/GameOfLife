from itertools import product
from pprint import pprint 

# a blank 10x10 grid
blank_grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

test_grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def get_cell(grid, row, column):
    return grid[row][column]

def is_alive(cell):
    return cell == 1

def get_neighbours_coords(cell_coords):

    x, y = cell_coords

    modifiers = list(
        product([-1,0,1], [-1,0,1])
        )

    return [(x + a, y + b) for [a, b] in modifiers if (x + a, y + b) != cell_coords]

def count_living_neighbours(neighbour_coords: list[tuple[int,int], ], grid: list[list[int,]]):
    return sum (
        [grid[x][y] for x,y in neighbour_coords]
    )    
    

if __name__ == '__main__':
    grid: list[list[int,],] = test_grid
    cell_coords: tuple[int, int] = (4,5)
    # row, column = cell_coord
    # cell: int = get_cell(grid=grid, row=row, column=column)
    # cell_alive = is_alive(cell)

    # print(cell_alive)

    neighbour_coords = get_neighbours_coords(cell_coords=cell_coords)
    num_neighbours_living = count_living_neighbours(neighbour_coords=neighbour_coords, grid=grid)

    # rule 1: any live cell with fewer than two live neighbours dies

    # rule 2: any live cell with two or three live neighbours lives on to the next turn

    # rule 3: any live cell with more than three live neighbours dies

    # rule 4: any dead cell with exactly three live neighbours becomes a live cell on the next turn




