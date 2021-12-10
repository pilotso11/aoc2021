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

good_lines = []
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
                    print("Found", c, "but expected", pairs[expected], points[c], 'points')
                    print("At", i, "in", line)
                    break
                
            i += 1
        if ok:
            good_lines.append(line)

print("Score:", score)


