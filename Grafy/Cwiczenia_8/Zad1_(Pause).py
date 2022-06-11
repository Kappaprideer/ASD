# W jakiej kolejnosci wyłączać stacje by graf został jak najdłuzej spójny
# --------------------------------------------------------
# Rozwiązanie:
# Po przejściu DFS-a odłączać po kolei wierchołki w malejącym czasie przetworzenia

time=0
def DFS_visit(G,visited,u,factory_time):
    global time
    visited[u]=1
    time +=1
    for s in G[u]:
        if visited[s]==0:
            DFS_visit(G,visited,s,factory_time)
    time+=1
    factory_time[u]=time

def DFS(G):
    n=len(G)
    visited=[ 0 for _ in range(n)]
    factory_time=[ 0 for _ in range(n)]
    for i in range(n):
        if visited[i]==0:
            DFS_visit(G,visited,i,factory_time)
    vactor= [ (factory_time[i], i) for i in range(n)]
    vactor.sort()
    factory_time=[ u[1] for u in vactor]
    return factory_time


if __name__=="__main__":
    G=[
    [2,3,4,7],
    [2,4,5],
    [0,1,4,7],
    [0,4],
    [0,3,1,2,5],
    [1,4,6],
    [5],
    [0,2],
    ]
    print(DFS(G))