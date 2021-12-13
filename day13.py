points = []
max_x, max_y = 0, 0
folds = []

with open('day13.input', 'r') as f:
    for line in f:
        if 'fold' in line:
            parts = line.strip().split(' ')
            folds.append(parts[2].split('='))
            pass
        else:
            if len(line) >=3:
                _x,_y = line.strip().split(',')
                x,y = int(_x), int(_y)
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                points.append((x,y))

#print(points)

def print_points(points, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in points: print('#', end='')
            else: print('.', end='')
        print()

if max_x < 50 and max_y < 50:
    print_points(points, max_x, max_y)  # part 1
    print()


old_points = {}
for p in points:
    old_points[p] = 0

new_max_x,new_max_y = max_x, max_y

print(folds)

for fold in folds:
    print(fold)
    new_points = {}
    x_split = new_max_x
    y_split = new_max_y
    if fold[0] == 'x': x_split = int(fold[1])
    elif fold[0] == 'y': y_split = int(fold[1])
    print('width=', new_max_x, "height=", new_max_y)
    print('Old points:', len(old_points))
    print('Fold on x:', x_split, 'y:', y_split)

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in old_points: 
                new_point = (x,y)
                if x > x_split:
                    new_point = ((x_split - (x-x_split),y))
                elif y > y_split:
                    new_point = (x,y_split - (y-y_split))
                if new_point not in new_points: new_points[new_point] = 0
    old_points = new_points.copy()
    new_max_x, new_max_y = x_split, y_split
    if new_max_x < 50 and new_max_y < 50:
        print_points(new_points, new_max_x, new_max_y) 
    #print(new_points)
    print('Count', len(new_points))    
