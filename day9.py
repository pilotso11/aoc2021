lines = []
with open("day9.input", "r") as f:
    while True:
        line = f.readline().strip()
        if len(line) > 0:
            lines.append(line)
        else:
            break

width = len(lines[0])
height = len(lines)
print(height, width)

grid = [[0 for x in range(width)] for y in range(height)]
for y in range(height):
    for x in range(width):
        grid[y][x] = int(lines[y][x])

def print_grid(grid):
    for y in range(height):
        for x in range(width):
            print(grid[y][x], end="")
        print()

def is_min(grid, y, x):
    is_smaller = True
    if y < height - 1:
        if grid[y][x] >= grid[y+1][x]:
            is_smaller = False
    if y > 0:
        if grid[y][x] >= grid[y-1][x]:
            is_smaller = False
    if x < width - 1:
        if grid[y][x] >= grid[y][x+1]:
            is_smaller = False
    if x > 0:
        if grid[y][x] >= grid[y][x-1]:
            is_smaller = False

    if y == 0 and x == 14:
        print(y, x, grid[y][x], is_smaller)

    return is_smaller    

if len(grid) < 10:
    print_grid(grid)

mins = []
for y in range(height):
    for x in range(width):
        if is_min(grid, y, x):
            mins.append((x, y))

print(mins)
min_vals = []
for min in mins:
    min_vals.append(grid[min[1]][min[0]] + 1)

print(min_vals)
print(sum(min_vals))