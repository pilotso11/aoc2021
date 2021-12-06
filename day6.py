#Day 
ages = [0] * 9
with open('day6.input') as f:
    line = f.readline()
    _fish = line.split(',')
    for i in _fish:
        ages[int(i)] += 1

print(ages)

days = 256

for day in range(days):
    new_fish = ages[0]
    for i in range(1, len(ages)):
        ages[i-1] = ages[i] # move down 1 day
    
    ages[6] += new_fish
    ages[8] = new_fish

    total = 0
    for i in ages:
        total += i
    print("Day: ", day, "Fish: ", total, "Ages: ", ages)


    