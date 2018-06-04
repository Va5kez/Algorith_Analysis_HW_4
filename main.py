import sys
from BFS.bfs import BFS

def main():
    print ("BFS Implementation\n")
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,4], 4: [3,5], 5: []}
    BFS(graph, 0)

if __name__ == "__main__":
    main()
