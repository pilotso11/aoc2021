hpos = []
with open('day7.input', 'r') as f:
    line = f.readline()
    parts = line.split(',')
    for p in parts:
        hpos.append(int(p))
    hpos.sort()

#print (hpos)
mean = sum(hpos) // len(hpos)
median = hpos[len(hpos)//2] 
print( "mean=",  mean)
print( "median=", median )

def cost_of_moving_to(pos, hpos):
    cost = 0
    for i in hpos:
        diff = abs(i - pos)
        cost += sum( range(0, diff+1) )
    return cost

min = -1
minpos = -1

for step in range(-1, 2, 2):
    print( "step=", step )
    i = mean  # median worked for version 1, mean for version 2, need to think about the maths on this one
    while True:
        cost = cost_of_moving_to(i, hpos)
        print(i, "Cost=", cost)
        if min == -1 or cost <= min:
            min = cost
            minpos = i
        else:
            break
        i = i + step

print("Best=", minpos, "Cost=", min)  






