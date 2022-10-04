from zad1testy import runtests
from queue import PriorityQueue


def jak_dojade(G, P, D, a, b):
    n=len(G)
    end=0
    d=[[ 10**10 ]*(D+1) for _ in range(n)]
    parent=[ [[-1,-1]]*(D+1) for _ in range(n)]
    for i in range(D):
        d[a][i]=0
    Q=PriorityQueue()
    Q.put((0,a,D))        # trasa przebyta do wierzchołka, wierzchołek do którego się dojechało, ilość paliwa w baku
    while not Q.empty():
        g=Q.get()
        s=g[1]
        bak=g[2]
        paliwo=bak
        if s==b:
            path=[]
            while b!=-1:
                path.append(b)
                if paliwo==D:
                    minimum=0
                    for i in range(n):
                        if d[parent[b][paliwo][0]][i]<d[b][minimum]:
                            minimum=i
                    b,paliwo=parent[b][paliwo]
                    paliwo=minimum
                else:
                    b, paliwo = parent[b][paliwo]
            path=path[::-1]
            return    

        for x in P:
            if x==s:
                bak=D
        
        for i in range(n):
            if G[s][i]!=-1 and bak-G[s][i]>=0 and d[i][bak-G[s][i]]>g[0]+G[s][i]:
                d[i][bak-G[s][i]]=g[0]+G[s][i]
                parent[i][bak-G[s][i]]=(s,bak-G[s][i])
                Q.put((d[i][bak-G[s][i]], i, bak-G[s][i]))

    return None

        

runtests( jak_dojade ) 
