# BFS - Breadth first search 
# levelwise traversal
# traverse all element in levels then moves to other level
# output may be different
# use visited list/array and queue

from collections import deque
class Graph:
    def __init__(self, vertex):
        self.mat = [ [0]*vertex for _ in range(vertex)] # 2-Dimentional
        self.size = vertex 

    def add_edge(self, src, dest):  
        if(0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1 
            #use lower line too when undirected graph
            self.mat[dest][src] = 1
            #but if directed graph then no use of this upper line

            #weighted graph - pass parameter = weight and lower line 
            #self.mat[src][dest] = weight
            #self.mat[src][dest] = weight
        else:
            print("Invalid Edge")

    def bfs(self, src):
        visited = [False] * self.size 
        queue = deque([src])
        visited[src] = True 

        while(queue):
            v = queue.popleft()
            print(v, end=" ")

            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True 
                    queue.append(i)

    

g = Graph(8)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,2)
g.add_edge(6,7)
g.bfs(0)