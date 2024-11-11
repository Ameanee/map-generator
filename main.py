import time
import random

width = 1000
height = 1000

land = [[-1 for i in range(width)] for j in range(height)]

seeds = 63
seed_cords = []
seed_cords2 = []

for i in range(seeds):
    seed_cords.append([(random.randint(0, width - 1), random.randint(0, height - 1))])
    land[seed_cords[-1][0][1]][seed_cords[-1][0][0]] = i

seed_cords2 = seed_cords

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

start = time.time()

updated = 1
while updated != 0:
    updated = 0
    for num in range(len(seed_cords2)):
        new_tiles = []
        for tile in seed_cords2[num]:
            for dir in dirs:
                new_tile = (tile[0] + dir[0], tile[1] + dir[1])

                if new_tile[0] >= 0 and new_tile[0] < width and new_tile[1] >= 0 and new_tile[1] < height and land[new_tile[1]][new_tile[0]] == -1 and len(new_tiles) + len(seed_cords[num]) < max_sizes[num]:
                    land[new_tile[1]][new_tile[0]] = num
                    new_tiles.append(new_tile)
                    updated += 1
        seed_cords[num] += new_tiles
        seed_cords2[num] = new_tiles
print(time.time() - start)

rainbow = [
    "#FF0000", "#FF1A00", "#FF3300", "#FF4D00", "#FF6600", "#FF7F00", "#FF9900", 
    "#FFB200", "#FFCC00", "#FFE600", "#FFFF00", "#E6FF00", "#CCFF00", "#B2FF00", 
    "#99FF00", "#7FFF00", "#66FF00", "#4DFF00", "#33FF00", "#1AFF00", "#00FF00", 
    "#00FF1A", "#00FF33", "#00FF4D", "#00FF66", "#00FF7F", "#00FF99", "#00FFB2", 
    "#00FFCC", "#00FFE6", "#00FFFF", "#00E6FF", "#00CCFF", "#00B2FF", "#0099FF", 
    "#007FFF", "#0066FF", "#004DFF", "#0033FF", "#001AFF", "#0000FF", "#1A00FF", 
    "#3300FF", "#4D00FF", "#6600FF", "#7F00FF", "#9900FF", "#B200FF", "#CC00FF", 
    "#E600FF", "#FF00FF", "#FF00E6", "#FF00CC", "#FF00B2", "#FF0099", "#FF007F", 
    "#FF0066", "#FF004D", "#FF0033", "#FF001A", "#FF0000", "#FF1A00", "#FF3300", 
    "#FF4D00", "#FF6600", "#FF7F00", "#FF9900"
]

start = time.time()
with open("out.svg", "w") as f:
    f.write(f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{width}\" height=\"{height}\">")
    for y in range(height):
        x = 0
        while x < width:
            w = 1
            color = rainbow[land[y][x]]
            x2 = x + 1
            while x2 < width and land[y][x2] == land[y][x]:
                x2 += 1
            w = x2 - x
            f.write(f"<rect x=\"{x}\" y=\"{y}\" width=\"{w}\" height=\"1\" fill=\"{color}\" stroke=\"none\"/>")
            x = x2
    f.write("</svg>")

print(time.time() - start)
