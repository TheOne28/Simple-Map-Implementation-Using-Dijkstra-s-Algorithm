class Graph:
    def __init__(self, node : list) -> None:
        self.node = node
        self.adjMatrix = [[-1 for i in range(len(node))] for j in range (len(node))]
    
    def addWeight(self, src : int, dest: int, weight: int):
        if(src not in self.node or dest not in self.node):
            raise("Node tidak ada")
        
    def djikstr(self):
        pass