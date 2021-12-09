import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def print_letter(c):
    if c == ' ':
        # print(' ', file=sys.stderr, flush=True)
        return ''
    else:
        o = ord(c) - ord('A') + 1
        # print(c, o, file=sys.stderr, flush=True)
        if o <= 13:
            return '+' * o
        else:
            return '-' * (27 - o)

magic_phrase = input()
ins = []

for attempt in range(2):
    freq = {}
    for c in magic_phrase:
        if c in freq:
            freq[c] += 1
        else: freq[c] = 1
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    instructions = ''

    if len(freq_sorted) == 1 and attempt == 0:
        instructions += print_letter(freq_sorted[0][0])
        instructions += '.' * (len(magic_phrase) % 26)
        if len(magic_phrase) > 26:
            instructions += '>'
            instructions += '-[<.>-]' * (len(magic_phrase) // 26)
        print(instructions, file=sys.stderr, flush=True)
    else:
        MAX_TOPS = 6
        WILD_CARD_SPACE=30
        last_wildcard = ' '

        # redistribute with most frequent in the middle
        if attempt == 0:
            freq_sorted = freq_sorted[::-2] + freq_sorted [len(freq_sorted)%2::2]
        letter_list = {}
        letter_lookup = {}
        i = 0
        for f in freq_sorted:
            letter_list[i] = f[0]
            letter_lookup[f[0]] = i
            i += 1


        # output the letters
        print(letter_list, file=sys.stderr, flush=True)



        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
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

    ins.append(instructions)

min_i = ['', 0]
for i in ins:
    print("Average moves for=", len(i), len(i) // len(magic_phrase), file=sys.stderr, flush=True)
    if min_i[1] == 0 or len(i) < min_i[1]:
        min_i[1] = len(i)
        min_i[0] = i

print(min_i[0])
