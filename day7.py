hpos = []
with open('day7.input', 'r') as f:
    line = f.readline()
    parts = line.split(',')
    for p in parts:
        hpos.append(int(p))
    hpos.sort()

print (hpos)
mean = sum(hpos) / len(hpos)
median = hpos[len(hpos)//2] 
print( "mean=",  mean)
print( "median=", median )

def cost_of_moving_to(pos, hpos):
    cost = 0
    for i in hpos:
        cost += abs(i - pos)
    return cost

min = -1
minpos = -1
for i in range(median-2, median+2):
    cost = cost_of_moving_to(i, hpos)
    if min == -1 or cost < min:
        min = cost
        minpos = i
    print(i, "Cost=", cost)

print("Best=", minpos, "Cost=", min)  






