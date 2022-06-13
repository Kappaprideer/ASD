# Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?
# ------------------------------------------------------------
# Rozwiązanie:
# Należy posortować wierzchołki topologicznie,a następnie puścić na nich BFS-a, szukającego najktórszych ścieżek.
from collections import deque

def visit(G,visited,sorted_G,s):
    visited[s]=1
    for u in G[s]:
        if visited[u]==0:
            visited[u]=1
            visit(G,visited,sorted_G,u)
    sorted_G.append(s)

def topological_sorting(G):
    n=len(G)
    arr=[]
    visited=[0 for _ in range(n)]
    for i in range(n):
        if visited[i]==0:
            visit(G,visited,arr,i)
    
    arr=arr[::-1]
    return arr

def shortest_paths(G):
    Q=deque()
    n=len(G)
    arr=topological_sorting(G)
    visited=[0 for _ in range(n)]
    d=[0 for _ in range(n)]

    Q.append(arr[0])
    d[arr[0]]=0
    visited[arr[0]]=1
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                d[u]=d[s]+1
                Q.append(u)
    return d

if __name__=="__main__":
    G=[
    [2,5],
    [3],
    [1,3],
    [],
    [2],
    [3,4]
    ]
    tab=shortest_paths(G)
    print("Wierzcholek: | Dlugosc do wierzcholka: ")
    for i in range(len(tab)):
        print(i,":",tab[i],end=" | ")
    print()