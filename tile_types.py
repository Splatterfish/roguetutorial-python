from typing import Tuple

import numpy as np


graphics_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool), #true if the tile can be walked on
        ("transparent", np.bool), #true if blocks FOV
        ("dark", graphics_dt), #graphics for when no longer in FOV
        ("light", graphics_dt),  # Graphics for when currently in FOV
    ]
)

def new_tile(
    *, #enforce use of keywords, so that parameter order doesn't matter
    walkable:int,
    transparent:int,
    dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphics_dt)

floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("."), (60,60,60), (0,0,0)),
    light=(ord("."), (220,220,220), (10,10,10)),
)
wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("#"), (60,60,60), (0,0,0)),
    light=(ord("#"), (220,220,220), (10,10,10)),
)