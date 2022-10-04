
from queue import PriorityQueue
from collections import deque


def minimalcost(G,s,t):
    n=len(G)
    visited=[ 0 for _ in range(n)]
    d=[ 10**10 for _ in range(n)]
    parent=[ None for _ in range(n)]
    Q=deque()
    visited[s]=1
    d[s]=0
    beginning=s
    end=t
    Q.append(s)
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u[0]]==1 and d[u[0]]>d[s]+u[1]:
                parent[u[0]]=s
                d[u[0]]=d[s]+u[1]
                Q.append(u[0])
            if visited[u[0]]==0:
                visited[u[0]]=1
                d[u[0]]=d[s]+u[1]
                parent[u[0]]=s
                Q.append(u[0])

    while end!=beginning and end!=None:
        print(end,end=" ")
        end=parent[end]
    print(beginning)

    return d[t]

if __name__=="__main__":
    # lista krawędzi z wagami zamieniona na graf
    graph=[
    (0,7,1),(7,6,1),(6,8,0),(8,2,1),(2,3,0),(3,5,1),(5,4,0),(4,0,0),(4,1,1),(3,1,1),(1,8,0),(7,1,1),(7,8,0)
    ]
    n=0
    for u in graph:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1

    G=[ [] for _ in range(n)]
    for u in graph:
        G[u[0]].append((u[1],u[2]))
        G[u[1]].append((u[0],u[2]))
    s=3
    t=7
    print("Minimalny koszt:",minimalcost(G,s,t))