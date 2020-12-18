import collections 
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        times is a list of sublist. Every sublist has A, B, C. A is origin,
            B is destination and C is time distance
        N is count of nodes
        K is initial node  
        """
        # First, create the graph with dictionary with the following structure
        # NODE : [(NEXT1,DIST1),(NEXT2, DIST2)]
        graph = collections.defaultdict(list)
        for a,b,time in times:
            graph[a].append((time,b))
        # We define a visited nodes
        visited = set()
        #The pending nodes to check, initializing with the origin with 0 distance
        pending = [(0,K)]

        # This is the djikstra matrix with the optimal values
        # It must begin with infinit distance, except of the origin with 0 distance
        distance = {x:float('inf') for x in range(1,N+1)}
        distance[K] = 0

        while pending:
            #Take the node with the lower current time to the origin
            current_time, node = heapq.heappop(pending)
            # If the node was visited, we need to check other node
            if node in visited:
                continue
            # Else, we declare the node as visited
            visited.add(node)
            # At this point, if algoritm visited all the nodes, we reach the optimal objective 
            # and return the current time
            if len(visited) == N:
                return current_time
            
            # Check all the next nodes 
            # If distance is lower than distance on djikstra matrix, we will upgrade 
            # and analyse it on the loop 
            for next_time, next_node in graph[node]:
                if next_node not in visited and next_time + current_time < distance[next_node]:
                    distance[next_node] = next_time + current_time
                    heapq.heappush(pending,(next_time + current_time,next_node))
        # If we checked all the possible nodes from the origin, the algoritm failed
        return -1


if __name__ == "__main__":
    s = Solution()
    times1 = [[1,2,7],[1,4,2],[2,3,6],[4,5,2],[4,2,3],[5,2,3],[5,3,6],]
    print("First exercise is {}".format(s.networkDelayTime(times1,5,1)))
