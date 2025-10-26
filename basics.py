from typing import List


def breath_first_search_print(graph, source):

    queue = []

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


def depth_first_search_print(graph, source):

    stack = [[source]]
    res = []

    while stack:
        path = stack.pop()
        current = path[-1]
        

        for node in graph[current]:
            stack.append(path + [node])
        
        res.append(path)
    
    return res


graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c': ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : [],
}

print(depth_first_search_print(graph, 'a'))

# print("---Depth Fist Search---")
# depth_first_search_print(graph, 'a')
# print("---Breath First Seartch---")
# breath_first_search_print(graph, 'a')






graph2 = {
    0: [1, 2], 
    1: [3], 
    2: [3], 
    3: []
}

graph3 = {
    0: [4, 3, 1], 
    1: [3, 2, 4], 
    2: [3], 
    3: [4], 
    4: []
}

graph4 = {
    0 : [1, 2],
    1 : [],
    2 : [5],
    3 : [4],
    4 : [2], 
    5 : []
}