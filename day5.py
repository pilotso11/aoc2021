vents = []
with open('day5.input', 'r') as f:
    for line in f:
        if len(line) < 1:
            break
        line = line.strip()
        parts = line.split(' ')
        _from = parts[0].split(',')
        _to = parts[2].split(',')
        vents.append( ( (int(_from[0]), int(_from[1])), (int(_to[0]), int(_to[1])) ) )

def max_x_y(vents):
    max_x = 0
    max_y = 0
    for v in vents:
        if v[0][1] > max_y:
            max_y = v[0][1]
        if v[0][0] > max_x:
            max_x = v[0][0]
        if v[1][1] > max_y:
            max_y = v[1][1]
        if v[1][0] > max_x:
            max_x = v[1][0]
    return max_y, max_x

def is_h_or_v(line):
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return True
    else:
        return False

def print_sea(sea):
    print('---------')
    for y in range(0, len(sea)):
        for x in range(0, len(sea[y])):
            print(sea[y][x], end='')
        print()
 
# matrix is [y][x]  = rows are the x axis, columns are the y axis

(max_y, max_x) = max_x_y(vents)
sea = []
for y in range(max_y+1):
    sea.append([])
    for x in range(max_x+1):
        sea[y].append(0)


def swap(a, b):
    return b, a

for line in vents:
    if is_h_or_v(line):
        #print('h_or_v', line)
        _x, _y = line[0][0], line[0][1]
        _x2, _y2 = line[1][0], line[1][1]

        # handle reverse direction
        if _x > _x2: 
            _x, _x2 = swap(_x, _x2)
        if _y > _y2:
            _y, _y2 = swap(_y, _y2)

        if _y == _y2:   # horizontal line  
            #print("horizontal")
            for x in range(_x, _x2+1):
                #print(x, _y)
                sea[_y][x] += 1
        else:
            #print("vertical")
            for y in range(_y, _y2+1):
                #print(_x, y)
                sea[y][_x] += 1
    else: # diagonal
        #print('diagonal:' , line)
        
        _x, _y = line[0][0], line[0][1]
        _x2, _y2 = line[1][0], line[1][1]
        if _x < _x2: x_inc = 1
        else: x_inc = -1
        if _y < _y2: y_inc = 1
        else: y_inc = -1
        #print(x_inc, y_inc)
        y = _y
        for x in range(_x, _x2+x_inc, x_inc):
            #print(x, y)
            sea[y][x] += 1  
            y += y_inc
    #print_sea(sea)
    #print('----')

if max_x < 100:
    print_sea(sea)

def find_max_height(sea):
    max = 0
    for row in sea:
        for col in row:
            if col > max:
                max = col
    return max

def count_great_than_one(sea):
    cnt = 0
    for row in sea:
        for col in row:
            if col > 1:
                cnt += 1
    return cnt

def count_max(sea, max):
    cnt = 0
    for row in sea:
        for col in row:
            if col == max:
                cnt += 1
    return cnt

max = find_max_height(sea)
print("max height:", max)
print("max count:", count_max(sea, max))
print("count > 1:", count_great_than_one(sea))



