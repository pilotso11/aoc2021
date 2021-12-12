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

paths = []

def descend(node, path):
    if node in path and node.islower():
        print('Already visited', node)
        return 
    if node == 'start': return

    path.append(node)
    if node == 'end':
        print('End found')
        p = ','.join(path)
        if p not in paths:
            paths.append(p)
        path.pop()
        return

    if node in links:
        for link in links[node]:
            print('Try', path, link)
            descend(link, path)
    path.pop() 


for node in links['start']:
    print('Starting at',node)
    path = []
    descend(node, path)

print('Found', len(paths), 'paths')


