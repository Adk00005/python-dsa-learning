class Graph:
    def __init__(self, vertex):
        self.mat = [[0] * vertex for _ in range(vertex)]
        self.size = vertex 

    #create(add edge)
    def add_edges(self, src, dest):
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1 
            self.mat[dest][src] = 1 
            print("Edge added successfully.")
        else:
            print("Invalid Edge.")

    #read(display matrix)
    def display(self):
        print("\nAdjacency Matrix: ")
        for row in self.mat:
            print(' '.join(map(str, row)))

    #delete(remove edge)
    def remove_edges(self, src, dest):
        if 0 <= src < self.size and 0 <= dest < self.size:
            if self.mat[src][dest] == 0:
                print("Edge does not Exist.")
            else:
                self.mat[src][dest] = 0
                self.mat[src][dest] = 0
                print("Edges removed successfully.")

        else:
            print("Invalid Edge.")

    #update(replace existing edge)
    def update_edge(self, old_src, old_dest, new_src, new_dest):
        if not (0 <= old_src < self.size and
                0 <= old_dest < self.size and
                0 <= new_src < self.size and 
                0 <= new_dest < self.size):
            print("Invalid vertex.")
            return 
        
        if self.mat[old_src][old_dest] == 0:
            print("Old edge does not exist.")
            return 
        
        self.mat[old_src][old_dest] = 0 
        self.mat[old_dest][old_src] = 0 

        self.mat[new_src][old_dest] = 1 
        self.mat[new_dest][old_src] = 1 
        print("edge updated successfully.")

vertices = int(input("Enter number of vertices: "))
g = Graph(vertices)

def main():
    while True:
        print("\n --- Python Graph Matrix CRUD Menu --- ")
        print("1.create(add edges)")
        print("2.read(display matrix)")
        print("3.update edge")
        print("4.delete edge")
        print("5.exit")
        
        choice = input("Enter the choice(1-5): ")

        #create
        if choice == "1":
            src = int(input("Enter source vertex: "))
            dest = int(input("Enter destination vertex: "))

            g.add_edges(src, dest) 

        #read 
        elif choice == "2":
            g.display()

        #update 
        elif choice == "3":
            old_src = int(input("Enter old source vertex: "))
            old_dest = int(input("Enter old destination vertex: "))
            
            new_src = int(input("Enter new source vertex: "))
            new_dest = int(input("Enter new destination vertex: "))

            g.update_edge(old_src, old_dest, new_src, new_dest)
        
        #delete
        elif choice == "4":
            src = int(input("Enter source vertex: "))
            dest = int(input("Enter destination vertex: "))
            g.remove_edges(src, dest)

        #exit 
        elif choice == "5":
            print("Exiting the program !!!")
            break 
        
        else:
            print("Invalid choice. RE ENTER !!")
            

if __name__ == "__main__":
    main()
