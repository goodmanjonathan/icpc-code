#!/usr/bin/env python3

def get_forced_edge(graph, closed, vertex):
    print(graph)

    for other_vertex in graph[abs(vertex)]:
        if other_vertex < 0 and other_vertex not in closed:
            return other_vertex 
    return None

def number_of_dead_ends(graph, start, opened, closed):
    glitch = 0
    end = 0
    
    while len(opened) > 0:
        current = abs(opened.pop())
        if glitch == 0:
            for glitch_edge in filter(lambda e: e > 0, graph[current]):
                opened.append(glitch_edge)
                number_of_dead_ends(graph, current, opened, closed)
            glitch += 1
        elif get_forced_edge(graph, closed, current) is None:
            end += 1
        else:
            for forced_edge in filter(lambda e: e < 0, graph[current]):
                opened.append(forced_edge)
        closed.append(current)

    return end

case_amt = int(input())
for _ in range(case_amt):
    [vertex_amt, edge_amt] = map(int, input().split(' '))
    
    graph = {}
    for i in range(edge_amt):
        graph[i] = []
    for i in range(edge_amt):
        [a, b] = map(int, input().split(' '))
        if a < 0:
            graph[-a].append(-b)
        else:
            graph[a].append(b)
    
    print(number_of_dead_ends(graph, 1, [1], []))
