#Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach

from queue import PriorityQueue
from collections import deque

def malejace_wagi(graph,s,t):
    n=0
    for u in graph:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1

    G=[ [] for _ in range(n)]
    for u in graph:
        G[u[0]].append(u[1])
        G[u[1]].append(u[0])

    visited=[0 for _ in range(n)]
    available=[ 0 for _ in range(n)]
    
    available[s]=1
    graph.sort(key= lambda x: x[2], reverse=True)
    for u in graph:
        if available[u[0]]==1 or available[u[1]]==1:
            available[u[0]]=1
            available[u[1]]=1    
    
    Q=deque()
    Q.append(s)
    visited[s]==1
    while len(Q)>0:
        s=Q.popleft()
        for e in G[s]:
            if visited[e]==0 and available[e]==1:
                visited[e]=1
                Q.append(e)
                if e==t:
                    return True
    
    return False


    
if __name__=="__main__":
    # Graf reprezentowany w postaci listy krawędzi
    G=[
    (0,2,5),
    (3,0,7),
    (2,3,8),
    (3,1,2),
    (2,1,4),
    (2,5,6),
    (1,5,9),
    (1,4,3),
    (4,5,1),
    (0,6,10)
    ]
    s=3
    t=5

    print("Graf ma sciezke od",s,"do",t,":",malejace_wagi(G,s,t))