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
        if x > self.size - 1 or y > self.size - 1:
            return False
        self.graph[x][y] = 1
        return True

    def printGraph(self):
        for i in range(self.size):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print("{} ==> {}".format(i,j))

    def DFS(self, startNode):
        visited = set() # Set of unreplicable nodes consulted
        pending = [] # Pending nodes to check
        pending.append(startNode) # Initializing with the start node
        while(pending): # while there is pending nodes
            checking = pending.pop()          # Take last pending as checking state and popped of pending
            if not checking in visited: # Only if it wasn't checked, we will print it and set as checked
                print("{}".format(checking), end=" ")
                visited.add(checking)
                for n in range(self.size):
                    if self.graph[checking][n] and n not in visited:
                        pending.append(n)

    def BFS(self, startNode):
        visited = set() 
        pending = [] 
        pending.append(startNode) 
        while(pending): 
            checking = pending.pop(0) # In order to check in levels, it must turn in queue. Pop is like FIFO logic
            if not checking in visited:
                print("{}".format(checking), end=" ")
                visited.add(checking)
                for n in range(self.size):
                    if self.graph[checking][n] and n not in visited:
                        pending.append(n)

if __name__ == "__main__":
    g = Graph(7)
    g.insertEdge(1,5)
    g.insertEdge(1,7)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,8)
    g.insertEdge(8,1)
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
