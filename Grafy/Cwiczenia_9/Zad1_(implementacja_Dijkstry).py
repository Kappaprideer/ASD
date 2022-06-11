from collections import deque
from queue import PriorityQueue


def Dijkstra(G,s,t):
    Q=PriorityQueue()
    n=len(G)
    visited=[ 0 for _ in range(n)]
    d= [ 10**10 for _ in range(n)]
    parent=[ None for _ in range(n)]
    Q.put(s)
    d[s]=0
    visited[s]=1
    while not Q.empty():
        s=Q.get()
        for u in G[s]:
            if visited[u[0]]==1 and d[u[0]]>d[s]+u[1]:
                d[u[0]]=d[s]+u[1]
                parent[u[0]]=s
                Q.put(u[0])
            elif visited[u[0]]==0:
                visited[u[0]]=1
                parent[u[0]]=s
                d[u[0]]=d[s]+u[1]
                Q.put(u[0])
    koniec=t
    print("Ścieżka:",end=" ")
    while koniec!=None:
        print(koniec,end=" ")
        koniec=parent[koniec]
    print()
    return d[t]


if __name__=="__main__":
    G=[
    [(2, 8), (3, 8), (5, 4)],
    [(5, 5), (6, 6)],
    [(0, 8), (5, 4), (3, 4), (4, 8)],
    [(6, 7), (0, 8), (2, 4), (5, 8)],
    [(2, 8), (6, 2)],
    [(2, 4), (6, 8), (3, 8), (1, 5), (0, 4)],
    [(5, 8), (3, 7), (1, 6), (4, 2)]
    ]
    s=0
    t=6
    print("Długość:",Dijkstra(G,s,t))