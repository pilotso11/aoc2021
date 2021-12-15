# this is least cost pathfinding with a*
import queue

map = []
with open('day15.input') as f:
    for line in f:
        row = []
        for c in line.strip():
            row.append(int(c))
        map.append(row)
w = len(map[0])
h = len(map)
print('w', w, 'h', h)


new_map = []
for i in range(5):
    for row in map:
        new_row = []
        for c in row:
            new_c = c + i
            while new_c > 9: new_c -= 9
            new_row.append(new_c)
        new_map.append(new_row)
map = new_map
w = len(map[0])
h = len(map)
print('w', w, 'h', h)


new_map = []
for row in map:
    new_row = []
    for i in range(5):
        for c in row:
            new_c = c+i
            while new_c > 9: new_c -= 9
            new_row.append(new_c)   
    new_map.append(new_row)

map = new_map

w = len(map[0])
h = len(map)
print('w', w, 'h', h)
start = (0,0)
end = (w-1, h-1)
print('start', start, 'end', end)

#for r in map:
#    print(r)

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def neighbors(pos):
    n = []
    if pos[0] > 0: n.append((pos[0]-1, pos[1]))
    if pos[0] < h-1: n.append((pos[0]+1, pos[1]))
    if pos[1] > 0: n.append((pos[0], pos[1]-1))
    if pos[1] < w-1: n.append((pos[0], pos[1]+1))

    return n

def astar(map, start, end):
    frontier = queue.PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    max_cost_so_far = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + map[next[0]][next[1]]
            if new_cost > max_cost_so_far:  # progress bar
                max_cost_so_far = new_cost
                print("...", max_cost_so_far)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(end, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far
    
def reconstruct_path(came_from, start, end):
    current = end
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

path, cost = astar(map, start, end)

print(reconstruct_path(path, start, end))
print('cost=', cost[end])

