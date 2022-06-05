from os.path import exists
from model.graph import Graph
from pathlib import Path

def getN() -> int:
    n = -1

    while(n < 3):
        n = int(input("Masukkan banyaknya node (n(node) >= 3): "))
    
    return n

def validateNode(node, countNode) -> bool:
    if(node <= 0 or node > countNode):
        return False
    
    return True
 
def updateEdge(graph: Graph, countNode) -> None:

    filename = input("Masukkan nama file: ")

    file_path = str(Path(__file__).parent) + "\\data\\" + filename

    if(not exists(file_path)):
        raise Exception("File tidak ada")

    #Asumsi bahwa tiap node maksimal hanya ada satu edhe yang menhubungkan untuk satu arah
    count = 0
    done = []
    with open(file_path, 'r') as file:
        for line in file:
            count += 1

            data = [int(numb) for numb in line.split(" ")]

            if(len(data) != 3):
                raise Exception("Terdapat kesalahan pada file pada baris {count}")
                
            if(not validateNode(data[0], countNode) or not validateNode(data[1], countNode)):
                raise Exception("Terdapat kesalahan node pada file pada baris {count}")
                
            if(data[2] < 0):
                raise Exception("Terdapat kesalahan weight edge pada file pada baris {count}")
                
            if([data[0], data[1]] in done):
                raise Exception("Terdapat kesalahn multiple edge pada file pada baris {count}")
                
            graph.addWeight(data[0], data[1], data[2])
            done.append([data[0], data[1]])

        file.close()
        
def getStartDestNode(countNode: int) -> list[int, int]:
    start = int(input("Masukkan start node: "))
    end = int(input("Masukkan end node: "))

    if(not validateNode(start, countNode) or not validateNode(end, countNode)):
        raise Exception("Node tidak valid")
    
    return [start, end]