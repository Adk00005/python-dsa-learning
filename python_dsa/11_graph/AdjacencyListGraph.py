# Advantages:- 1.No Memory wastage
#              2.use when sparse graph but not at dense graph
# Disadvantages:- 1.make many pointers in other language but no in python

class Graph:
    def __init__(self):
        self.adjList = {} #dictionary

    def add_vertex(self, vertex):  #key -- no duplicacy
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def addEdge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        #if we use non directional graph then 

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

        #if we use directional graph then 
        # --> self.adjList[src].append(dest)

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, " -> ", self.adjList[vertex], end="\n")


g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)

g.printGraph()
