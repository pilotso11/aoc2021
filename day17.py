if False: # sample
    target_x =[20,30]
    target_y = [-10,-5]
else:
    target_x =[288,330]
    target_y = [-96,-50]

dx = -1
dy = -1

def check_hit(x,y):
    if x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]:
        return True
    return False

def move(x,y, vx, vy):
    y += vy
    x += vx
    vx = max(0, vx + dx)
    vy = vy + dy
    return x, y, vx, vy

def sim_start(vx,vy, max_x, min_y):
    step = 0
    top = 0
    x,y=0,0
    while True:
        if check_hit(x,y):
            print('hit at step:', step, x, y)
            return step, top
        x,y,vx,vy = move(x,y,vx,vy)
        if top < y: top = y
        step += 1
        if x > max_x or y < min_y:
            #print('miss at step:', step, x, y)
            return -1, 0

max_top = 0

hits = []
for x in range(1,target_x[1]+1):
    for y in range(target_y[0], -target_y[0]+100):
        #print(x,y)
        step, top = sim_start(x,y, target_x[1], target_y[0])
        if step > 0:
            print(x,y, step, top)
            hits.append((x,y))
            if max_top < top: 
                max_top = top
                max_start = (x,y)

print('Max top=', max_top, 'at', max_start) 
print('Total hits=', len(hits))