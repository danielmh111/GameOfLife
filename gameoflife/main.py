

def get_start_condition():
    ...

def get_next_state():
    # rule 1: any live cell with fewer than two live neighbours dies

    # rule 2: any live cell with two or three live neighbours lives on to the next turn

    # rule 3: any live cell with more than three live neighbours dies

    # rule 4: any dead cell with exactly three live neighbours becomes a live cell on the next turn
    ...

def main():

    print("set the start conditions")

    get_start_condition()

    turns = input("how many turns to play?")

    while turns > 1:
        get_next_state()
        turns -= 1