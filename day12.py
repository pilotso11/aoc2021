links = {}

with open('day12.input') as f:
    for line in f:
        words = line.strip().split('-')
        if words[0] not in links:
            links[words[0]] = []
        links[words[0]].append(words[1])
        if words[1] not in links:
            links[words[1]] = []
        links[words[1]].append(words[0])


print(links)

tries = 0
paths = []

def dup_lower_in_path(path):
    count = 0
    lowers = []
    for node in path:
        if node.islower():
            if node in lowers:
                return True
            else:
                lowers.append(node)
    return False


def descend(node, path):
    global tries
    tries += 1
    if tries % 1000 == 0: print('Tries', tries)

    if node == 'start': return

    if node == 'end':
        #print('End found')
        path.append(node)
        p = ','.join(path)
        if p not in paths:
            paths.append(p)
            if len(paths) % 50 == 0: print('Found', len(paths), 'paths so far')
        path.pop()
        return

    if node in path and node.islower() and dup_lower_in_path(path):
        #print('Already visited', node)
        return 

    path.append(node)
    if node in links:
        for link in links[node]:
            #print('Try', path, link)
            descend(link, path)
    path.pop() 


for node in links['start']:
    #print('Starting at',node)
    path = []
    descend(node, path)

#for p in paths:
#    print(p)
print('Found', len(paths), 'paths')


