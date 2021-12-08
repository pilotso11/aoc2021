
import time

digits = {
    0: ['a', 'b', 'c','e','f','g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
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

sum = 0
words = []
result = []
counts = [0] * 10
start = time.perf_counter()
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
        this_map = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
        this_digits = [''] * 10
        sixes = []
        fives = []
        for word in words:
            for i in (1, 4, 7, 8):
                if len(word) == lengths[i]:
                    this_digits[i] = word
            if len(word) == lengths[0]:
                sixes.append(word)
            if len(word) == 5:
                fives.append(word)
            
        # segment a is the diff beteen 1 and 7
        for c in this_digits[7]:
            if c not in this_digits[1]:
                this_map['a'] = c
        # segment c is not in six, but is in the other 3 6 segment numnbers (9 and 0) and is in 1
        for c in this_digits[1]:
            for w in sixes:
                if c not in w:
                    this_map['c'] = c  
        # f is the other half of 1
        for c in this_digits[1]:
            if c != this_map['c']:
                this_map['f'] = c
        # d is in 4 and also in all of the 5's
        for c in this_digits[4]:
            cnt = 0
            for w in fives:
                if c in w:
                    cnt += 1
            if cnt == 3:
                this_map['d'] = c
        # b is in the other piece of 4   
        for c in this_digits[4]:    
            if c != this_map['d'] and c != this_map['c'] and c != this_map['f']:
                this_map['b'] = c
        # g is in all 3 5's but not in 7 and not d
        for c in this_map.keys():
            cnt = 0
            for c2 in fives:
                if c in c2:
                    cnt += 1    
            if cnt == 3 and c not in this_digits[7] and c != this_map['d']:
                this_map['g'] = c
        # e is the last one left
        for c in this_map.keys():
            if c not in this_map.values():
                this_map['e'] = c

        # build the letters
        for i in range(10):
            if this_digits[i] == '':
                for c in digits[i]:
                   this_digits[i] += this_map[c]

        # sort everything
        for i in range(10):
            this_digits[i] = ''.join(sorted(this_digits[i]))
        for i in range(len(words)):
            words[i] = ''.join(sorted(words[i]))
        for i in range(len(result)):
            result[i] = ''.join(sorted(result[i]))
        
        #print(this_digits)
        #print(this_map)
        #print(words)
 
        val = 0
        for v in result:
            #print(v)
            for i in range(10):
                if v == this_digits[i]:
                    val = val * 10 + i
                    #print("found", i)
        print(result, val)
        sum += val
end = time.perf_counter()

print("sum=", sum)
print("time taken=", end - start)

                    





    
