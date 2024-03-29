from collections import deque
from queue import PriorityQueue

def MST(G):
    n=len(G)
    visited=[0 for _ in range(n)]
    parent=[ None for _ in range(n)]
    d=[10**10 for _ in range(n)]
    Q=deque()
    d[0]=0
    visited[0]=1
    Q.append(0)
    while len(Q):
        s=Q.popleft()
        for u in G[s]:
            if visited[u[0]]==1 and d[u[0]]>u[1] and u[0]!=parent[s]:
                d[u[0]]=u[1]
                parent[u[0]]=s
            if visited[u[0]]==0:
                d[u[0]]=u[1]
                parent[u[0]]=s
                visited[u[0]]=1
                Q.append(u[0])

    return parent

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

    path=MST(G)
    print("Krawedzie minimanego drzewa rozpinajacego:")
    for i in range(1,len(path)):
        print(i,"<-->", path[i],end=" | ")
    print()




