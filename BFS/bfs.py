def BFS(Adj, s):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    print ("Root: ", s)
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        print ("Level: ", i, " | Branches not visited: ",str(next)[1:-1])
        frontier = next
        i += 1
