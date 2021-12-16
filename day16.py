hex_to_b ={
    '0': '0000',
    '1':'0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def calc(ptype, vals):
    if ptype == 0: # sum
        return sum(vals)
    elif ptype == 1: # product
        v = 1
        for i in vals:
            v *= i
        return v
    elif ptype == 2:
        return min(vals)
    elif ptype == 3:
        return max(vals)
    elif ptype == 4:
        return [0,1][vals[0] > vals[1]]
    elif ptype == 5:
        return [0,1][vals[0] < vals[1]]
    elif ptype == 6:
        return [0,1][vals[0] == vals[1]]


def parse_packet(packet, depth):
    print('  '*depth, packet)
    version_b, ptype_b = packet[0:3], packet[3:6]
    version, ptype = int(version_b, 2), int(ptype_b, 2)
    version_sum = version
    if ptype == 4:
        print('  '*depth, 'Version=', version, 'Ptype=', ptype)
        pos = 6
        literal = ''
        while True:
            #print(pos, packet[pos:pos+5])
            next = packet[pos]
            literal += packet[pos+1:pos+5]
            pos += 5
            if next == '0':
                break
        print('  '*depth, 'Packet 4,literal=', literal, int(literal,2))
        return pos, int(literal,2), version_sum
    else:
        print('  '*depth, 'Version=', version, 'Ptype=', ptype)
        l_flag = packet[6]
        vals = []
        if l_flag == '0':
            # len 15 bits - length of subpackets
            len_b = packet[7:7+15]
            l = int(len_b, 2)
            print('  '*depth, 'Sub-Packets len=', l )
            new_packet = packet[7+15:7+15+l]
            pos = 7 + 15 
            total = 0
            while total < len(new_packet)-1:
                print('  '*depth, "Packet at ", total, '(', pos + total, ')') 
                new_pos, val, vs = parse_packet(new_packet[total:], depth+1)
                version_sum += vs
                vals.append(val)
                total += new_pos
            pos += total
        else:
            # len 11 bits - number of subpackets
            len_b = packet[7:7+11]
            l = int(len_b,2)
            print('  '*depth, 'Sub-Packet count=', l)
            new_packet = packet[7+11:]
            pos = 7 + 11 
            total = 0
            cnt = 0
            vals=[]
            while cnt < l:
                print('  '*depth, "Packet at ", total, '(', pos + total, ')') 
                new_pos, val, vs = parse_packet(new_packet[total:], depth+1)
                version_sum += vs
                vals.append(val)
                total += new_pos
                cnt += 1
            pos += total
        return pos, calc(ptype, vals), version_sum
          

with open('day16.sample', 'r') as f:
    for line in f:
        packet = ''
        line = line.strip()
        for c in line:
            packet += hex_to_b[c]

        print(line)
        pos, vals, version_sum = parse_packet(packet, 0)
        print(vals)
        print(version_sum)

