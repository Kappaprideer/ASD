# Algorytm: 
# 1. DFS na grafie zapamiętując czasy przetrwarzania. 
# 2. Odwrócenie kierunku wszystkich krawędzi 
# 3. DFS w kolejnosci malejących czasów przetwarzania

from collections import deque
t=0
 
def DFS_visit(G, factory_time, visited, s):     # zwykły DFS_visit
    visited[s]=1
    global t
    t+=1
    for u in G[s]:
        if visited[u]==0:
            DFS_visit(G, factory_time, visited, u)
    t+=1
    factory_time[s]=t

def DFS(G):                                     # DFS zwracający tablice czasów
    factory_time=[0 for _ in range(len(G))]
    visited=[0 for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u]==0:
            DFS_visit(G, factory_time, visited, u)
    return factory_time


def SCC(G): # stronly connected component, wypisuje silnie spójne składowe
    aesthethic_printing=True # zmienna tylko do wypisywania
    tmp=DFS(G)
    S=deque()
    factory_time=[ (tmp[i], i) for i in range(len(tmp)) ]
    factory_time.sort(reverse=True)
    r_G=[ [] for _ in range(len(G))]
    for i in range(len(G)):
        for u in G[i]:
            r_G[u].append(i)
    visited=[ 0 for _ in range(len(r_G))]
    for g,u in factory_time:
        aesthethic_printing=False
        if visited[u]==0:
            S.append(u)
            visited[u]=1
        while len(S)>0:
            aesthethic_printing=True
            s=S.pop()
            print(s, end=" ")
            for k in r_G[s]:
                if visited[k]==0:
                    S.append(k)
                    visited[k]=1
        if aesthethic_printing:
            print()


if __name__=="__main__":
    graph=[[1],[2,3],[0,9],[5],[3,6],[4],[5],[9],[4,7],[10],[5,8]]
    SCC(graph)