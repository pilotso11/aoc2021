class Node:
    value = ''
    next = None
    prev = None
    def __init__(self, value, prev):
        self.value = value
        self.pref = prev
        self.next = None
    
    def insert_after(self, node):
        node.next = self.next
        node.prev = self
        self.next = node
    

polymer = ''
p_list = None
tail = None

last = ''
pairs = {}
freq = {}

with open('day14.input', 'r') as f:
    polymer = f.readline().strip()
    for c in polymer:
        if p_list == None:
            p_list = Node(c, None)
            tail = p_list
        else:
            tail.next = Node(c, tail)
            tail = tail.next
            last = c
    
    f.readline()
    while(True):
        line = f.readline().strip()
        parts = line.split(' ')
        if len(parts) == 3:
            pairs[parts[0]] = parts[2]
            freq[parts[0]] = 0
        else:
            break

def print_node(node):
    while node != None:
        print(node.value, end='')
        node = node.next
    print()

#print_node(p_list)
#print(pairs)

    # do one pass
node = p_list
while node != None:
    next = node.next
    if node.next != None:
        pair = node.value + node.next.value
        if pair in pairs:
            freq[pair] += 1
    node = next

#print(freq) 

for i in range(40):
    new_freq = {}
    for (k,v) in freq.items():
        if v == 0:
            continue
        #print(k,v)
        pair_l = k[0] + pairs[k]
        pair_r = pairs[k] + k[1]
        if pair_l not in new_freq: new_freq[pair_l] = 0
        if pair_r not in new_freq: new_freq[pair_r] = 0
        new_freq[pair_l] += v
        new_freq[pair_r] += v
    freq = new_freq
print(freq)

counts = {}
total = 0
for (k,v) in freq.items():
    if v == 0:
        continue
    if k[0] not in counts:
        counts[k[0]] = 0
    counts[k[0]] += v
    total += v

counts[last] += 1
total += 1
print(counts)

max_key = max(counts, key=counts.get)   
min_key = min(counts, key=counts.get)

print('Len:', total)
print("Max:", max_key, "Min:", min_key)
print('Answer:', counts[max_key] - counts[min_key])




