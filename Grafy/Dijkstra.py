from queue import PriorityQueue

def Dijkstra(G, s):         # graf G oraz startowa krawędź G
    visited=[ 0 for _ in range(len(G))]
    d=[ 10**10 for _ in range(len(G))]
    parent=[-1 for _ in range(len(G))]
    d[s]=0
    Q=PriorityQueue()
    for u in G[s]:
        Q.put(u)

    
    






if __name__=="__main__":
    G=[[0,0]]   ## reprezentacja listowa grafu
    Dijkstra(G)