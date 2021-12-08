digits = {
    0: ['a', 'b', 'c','e','f','g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'f'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f','g'],    
    6: ['a','b','d','e','f','g'],
    7: ['a', 'c', 'f',],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
lengths = [0] * 10

for d in range(10):
    for digit in digits[d]:
        freq[digit] += 1    
    lengths[d] = len(digits[d])

print(freq)
print(lengths)

words = []
result = []
counts = [0] * 10
with open('day8.input', 'r') as f:
    while(True):
        lines = f.readline()
        if len(lines) < 10:
            break
        parts = lines.split('|')
        result = parts[1].strip().split()
        words = parts[0].strip().split()
        #print(words)
        #print(result)
        for r in result:
            l = len(r)
            for i in range(10):
                if l == lengths[i]:
                    counts[i] += 1
                    break

print(counts[1], counts[4], counts[7], counts[8])
print(counts[1] + counts[4] + counts[7] +counts[8])





    
