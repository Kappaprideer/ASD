# Dostarczenie przesyłek
# Dane jest N, oraz N-1 dróg dwukierunkowych, układ dróg tworzy graf spójny. Mając listę K miast do których musimy dostarczyć przesyłki i mogąc wystartować i zakończyć
# trasę w dowolnym mieście, podaj minimalny dystans, który musimy przebyć, żeby zrealizować to zadanie.
# -------------------------------------------------------------------------------------------------------
# Rozwiązanie:
# Szukamy średnicy w grafie ponieważ graf ten jest drzewem, a następnie przechodząc po średnicy sprawdamy długość rozgałęzień które nie należą do średnicy, ale
# do których również należy dostarczyć paczki, długości do tych miast mnożymy razy dwa, ponieważ trzeba jeszcze wrócić do średnicy i na końcu dodajemy długość
# średnicy drzewa.

from collections import deque
from lib2to3.pytree import Node

def delivery(G,S):
    n=len(G)
    check=[ False for _ in range(n)]
    for i in S:
        check[i]=True

    Q=deque()
    visited =[ 0 for _ in range(n)]
    d = [ 10**10 for _ in range(n)]
    path = [ None for _ in range(n)]
    node=0
    maximum=0

    Q.append(0)
    visited[0]=1
    d[0]=0
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                path[u]=s
                d[u]=d[s]+1
                if d[u]>maximum and check[u]:
                    maximum=d[u]
                    node=u
                Q.append(u)
    maximum=0
    d= [0 for _ in range(n)]
    visited =[ 0 for _ in range(n)]
    visited[node]=1
    path[node]=None
    Q.append(node)
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                path[u]=s
                d[u]=d[s]+1
                if d[u]>maximum and check[u]:
                    maximum=d[u]
                    node=u
                Q.append(u)
    answer=maximum
    diameter=[ 0 for _ in range(maximum+1)]
    visited=[0 for _ in range(n)]
    for i in range(maximum+1):
        visited[node]=1
        diameter[i]=node
        node=path[node]
    for i in diameter:
        Q.append(i)
        d[i]=0
        while len(Q)>0:
            s=Q.popleft()
            for u in G[s]:
                if visited[u]==0:
                    d[u]=d[s]+1
                    visited[u]=1
                    if check[u]:
                        answer+=d[u]*2
                        d[u]=0
                    Q.append(u)
    return answer


if __name__=="__main__":
    graph=[(1,2),(1,0),(0,3),(0,15),(15,4),(15,16),(16,17),(4,6),(4,5),(0,8),(7,8),(8,9),(9,10),(8,13),(13,12),(12,11),(11,14)] # graph - graf reprezentowany w postaci listy krawędzi
    n=0
    for u in graph:
        n=max(n, u[0])
        n=max(n, u[1])
    n+=1
    G=[ [] for n in range(n)]       # G - graf reprezentowany w postaci listy sąsiedztwa
    for u in graph:
        G[u[0]].append(u[1])
        G[u[1]].append(u[0])
    S=[8,7,2,4,6,12,11,14,17]             # S - listwa krawędzi do których należy dostarczyć przesyłki
    print(delivery(G,S))
