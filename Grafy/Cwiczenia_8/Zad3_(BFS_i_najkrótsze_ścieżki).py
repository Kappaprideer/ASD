from collections import deque

def BFS(G,s):
    n=len(G)
    visited=[ 0 for _ in range(n)]
    parent=[ None for _ in range(n)]
    Q=deque()
    visited[s]=1
    Q.append(s)
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                parent[u]=s
                Q.append(u)
    return parent

def shortest_path(G,s,t):
    path=BFS(G,s)
    while t!=s:
        print(t,end=" ")
        t=path[t]
    print(s)


if __name__=="__main__":
    s=2
    t=4
    G=[
    [1,2,3],
    [0,2,5],
    [1,0],
    [0,4,6],
    [3,6],
    [1,6],
    [3,4,5]
    ]
    shortest_path(G,s,t)