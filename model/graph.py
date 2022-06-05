INFINITY = 1000000000

class Graph:
    def __init__(self, node : int) -> None:
        self.node = [i for i in range (1, node + 1)]
        self.adjMatrix = [[-1 for i in range(len(self.node))] for j in range (len(self.node))]
    
    def addWeight(self, src : int, dest: int, weight: int) -> None:
        if(src not in self.node or dest not in self.node):
            raise("Node tidak ada")

        self.adjMatrix[src - 1][dest - 1] = weight
        
    def updateDistance(self, node : int, value: int) -> None:
        for i in range(len(self.node)):
            self.adjMatrix[node][i] = self.adjMatrix[node][i] + value
    
    def getMinimum(self, node, visited : list) -> list[int, int]:
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
        # Start dan dest masih one indexing, diubah ke zero indexing
        start -= 1
        dest -= 1

        for row in self.adjMatrix:
            for numb in row:
                print(numb, end = " ")
            print("\n")
        visited = []
        allDistance = [INFINITY for i in range(len(self.node))]
        distance = 0


        current = start - 1

        while(current != dest - 1):
            if(self.adjMatrix[current][dest - 1] != -1):
                distance += self.adjMatrix[current][dest - 1]
                break

            minimum, ind = self.getMinimum(current, visited)
            visited.append(ind)
            current = ind
            distance += minimum
            self.updateDistance(ind, minimum)

        return distance       

