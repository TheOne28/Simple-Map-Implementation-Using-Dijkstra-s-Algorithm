from model.graph import Graph
from helperFunction import getN, updateEdge

def main():    
    numb = getN()
    graph = Graph(numb)

    updateEdge(graph, numb)
    


if __name__ == "__main__":
    main()