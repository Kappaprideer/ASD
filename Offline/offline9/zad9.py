from zad9testy import runtests
from collections import deque

# Program tworzy nowy graf resuidalny reprezentowany w postaci macierzowej. Dla wszystkich możliwych dwóch ujść program osobno tworzy graf resuidalny z połączonymi
# ujściami w jedno super ujśćie oraz uruchamia algorytm Endmondsa-Krapa. Na końcu porównuje wszystkie możliwe wyniki wybierając sumę dwóch ujść o największym przepływie.
# Złożoność alogrytmu to O(V^3E^2) 

def BFS(R,s):
    n=len(R)
    PQ=deque()
    visited = [ 0 for _ in range(n)]
    visited[s]=1
    parent = [ None for _ in range(n)]
    PQ.append(s)
    while len(PQ)>0:
        s=PQ.popleft()
        for i in range(n):
            if R[s][i][0]>0 and visited[i]==0:
                parent[i]=s
                visited[i]=1
                PQ.append(i)
                if i==n-1:
                    return True, parent
    return False, parent


def maxflow( G,s ):
    
    v=0
    for u in G:
        v=max(v,u[1])
        v=max(v,u[0])
    v+=2
    odpowiedz=0

    for x in range(v-1):
        for y in range(x+1,v-1):
            if x!=s and y!=s:

                R =[ [[0,0] for _ in range(v)] for i in range(v) ]
                for u in G:
                    if u[0]!=x and u[0]!=y:                                         # R - tablica resuidalna
                        R[u[0]][u[1]]=[u[2],1]
                R[x][v-1][0]=10**10
                R[y][v-1][0]=10**10

                E = [0 for _ in range(v)]             # Tablica wartosci przeplywu w krawedziach 
                exist, parent = BFS(R,s)
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

                    exist, parent=BFS(R,s)
                    city=parent[v-1]
                    value=10**10

                odpowiedz=max(odpowiedz,E[x]+E[y])
                

    return odpowiedz
   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )