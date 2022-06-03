class Graph:
    def __init__(self, node : int) -> None:
        self.node = [i for i in range (1, node + 1)]
        self.adjMatrix = [[-1 for i in range(len(node))] for j in range (len(node))]
    
    def addWeight(self, src : int, dest: int, weight: int) -> None:
        if(src not in self.node or dest not in self.node):
            raise("Node tidak ada")

        self.adjMatrix[src][dest] = weight
        
    def updateDistance(self, node : int) -> None:
        pass
    
    def getMinimum(self, node, visited : list) -> tuple(int, int):
        toCheck = self.adjMatrix[node]

        minimum = -1
        indMin = -1
        for i in range(len(toCheck)):
            if(minimum == -1):
                if((i + 1) not in visited):
                    minimum = toCheck[i]
                    indMin = i
            else:
                #Asumsi kalau misalnya ada node yang punya weight sama, dipilih nomor node terkecil
                if((i + 1) not in visited and toCheck[i] < minimum):
                    minimum = toCheck[i]
                    indMin = i

        return (minimum, indMin)
                
        

    def djikstr(self, start, dest) -> None:
        visited = []

        current = start - 1
        
        while(current != dest - 1):
            toCheck = self.adjMatrix[current]
