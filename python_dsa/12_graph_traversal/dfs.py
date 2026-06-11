#DFS - Defth first search 
#normally use to explore paths
#possible to have different answers after traversal
#start node - any vertex 
#probable different answers even if start from same vertex

#jabtak rasta milega tab tak aage jayenge 
#dfs use liya jata hai bhul bulbhulaiya se bahar nikalne ke liye

#DFS traversal can be done using 2 things:- 
#1.Visited Array/list and
#2.Stack /or Recursion.
#Graphs has cyclic structure while tree don't have.

#DFS creates Minimum Spanning Tree(MST)

#adjacency matrix/list use to make graph
#Here we use adjcency matrix and stack 
#dfs is graph traversal technique 

class Graph:
    def __init__(self, vertex):
        self.mat = [ [0]*vertex for _ in range(vertex)] # 2-Dimentional
        self.size = vertex 

    def add_edge(self, src, dest):  
        if(0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1 
            #use lower line when undirected graph
            self.mat[dest][src] = 1
            #but if directed graph then no use of this upper line

            #weighted graph - pass parameter = weight and lower line 
            #self.mat[src][dest] = weight
            #self.mat[src][dest] = weight
        else:
            print("Invalid Edge")

    def print(self):
        for row in self.mat:
            print(' '.join(map(str, row)))  

    def dfs(self, src):
        visited = [False] * self.size #visited list/array
        stack = [src]                 #push/pop operation on list called stack in python 

        while(stack):
            v = stack.pop()

            if visited[v] == False:
                print(v, end=" -> ")
                visited[v] = True 

            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i)

g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.dfs(0)