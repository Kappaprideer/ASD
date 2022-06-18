from queue import PriorityQueue

def shortestpath(G,t):
    n=len(G)                                # wierzchołki parzyste - prowadzi BOB, wierzchołki nieparzyste - prowadzi ALICE 
    H=[ [] for _ in range(2*(n+1))]
    parent=[ None for _ in range(2*(n+1))]
    visited=[0 for _ in range(2*(n+1))]
    d=[10**10 for _ in range(2*(n+1))]
    H[0].append((1,0))
    H[0].append((2,0))
    for i in range(n):
        vert=G[i]
        for u,w in vert:
            H[(i*2)+1].append(((u*2)+2,w))
            H[(i*2)+2].append(((u*2)+1,0))
    
    d[0]=0
    visited[0]=0
    Q=PriorityQueue()
    Q.put(0)
    while not Q.empty():
        s=Q.get()
        for u in H[s]:
            if visited[u[0]]==1 and d[u[0]]>d[s]+u[1]:
                d[u[0]]=d[s]+u[1]
                parent[u[0]]=s
                Q.put(u[0])
            if visited[u[0]]==0:
                d[u[0]]=d[s]+u[1]
                visited[u[0]]=1
                parent[u[0]]=s
                Q.put(u[0])
    path=[]

    if d[t*2+1]<d[t*2+2]:
        tmp=t*2+1
        while parent[tmp]!=None:
            path.append((tmp-1)//2)
            tmp=parent[tmp]
        path=path[::-1]
        print(path)
        print()
        return d[t*2+1]
    
    tmp=t*2+2
    while parent[tmp]!=None:
        path.append((tmp-1)//2)
        tmp=parent[tmp]
    path=path[::-1]
    print(path)
    print()
        
    return d[t*2+2]

if __name__=="__main__":
    G=[
    [(4, 5), (3, 8), (5, 10)],
    [(6, 4), (2, 9)],#, (4, 11)],
    [(5, 5), (1, 9), (3, 20)],
    [(4, 20), (0, 8), (2, 20)],
    [(0, 5), (3, 20)],#, (1, 11)],
    [(0, 10), (2, 5), (6, 7)],
    [(5, 7), (1, 4)]
    ]
    print(shortestpath(G,1))
