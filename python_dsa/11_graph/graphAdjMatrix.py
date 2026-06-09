#contains vertices and edges 
# Type of graphs:-

    # 1.Undirected graph:- can moves in every direction.
    # 2.Directed graph:- strictly follows given directions to move.
    # 3.Weighted graph:- also have distance between two vertices.

#Note :- this is visual logical way to think
# to store in memory we need graph representation.

#Graph Representation:-
    #1.Matrix representation.
    #2.List representation.

#Here we use, ------ matrix representation ------
# n of vertices = make n x n matrix (0=no edge, 1=present)

# undirected matrix = symmetric matrix
# rows = source 
# columns = destination

#Matrix edge Add:-
# go to matrix rows = 1 to column = 2 --> 
# mat[1][2] = 1
# mat[2][1] = 1
# mat[2][3] 5
# mat[2][3] 0

# Matric edge remove:-
# mat[2][3] = 0

class Graph:
    def __init__(self, vertex):
        self.mat = [ [0]*vertex for _ in range(vertex)] # 2-Dimentional
        # no need to write loop variable so write any or "_".
        self.size = vertex 

    def add_edge(self, src, dest):     #src = source, dest = destination
        #index out of bound exception handling 
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
            #map = convert other data types to string  
            #join = joins the value with each other at once

G = Graph(5)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(2,3)

G.print()

# dense graph :- more no. of edges / more 1 in it.(best -> matrix representation)
# sparse graph :- less no. of edges / more 0 in it.(best -> list representation.)


#Advantages of matrix representation -
#1.simple
#2.use if dense graph 

#Disadvantages of matrix representation - 
#1.memory wastage
#2.don't use if sparse graph (due to memory wastage)


