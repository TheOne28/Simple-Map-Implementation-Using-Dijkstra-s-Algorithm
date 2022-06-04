class Graph:
    def __init__(self, node : int) -> None:
        self.node = [i for i in range (1, node + 1)]
        self.adjMatrix = [[-1 for i in range(len(node))] for j in range (len(node))]
    
    def addWeight(self, src : int, dest: int, weight: int) -> None:
        if(src not in self.node or dest not in self.node):
            raise("Node tidak ada")

        self.adjMatrix[src][dest] = weight
        
    def updateDistance(self, node : int, value: int) -> None:
        for i in range(len(self.node)):
            self.adjMatrix[node][i] = self.adjMatrix[node][i] + value
    
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
                
        

    def djikstra(self, start, dest) -> int:
        visited = []

        current = start - 1
        distance = 0
        while(current != dest - 1):
            minimum, ind = self.getMinimum(visited)
            visited.append(ind)
            current = ind
            distance += minimum
            self.updateDistance(ind, minimum)

        return distance       

