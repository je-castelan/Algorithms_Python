"""
Directed Graph Implementation using Matrix
"""
from collections import defaultdict

class Graph:
    def __init__(self, size):
        self.size = size + 1
        
        self.graph = self.graph = [[0 for x in range(size+1)]
                      for y in range(size+1)]

    def insertEdge(self, x, y):
        if x > self.size or y > self.size:
            return False
        self.graph[x][y] = 1
        return True

    def printGraph(self):
        for i in range(self.size):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print("{} ==> {}".format(i,j))

if __name__ == "__main__":
    g = Graph(7)
    g.insertEdge(1,5)
    g.insertEdge(1,7)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,1)
    g.printGraph()
