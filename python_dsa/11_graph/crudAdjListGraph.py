class Graph:
    def __init__(self):
        self.adjList = {}

    #create vertex 
    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            print("vertex added successfully.")
        else:
            print("vertex already exists.")

    #create edge 
    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        if dest not in self.adjList[src]:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            print("Edge addded successfully.")
        else:
            print("Edge already Exists.")
    
    #read 
    def display(self):
        if not self.adjList:
            print("Graph is empty.")
        else:
            print("\nAdjacency List:")
            for vertex in self.adjList:
                print(vertex, " -> ", self.adjList[vertex], end="\n")

    #update vertex 
    def update_vertex(self, old_vertex, new_vertex):
        if old_vertex not in self.adjList:
            print("vertex not found.")
            return 
        
        if new_vertex in self.adjList:
            print("New vertex already exists.")
            return 
        
        self.adjList[new_vertex] = self.adjList.pop(old_vertex)

        for vertex in self.adjList:
            new_list = []
            for x in self.adjList[vertex]:
                if x == old_vertex:
                    new_list.append(new_vertex)
                else:
                    new_list.append(x)  
            self.adjList[vertex] = new_list

        print("vertex updated successfully")

    #delete edge
    def remove_edge(self, src, dest):
        if src in self.adjList and dest in self.adjList[src]:
            self.adjList[src].remove(dest)
            self.adjList[dest].remove(src)
            print("Edge removed successfully.")
        else:
            print("Edge not found.")

    #delete vertex
    def remove_vertex(self, vertex):
        if vertex not in self.adjList:
            print("vertex not found.")
            return 
        for i in self.adjList[vertex]:
            self.adjList[i].remove(vertex)

        del self.adjList[vertex]
        print("vertex removed successfully")

g = Graph()

def main():
    while True:
        print("\n --- Python Graph (Adjacency List) CRUD Menu ---")
        print("1.create vertex")
        print("2.create edge")
        print("3.read graph")
        print("4.update vertex")
        print("5.delete edge")
        print("6.delete vertex")
        print("7.exit")
        choice = input("Enter the  choice (1-7): ")

        #create vertex
        if choice == "1":
            vertex = int(input("Enter the vertex: "))
            g.add_vertex(vertex)

        #create edge 
        elif choice == "2":
            src = int(input("Enter source vertex: "))
            dest = int(input("Enter destination vertex: "))

            g.add_edge(src, dest)

        #read 
        elif choice == "3":
            g.display()

        #update 
        elif choice == "4": 

            old_vertex = int(input("Enter the old vertex: "))
            new_vertex = int(input("Enter the new vertex: "))

            g.update_vertex(old_vertex, new_vertex)

        #delete edge
        elif choice == "5":
            src = int(input("Enter source vertex: "))
            dest = int(input("Enter destination vertex: "))

            g.remove_edge(src, dest)

        #delete vertex
        elif choice == "6":
            vertex = int(input("Enter the vertex: "))
            g.remove_vertex(vertex)

        #exit
        elif choice == "7":
            print("Exiting the program!!!")
            break 
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



        