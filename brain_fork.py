import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

magic_phrase = input()

freq = {}
for c in magic_phrase:
    if c in freq:
        freq[c] += 1
    else: freq[c] = 1
freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# redistribute with most frequent in the middle
freq_sortred = freq_sorted[::-2] + freq_sorted [len(freq_sorted)%2::2]

letter_list = {}
letter_lookup = {}
i = 0
for f in freq_sorted:
    letter_list[i] = f[0]
    letter_lookup[f[0]] = i
    i += 1

# output the letters
print(letter_list, file=sys.stderr, flush=True)

def print_letter(c):
    if c == ' ':
        print(' ', file=sys.stderr, flush=True)
        return ''
    else:
        o = ord(c) - ord('A') + 1
        print(c, o, file=sys.stderr, flush=True)

        if o <= 13:
            return '+' * o
        else:
             return '-' * (27-o)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
instructions = ''
pos = 0
for i in range(len(letter_list)):
    if i != 0:
        instructions += '>'
        pos = pos + 1
    instructions += print_letter(letter_list[i])

for c in magic_phrase:
    new_pos = letter_lookup[c]
    dist = new_pos - pos
    if dist > 15:
        dist = -30 + dist
    elif dist < -15:
        dist = 30 + dist
    #print(pos, new_pos, dist, file=sys.stderr, flush=True)
    if dist > 0:
        instructions += '>' * dist + '.'
        pos += dist
    elif dist < 0:
        instructions += '<' * -dist + '.'
        pos += dist
    else:
        instructions += '.'

print(instructions)