from itertools import product
from pprint import pprint 

# A Game of Life, played on a 10x10 grid as a test case

# rule 1: any live cell with fewer than two live neighbours dies

# rule 2: any live cell with two or three live neighbours lives on to the next turn

# rule 3: any live cell with more than three live neighbours dies

# rule 4: any dead cell with exactly three live neighbours becomes a live cell on the next turn


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
    row, column = cell_coords
    cell: int = get_cell(grid=grid, row=row, column=column)

    neighbour_coords = get_neighbours_coords(cell_coords=cell_coords)
    num_neighbours_living = count_living_neighbours(neighbour_coords=neighbour_coords, grid=grid)

    pprint(grid)
    print(f"cell at {cell_coords} is {"alive" if is_alive(cell) else "dead"} and has {num_neighbours_living} living neighbours")



    if num_neighbours_living < 2 or num_neighbours_living >= 4:
        print("cell dies")
    elif num_neighbours_living in {2,3} and is_alive(cell):
        print("cell stays alive if alive")
    elif num_neighbours_living == 3 and not is_alive(cell):
        print("cell comes to life if dead")
    elif num_neighbours_living != 3 and not is_alive(cell):
        print("cell will remain dead")

    print("done")


