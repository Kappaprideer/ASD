# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek

def DFS_visit(G,visited,s):
    visited[s]=1
    for u in G[s]:
        if visited[u]==0:
            DFS_visit(G,visited,u)

def good_beginning(G):
    kandydat=0
    n=len(G)
    visited=[0 for _ in range(n)]
    for i in range(n):
        if visited[i]==0:
            kandydat=i
            DFS_visit(G,visited,i)
    
    visited=[0 for _ in range(n)]
    DFS_visit(G,visited,kandydat)
    for x in visited:
        if x==0:
            return None
    return kandydat


if __name__=="__main__":
    G=[
    [2,5],
    [3],
    [1,3],
    [],
    [2],
    [3,4]
    ]
    print(good_beginning(G))