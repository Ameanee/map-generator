import random
from colorama import Back


width = 40
height = 40

land = [[-1 for i in range(width)] for j in range(height)]

seeds = 16
seed_cords = []

for i in range(seeds):
    seed_cords.append([(random.randint(0, width - 1), random.randint(0, height - 1))])
    land[seed_cords[-1][0][1]][seed_cords[-1][0][0]] = i

dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

max_sizes = [
    width * height for i in range(seeds)
]

updated = True
while updated:
    updated = False
    for num, seed in enumerate(seed_cords):
        new_tiles = []
        for tile in seed:
            for dir in dirs:
                new_tile = (tile[0] + dir[0], tile[1] + dir[1])

                if new_tile[0] >= 0 and new_tile[0] < width and new_tile[1] >= 0 and new_tile[1] < height and land[new_tile[1]][new_tile[0]] == -1 and len(new_tiles) + len(seed) < max_sizes[num]:
                    land[new_tile[1]][new_tile[0]] = num
                    new_tiles.append(new_tile)
                    updated = True
        seed_cords[num] += new_tiles

rainbow = [
    Back.BLACK,
    Back.BLUE,
    Back.CYAN,
    Back.GREEN,
    Back.LIGHTBLACK_EX,
    Back.LIGHTBLUE_EX,
    Back.LIGHTCYAN_EX,
    Back.LIGHTGREEN_EX,
    Back.LIGHTMAGENTA_EX,
    Back.LIGHTRED_EX,
    Back.LIGHTWHITE_EX,
    Back.LIGHTYELLOW_EX,
    Back.MAGENTA,
    Back.RED,
    Back.RESET,
    Back.WHITE,
    Back.YELLOW,
    Back.RESET
]

for i in land:
    for j in i:
        print(f"{rainbow[j]}  {Back.RESET}", end="")
    print()
