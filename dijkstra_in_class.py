from math import inf

nodes = {'a', 'b', 'c', 'd', 'e', 'f'}
connections = {frozenset({'a','b'}): 7,
               frozenset({'c','b'}): 10,
               frozenset({'a','c'}): 9,
               frozenset({'a','f'}): 14,
               frozenset({'c','f'}): 2,
               frozenset({'f','e'}): 9,
               frozenset({'e','d'}): 6,
               frozenset({'c','d'}): 11,
               frozenset({'d','b'}): 15}
start = 'a'
end = 'e'

priority_queue = {nd:inf for nd in nodes}
priority_queue[start] = 0
# Visited starts as an empty dictionary
visited = {}

while priority_queue:
    # find the node with the smallest value in the priority queue
    # take it out of the priority queue and put it in the visited queue
    next_node = min(priority_queue, key=priority_queue.get)
    next_dist = priority_queue.pop(next_node)
    visited[next_node] = next_dist

    # find the neighbours of the newly added node that are in the priority queue
    neighbours = {nd for nd in priority_queue if {nd, next_node} in set(connections.keys())}

    # for each neighbour of 'next_node' check if it is necessary fo update the distance to that neighbour.
    for neighbour in neighbours:
        min_dist = min(priority_queue[neighbour], next_dist + connections[frozenset({next_node, neighbour})])
        priority_queue[neighbour] = min_dist

    print(f'visited: {visited}')
    print(f'priorty queue: {priority_queue}')

