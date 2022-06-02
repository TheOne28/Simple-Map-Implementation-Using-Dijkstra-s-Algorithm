from attr import field
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
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                count += 1

                data = [int(numb) for numb in line.split(" ")]

                if(len(data) != 3):
                    raise("Terdapat kesalahan pada file pada baris {count}")
                
                


            file.close()
    except Exception as e:
        print(e.with_traceback())
        raise("Error saat membaca file")
