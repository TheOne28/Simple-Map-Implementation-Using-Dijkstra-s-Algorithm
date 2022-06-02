from model.graph import Graph
from helperFunction import getN, updateEdge, getStartDestNode

def main():    
    numb = getN()
    graph = Graph(numb)

    updateEdge(graph, numb)
    
    start, dest = getStartDestNode()

    graph.djikstr(start, dest)

if __name__ == "__main__":
    main()