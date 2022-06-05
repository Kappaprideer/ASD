from zad9testy import runtests
from collections import deque

# Program tworzy nowy graf resuidalny reprezentowany w postaci macierzowej. Dla wszystkich możliwych dwóch ujść program osobno tworzy graf resuidalny z połączonymi
# ujściami w jedno super ujśćie oraz uruchamia algorytm Endmondsa-Krapa. Na końcu porównuje wszystkie możliwe wyniki wybierając sumę dwóch ujść o największym przepływie.
# Złożoność alogrytmu to O(V^3E^2) 

def BFS(graph,R,s,parent):
    n=len(R)
    PQ=deque()
    visited = [ 0 for _ in range(n)]
    visited[s]=1
    PQ.append(s)
    while len(PQ)>0:
        s=PQ.popleft()
        for u in range(n):
            if R[s][u][0]>0 and visited[u]==0:
                parent[u]=s
                visited[u]=1
                PQ.append(u)
                if u==n-1:
                    return True, parent
    return False, parent


def maxflow( G,s ):
    v=0
    for u in G:
        v=max(v,u[1])
        v=max(v,u[0])
    v+=2
    odpowiedz=0
    parent=[ None for _ in range(v)]
    graph =[ [] for _ in range(v)]
    for u in G:
        graph[u[0]].append((u[1],u[2]))
        # graph[u[1]].append((u[0],0))    

    HI =[ [[0,0] for _ in range(v)] for i in range(v) ]
    for u in G:
        HI[u[0]][u[1]]=[u[2],1]
    
    E = [0 for _ in range(v)] 

    for x in range(v-1):
        for y in range(x+1,v-1):
            if x!=s and y!=s:
                sum_x=0
                sum_y=0
                R=HI.copy()
                for u in graph[x]:
                    R[x][u[0]][0]=0
                    sum_x+=u[1]
                    # R[u[0]][x][0]=0
                for u in graph[y]:
                    R[y][u[0]][0]=0
                    sum_y+=u[1]
                    # R[u[0]][y][0]=0

                R[x][v-1][0]=sum_x
                R[y][v-1][0]=sum_y

                # E = [0 for _ in range(v)]                       # Tablica wartosci przeplywu w krawedziach 
                exist, parent = BFS(graph,R,s,parent)
                city=parent[v-1]
                value=10**10
                while exist:

                    while city!=s:
                        value=min(value,R[parent[city]][city][0])
                        city=parent[city]
                    
                    city=parent[v-1]
                    while city!=s:
                        if R[parent[city]][city][1]==1:
                            E[city]+=value
                        else:
                            E[city]-=value
                        R[parent[city]][city][0]-=value
                        R[city][parent[city]][0]+=value 
                        city=parent[city]

                    exist, parent=BFS(graph,R,s,parent)
                    city=parent[v-1]
                    value=10**10

                odpowiedz=max(odpowiedz,E[x]+E[y])
                
                for u in graph[x]:
                    R[x][u[0]][0]=u[1]
                for u in graph[y]:
                    R[y][u[0]][0]=u[1]
                R[x][v-1][0]=0
                R[y][v-1][0]=0
                R[v-1][x][0]=0
                R[v-1][y][0]=0

    return odpowiedz
   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )