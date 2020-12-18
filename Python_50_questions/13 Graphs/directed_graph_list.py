"""
Directed Graph Implementation using List
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, value1, value2):
        self.graph[value1].append(value2)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print("{} => {}".format(node, v))
    
    def DFS(self, startNode):
        visited = set() # Set of unreplicable nodes consulted
        pending = [] # Pending nodes to check
        pending.append(startNode) # Initializing with the start node
        while(pending): # while there is pending nodes
            checking = pending.pop() # Take last pending as checking state and popped of pending
            if not checking in visited: # Only if it wasn't checked, we will print it and set as checked
                print("{}".format(checking), end=" ")
                visited.add(checking)
                for nextnode in self.graph[checking]: # The nextnodes must be inserted as pending
                    if nextnode not in visited:
                        pending.append(nextnode)

    def BFS(self, startNode):
        visited = set() 
        pending = [] 
        pending.append(startNode) 
        while(pending): 
            checking = pending.pop(0) # In order to check in levels, it must turn in queue. Pop is like FIFO logic
            if not checking in visited:
                print("{}".format(checking), end=" ")
                visited.add(checking)
                for nextnode in self.graph[checking]: 
                    if nextnode not in visited:
                        pending.append(nextnode)

if __name__ == "__main__":
    g = Graph()
    g.insertEdge(1,5)
    g.insertEdge(1,7)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,1)
    g.insertEdge(7,6)
    g.insertEdge(6,4)

    #  1
    #  |--5
    #     |--2 (va al 7 tambien, pero es irrelevante)
    #  |--7 (va tambien al 1 pero es irrelevante)
    #     |--6
    #        |--4


    print("********Listing graph***********")
    g.printGraph()
    print("********DFS***********")
    g.DFS(1)
    print("\n********BFS***********")
    g.BFS(1)