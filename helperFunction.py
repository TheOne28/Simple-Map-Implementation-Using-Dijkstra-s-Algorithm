from attr import field
from numpy import intp
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

    try:
        #Asumsi bahwa tiap node maksimal hanya ada satu edhe yang menhubungkan untuk satu arah
        count = 0
        done = []
        with open(file_path, 'r') as file:
            for line in file:
                count += 1

                data = [int(numb) for numb in line.split(" ")]

                if(len(data) != 3):
                    raise("Terdapat kesalahan pada file pada baris {count}")
                
                if(not validateNode(data[0]) or not validateNode(data[1])):
                    raise("Terdapat kesalahan node pada file pada baris {count}")
                
                if(data[2] < 0):
                    raise("Terdapat kesalahan weight edge pada file pada baris {count}")
                
                if([data[0], data[1]] in done):
                    raise("Terdapat kesalahn multiple edge pada file pada baris {count}")
                
                graph.addWeight(data[0], data[1], data[2])
                done.append([data[0], data[1]])

            file.close()
    except Exception as e:
        print(e.with_traceback())
        raise("Error saat membaca file")

def getStartDestNode() -> list[int, int]:
    start = int(input("Masukkan start node: "))
    end = int(input("Masukkan end node: "))

    if(not validateNode(start) or not validateNode(end)):
        raise("Node tidak valid")
    
    return [start, end]