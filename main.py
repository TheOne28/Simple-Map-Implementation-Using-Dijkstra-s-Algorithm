from model.graph import Graph
from helperFunction import getN, updateEdge

def main():    
    graph = Graph(getN())

    updateEdge(graph)
    


if __name__ == "__main__":
    main()