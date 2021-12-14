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

pairs = {}

with open('day14.sample', 'r') as f:
    polymer = f.readline().strip()
    for c in polymer:
        if p_list == None:
            p_list = Node(c, None)
            tail = p_list
        else:
            tail.next = Node(c, tail)
            tail = tail.next
    
    f.readline()
    while(True):
        line = f.readline().strip()
        parts = line.split(' ')
        if len(parts) == 3:
            pairs[parts[0]] = parts[2]
        else:
            break

def print_node(node):
    while node != None:
        print(node.value, end='')
        node = node.next
    print()

print_node(p_list)
print(pairs)


for i in range(10):
    # do one pass
    print('pass', i)
    node = p_list
    while node != None:
        next = node.next
        if node.next != None:
            pair = node.value + node.next.value
            if pair in pairs:
                node.insert_after(Node(pairs[pair], None))
        node = next

counts = {}
node = p_list
total = 0
while node != None:
    if node.value not in counts:
        counts[node.value] = 1
    else:
        counts[node.value] += 1
    total += 1
    node = node.next


max_key = max(counts, key=counts.get)   
min_key = min(counts, key=counts.get)

print('Len:', total)
print("Max:", max_key, "Min:", min_key)
print('Answer:', counts[max_key] - counts[min_key])





