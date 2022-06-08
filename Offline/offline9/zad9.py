# Andrzej Zaborniak
from zad9testy import runtests
from collections import deque

# Złożoność alogrytmu to O(V^3E^2) 
# Program tworzy graf reprezentowany listą sąsiedztwa, oraz dwie dwuwymiarowe tablice: F - flow oraz C- Capacity które przetrzymują odpowiednio informacje:
# o danym przepływie w krawędzi [u][v] oraz maksymalnym przepływie w [u][v].
# Następnie dwie zagnieżdżone pętle odwzorowywują wybieranie wszystkich możliwych par ujść dodając sztucznie jedno super ujście o nieograniczonej
# przepustowości. Na tak stworzonym grafie używam metody Edmonca Karpa oraz porównuje otrzymany wynik ze wszystkimi poprzednimi wybierając największy.

def BFS(graph,F,C,s):     #graf jako lista sąsiedztwa, flow, capacity, start
    n=len(F)
    visited=[ 0 for _ in range(n)]
    minimum=[ 10**10 for _ in range(n)]
    P=[ None for _ in range(n)]
    q=deque()
    q.append(s)
    visited[s]=1

    while len(q)>0:
        s=q.popleft()
        for u in graph[s]:
            if visited[u]==0 and C[s][u]-F[s][u]>0:
                visited[u]=1
                P[u]=s
                minimum[u]=min(minimum[s],C[s][u]-F[s][u])
                q.append(u)
                if u ==len(F)-1:
                    return P, minimum[u]
    
    return None, minimum[len(F)-1]
    


def maxflow(G,s):
    n=0
    odpowiedz=0
    for u in G:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=2
    C=[[ 0 for _ in range(n)] for i in range(n)]
    graph=[[] for _ in range(n)]

    for u in G:
        graph[u[0]].append(u[1])
        graph[u[1]].append(u[0])
        C[u[0]][u[1]]=u[2]

    for x in range(n):
        for y in range(x+1,n):
            if x!=s and y!=s:

                F=[ [ 0 for _ in range(n)] for i in range(n)]
                C[x][n-1]=10**10
                C[y][n-1]=10**10
                graph[x].append(n-1)
                graph[n-1].append(x)
                graph[y].append(n-1)
                graph[n-1].append(y)
                
                P, minimum=BFS(graph,F,C,s)
                while P!=None:
                    u=n-1
                    while u!=s:
                        F[P[u]][u]+=minimum
                        F[u][P[u]]-=minimum
                        u=P[u]
                    P, minimum=BFS(graph,F,C,s)


                C[x][n-1]=0
                C[y][n-1]=0
                graph[x].pop()
                graph[y].pop()
                graph[n-1].pop()
                graph[n-1].pop()

                suma=0
                for i in range(n):
                    suma+=F[s][i]
                odpowiedz=max(odpowiedz,suma)

    return odpowiedz
   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )