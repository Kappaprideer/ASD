# Średnicą drzewa są dwa najdalej oddalone od siebie krawędzie w grafie, algorytm ma przyjmować graf reprezentowany listą krawędzi
# oraz zwrócić jego średnicę.
# Drzewo - graf acykliczny, nieskierowany
# -----------------------------------
# Rozwiązanie:
# Puścic BFS z dowolnego wierzchołka, i znaleźć wierzchołek najdalej oddalony, następnie z tamtego wierzchołka puśić BFS i znaleźć najdłuższą ścieżkę.
# Ścieżka ta bedzie średnicą drzewa.

from collections import deque

def tree_diameter(T):
    n=0
    for u in T:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1
    G= [ [] for _ in range(n)]
    for u in T:
        G[u[0]].append(u[1])
        G[u[1]].append(u[0])
    Q=deque()
    d=[ 10**10 for _ in range(n)]
    visited=[0 for _ in range(n)]
    Q.append(0)
    d[0]=0
    visited[0]=1
    maximum=0
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                d[u]=d[s]+1
                if d[u]>maximum:
                    maximum=d[u]
                    vertex=u
                Q.append(u)
    visited=[0 for _ in range(n)]
    d=[0 for _ in range(n)]
    maximum=0
    d[vertex]=0
    visited[vertex]=1
    Q.append(vertex)
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                d[u]=d[s]+1
                maximum=max(maximum,d[u])
                Q.append(u)
    return maximum


if __name__=="__main__":
    tab=[[0,1],[0,6],[1,2],[1,3],[1,4],[4,5],[6,7],[6,8]]
    print(tree_diameter(tab))
