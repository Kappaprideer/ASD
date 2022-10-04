# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
# malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).
from queue import PriorityQueue

def decreasingedges(G,x,y):
    n=len(G)
    d=[10**10 for _ in range(n)]
    edges=[]

    for i in range(n):
        for u in G[i]:
            edges.append((i,u[0],u[1]))

    edges.sort(key= lambda k: k[2], reverse=True)
    d[x]=0

    Q=PriorityQueue()
    for u,v,w in edges:
        if d[v]>d[u]+w:
            d[v]=d[u]+w
            Q.put((w,v))
        while not Q.empty():
            tmp,g= Q.get()
            for s in G[g]:
                if d[s[0]]>d[g]+s[1]:
                    d[s[0]]=d[g]+s[1]
                    Q.put((s,s[1]))
    print(d)
    return d[y]





if __name__=="__main__":
    G=[
    [(1,19),(3,8)],
    [(7,5)],
    [(0,20),(5,3)],
    [(6,6)],
    [],
    [(4,2)],
    [(2,4)],
    [(0,10),(4,1)]
    ]
    print(decreasingedges(G,0,4))