pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}

points = {
    ')':3,
    ']':57,
    '}': 1197,
    '>': 25137
}

cpoints = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

good_lines = []
completion_scores = []
score = 0
with open('day10.input') as f:
    while(True):
        line = f.readline().strip()
        if len(line) == 0:
            break
        stack = []
        ok = True
        i = 0
        for c in line:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                    ok = False
                    print("Bad line:", line)
                    break
                expected = stack.pop()
                if pairs[expected] != c:
                    ok = False
                    score += points[c]
                    #print("Found", c, "but expected", pairs[expected], points[c], 'points')
                    #print("At", i, "in", line)
                    break
            i += 1
        
        if ok and len(stack) == 0:
            good_lines.append(line)
        elif ok:
            # Incomplete line
            cscore = 0
            cstr = ''
            while len(stack) > 0:
                cscore *= 5
                expected = stack.pop()
                cscore += cpoints[pairs[expected]]
                #print("Part score:", cscore)
                cstr += pairs[expected]
            completion_scores.append(cscore)
            print("Completion is", cstr, cscore)
            
                

print("Score:", score)

completion_scores.sort()
print("Mid score: ", completion_scores[len(completion_scores)//2])

