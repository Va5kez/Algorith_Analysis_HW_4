import sys
from BFS.bfs import BFS
from DFS.dfs import DFS

def main():
    print ("BFS Implementation\n")
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,4], 4: [3,5], 5: []}
    BFS(graph, 0)
    print ("DFS Implementation\n")
    graph2 = {0: [1, 2], 1: [2,3], 2: [3], 3: [1,4], 4: [3,5], 5: []}
    DFS(graph2, 0)

if __name__ == "__main__":
    main()
