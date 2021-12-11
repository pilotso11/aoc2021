map = []

with open("day11.sample") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        row = []
        for c in line.strip():
            row.append(int(c))
        map.append(row)

def print_map(map):
    for row in map:
        for c in row:
            print(c, end="")
        print()
    print()

def flash_cell(map, y, x):
    flashes = 0
    if map[y][x] >= 10:   
        flashes += 1
        map[y][x] = 0
        for y2 in range(y-1, y+2):
            for x2 in range(x-1, x+2):
                if y2 >= 0 and y2 < len(map) and x2 >= 0 and x2 < len(map[y2]):
                    if map[y2][x2] != 0:
                        map[y2][x2] += 1
                        flashes += flash_cell(map, y2, x2)
    return flashes

def add_one(map):
    flashes = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] += 1
    # now check for 10 and over
    for y in range(len(map)):
        for x in range(len(map[y])):
            flashes += flash_cell(map, y, x)
    return flashes

flashes = 0
turns = 100
for i in range(turns):
    print('After step ', i)
    flashes += add_one(map)
    print_map(map)

print('Flash: ', flashes)

