from model.graph import Graph
from helperFunction import getN, updateEdge, getStartDestNode

def main():    
    numb = getN()
    graph = Graph(numb)

    try:
        updateEdge(graph, numb)
    except Exception as e:
        print(e)
        return

    start, dest = getStartDestNode()

    graph.djikstra(start, dest)

if __name__ == "__main__":
    main()