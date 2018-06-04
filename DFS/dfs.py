def DFS(Adj, s):
    dfs_visited = []
    dfs_backwards = []
    DFS_Visited(Adj, s, dfs_visited, dfs_backwards)
    print ("Visited: ", str(dfs_visited)[1:-1])
    print ("Regression vertex: ", str(dfs_backwards)[1:-1])

def DFS_Visited(Adj, s, dfs_visited, dfs_backwards):
    dfs_visited.append(s)
    for v in Adj[s]:
        for w in Adj[v]:
            if w not in dfs_visited:
                DFS_Visited(Adj, w, dfs_visited,dfs_backwards)
            elif w in dfs_visited and w not in dfs_backwards:
                    dfs_backwards.append(w)
