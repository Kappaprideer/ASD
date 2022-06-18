v=0
maximum=0

def DFS_visit(G,d,visited,parent,s):
    global v, maximum
    for u,w in G[s]:
        if visited[u]==0:
            d[u]=d[s]+w
            parent[u]=s
            if d[u]>maximum:
                v=u
                maximum=d[u]
            visited[u]=1
            DFS_visit(G,d,visited,parent,u)
    

def bestroot(G):
    global v, maximum
    v=0
    maximum=0
    n=len(G)
    visited=[0 for _ in range(n)]
    d=[0 for _ in range(n)]
    parent=[None for _ in range(n)]
    visited[0]=1
    d[0]=0
    DFS_visit(G,d,visited,parent,0)
    maximum=0
    visited=[0 for _ in range(n)]
    parent=[None for _ in range(n)]
    d=[0 for _ in range(n)]
    visited[v]=1
    DFS_visit(G,d,visited,parent,v)
    result=v
    current=10**10
    while v is not None:
        if abs(maximum//2-d[v])<current:
            current=abs(d[v]-maximum//2)
            result=v
        v=parent[v]
    return result


if __name__=="__main__":
    G=[
    [(4,2),(7,10),(5,1)],
    [(2,2)],
    [(1,2),(5,15)],
    [(8,2)],
    [(0,2)],
    [(2,15),(0,1),(8,10)],
    [(8,3)],
    [(0,10)],
    [(5,10),(6,3),(3,2)]
    ]
    print(bestroot(G))
