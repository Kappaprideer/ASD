# Krasnoludy i Trolle 
# Wyobraźmy sobie że są połączone jaskienie trolli oraz ogrów. Jest jedna jaskina trolli, wiedzą one ile jest w każdej innej jaskini ogrów, planują one
# podstawić materiały wybuchowe do jednego z przejść w taki sposób aby odciąć od siebie drogę jak największej liczbie ogrów. Które przejście powinni wybrać ?
# ---------------------------------------------------------------------------------------------------
# Rozwiązanie:
# Szukamy mostu za każdym razem zliczając zarazem ile w danym podgrafie jest łącznie ogrów. 

from collections import deque


time=0
v=0

def DFS(G,values,s,visited,parent,d,low, edges, number_of_orks):
    global v, time
    time+=1
    number_of_orks[s]=v
    visited[s]=1
    v+=values[s]
    d[s]=time
    low[s]=time
    for u in G[s]:
        if visited[u]==1 and parent[s]!=u:
            low[s]=min(low[u],low[s])            
        if visited[u]==0:
            parent[u]=s
            DFS(G,values,u,visited,parent,d,low,edges,number_of_orks)
    
    if parent[s] is not None:
        low[parent[s]]=min(low[parent[s]],low[s])
        if d[s]==low[s]:
            sum_of_orks=v-number_of_orks[s]
            edges.append((parent[s],s,sum_of_orks))
    
    visited[s]=2



def where_dynamit(G,values,u):
    n=len(values)
    visited =[ 0 for _ in range(n)]
    parent = [ None for _ in range(n)]
    d =[ 10**10 for _ in range(n)]
    low = [ 10**10 for _ in range(n)]
    number_of_orks=[ 0 for _ in range(n)]
    edges=[]
    visited[s]=1
    DFS(G,values,s,visited,parent,d,low, edges, number_of_orks)
    edges.sort(key=lambda x: x[2], reverse=True)
    return (edges[0][0],edges[0][1])


if __name__=="__main__":
    values_in_vertices=[20,40,5,8,7,200,0,18,10,10]                                              # (vertice, number of orgs in vertice)
    edges=[(0,1),(0,2),(1,2),(2,3),(9,8),(8,6),(6,4),(4,3),(3,6),(4,5),(5,7),(4,7),(6,5)]        # undirected list of edges
    G=[[] for _ in range(len(values_in_vertices))]                                               # Graf w reprezentacji listy sąsiedztw
    for e in edges:
        G[e[0]].append(e[1])    
        G[e[1]].append(e[0])    
    s=6                                                                                          # vertice where trolls are
    print(where_dynamit(G,values_in_vertices,s))
