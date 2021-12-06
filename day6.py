#Day 
fish = []
with open('day6.input') as f:
    line = f.readline()
    _fish = line.split(',')
    for i in _fish:
        fish.append(int(i))

print(fish)

days = 80


for day in range(days):
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] < 0:
            fish[i] = 6
            fish.append(8)
    print("Day: ", day, "Fish: ", len(fish))


    