class Graph:
    def __init__(self, node : int) -> None:
        self.node = [i for i in range (1, node + 1)]
        self.adjMatrix = [[-1 for i in range(len(node))] for j in range (len(node))]
    
    def addWeight(self, src : int, dest: int, weight: int):
        if(src not in self.node or dest not in self.node):
            raise("Node tidak ada")

        self.adjMatrix[src][dest] = weight
        

    def djikstr(self):
        pass