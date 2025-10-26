

# f -> g -> h
# |  '  |
# i <- j
# |
# k



def has_path(graph, src, destination):

    if src == destination: 
        return True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, destination) == True:
            return True
    
    return False


def breadth_first_search(graph, src, dst):

    queue = [[src]]
    res = []
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == dst:
            res.append(path)
        else:
            for neigh in graph[node]:
                queue.append(path + [neigh])
    return res


graph = {
    'f' : ['g', 'i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g', 'k'],
    'j' : ['i'],
    'k' : []
}

print(breadth_first_search(graph, 'f', 'k'))