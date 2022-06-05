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

    try:
        start, dest = getStartDestNode(numb)
    except Exception as e:
        print(e)
        return
    else:
        print(start, dest)
        distance = graph.djikstra(start, dest)
        print(distance)

if __name__ == "__main__":
    main()