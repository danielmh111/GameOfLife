from dataclasses import dataclass

@dataclass
class Pattern:
    name: str 
    live_cells: set[tuple[int, int]] # set is used here so that set operations can be used to find distinct cells that should be alive or dead - a unique pair of cell coordinates can only exist once in a set.


