    
"""
Directed Graph Implementation using List
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, value1, value2):
        self.graph[value1].append(value2)
        self.graph[value2].append(value1)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print("{} => {}".format(node, v))

if __name__ == "__main__":
    g = Graph()
    g.insertEdge(1,5)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,1)
    g.printGraph()