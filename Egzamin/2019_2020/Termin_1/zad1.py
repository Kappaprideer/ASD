from zad1testy import runtests
from queue import PriorityQueue


def islands(G, A, B):
    n=len(G)
    T=[[10**10 for _ in range(n)] for j in range(10)]
    Q=PriorityQueue()
    T[1][A]=0
    T[5][A]=0
    T[8][A]=0
    for i in range(n):
        if G[A][i]!=0: 
            Q.put((G[A][i],i,0))
    
    # jaki transport, gdzie ide, za ile transport
    while not Q.empty():
        t, u, s= Q.get()
        if u==B:
            return t+s
        if T[t][u]>t+s:
            T[t][u]=t+s
            for i in range(n):
                if t==1:
                    if G[u][i]==5 and T[5][i]>T[t][u]+5:
                        Q.put((5,i,T[t][u]))
                    if G[u][i]==8 and T[8][i]>T[t][u]+8:
                        Q.put((8,i,T[t][u]))
                if t==5:
                    if G[u][i]==1 and T[1][i]>T[t][u]+1:
                        Q.put((1,i,T[t][u]))
                    if G[u][i]==8 and T[8][i]>T[t][u]+8:
                        Q.put((8,i,T[t][u]))
                if t==8:
                    if G[u][i]==1 and T[1][i]>T[t][u]+1:
                        Q.put((1,i,T[t][u]))
                    if G[u][i]==5 and T[5][i]>T[t][u]+5:
                        Q.put((5,i,T[t][u]))
    return None
        
runtests( islands ) 
