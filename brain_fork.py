import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def print_letter(c, starting=' '):
    o = 0
    start = 0
    if starting != ' ':
        start = ord(starting) - ord('A') + 1
    if c == ' ':
        # print(' ', file=sys.stderr, flush=True)
        if starting == ' ':
            return ''
        o = ord(c) - ord('A') + start
    else:
        o = ord(c) - ord('A') + 1 - start
        # print(c, o, file=sys.stderr, flush=True)

    if o < 0:
        o += 27

    if o == 0:
        return ''

    if o <= 13:
        return '+' * o
    else:
        return '-' * (27 - o)

magic_phrase = input()
ins = []

for attempt in range(5):
    freq = {}
    for c in magic_phrase:
        if c in freq:
            freq[c] += 1
        else: freq[c] = 1
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    instructions = ''

    if attempt == 3 or attempt == 4:  # save top 3 letters, + space, use a floater for the rest
        TOP = 1
        if attempt == 3:
            TOP = min(3, len(freq_sorted))
        tops = [''] * TOP
        last = ' '
        first = True
        for i in range(TOP):
            tops [i] = freq_sorted[i][0]
        tops = tops[::-1]
        print('tops', tops, file=sys.stderr, flush=True)
        first = True
        for c in tops:
            if not first:  instructions += '>'
            else: first = False
            instructions += print_letter(c)
        work_area = TOP
        pos = TOP-1
        for c in magic_phrase:
            target_pos = work_area
            if c == ' ': target_pos = work_area+1
            elif c in tops: target_pos = tops.index(c)
            while pos != target_pos: # move to target location
                if pos > target_pos:
                    instructions += '<'
                    pos -=1
                else:
                    instructions += '>'
                    pos += 1
            if pos != work_area:
                instructions += '.'
            else:
                instructions += print_letter(c, starting=last)
                instructions +=  '.'
                last = c
        print(instructions, file=sys.stderr, flush=True)
    elif attempt == 2:  # just use 1 cell
        lasts = [' ', ' ']
        pos = 0
        i = 0
        while i < len(magic_phrase):
            c = magic_phrase[i]
            if c == ' ' and pos == 0:
                instructions += '<.>'
                i += 1
            elif c == ' ' and pos == 1:
                instructions += '>.<'
                i += 1
            elif c == lasts[pos]:
                cnt = 0
                while i < len(magic_phrase) and magic_phrase[i] == lasts[pos]:
                    cnt += 1
                    i += 1
                if cnt < 20:
                    while cnt > 0:
                        cnt -= 1
                        instructions += '.'
                else:
                    instructions += '>'
                    while cnt >= 26:
                        instructions += '-[<.>-]'
                        cnt -= 26
                    if cnt > 19:
                        while cnt > 19:
                            instructions += '-'
                            cnt -= 1
                        instructions += '-[<.>-]<'
                    else:
                        instructions += '<'
                        while cnt > 0:
                            instructions += '.'
                            cnt -= 1
            else:
                if c > 'L':
                    if pos == 0:
                       instructions += '>'
                       pos = 1
                else:
                    if pos == 1:
                        instructions += '<'
                        pos = 0
                instructions += print_letter(c, starting=lasts[pos])
                instructions += '.'
                lasts[pos] = c
                i += 1
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
