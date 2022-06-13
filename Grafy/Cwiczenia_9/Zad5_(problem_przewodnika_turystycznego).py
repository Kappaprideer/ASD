from queue import PriorityQueue
from collections import deque

def Dijksta_with_wild_argument(G,s,t):
    n=len(G)
    visited=[ 0 for _ in range(n)]
    d=[ 0 for _ in range(n)]
    parent=[ None for _ in range(n)]
    Q=PriorityQueue()
    visited[s]=1
    d[s]=10**10

    for u in G[s]:
        visited[u[0]]=1
        parent[u[0]]=s
        d[u[0]]=u[1]
        Q.put((-1*u[1],u[0]))

    while not Q.empty():
        s=Q.get()
        for u in G[s[1]]:
            if visited[u[0]]==1 and min(d[s[1]],u[1])>d[u[0]]:
                d[u[0]]=min(d[s[1]],u[1])
                parent[u[0]]=s[1]
                Q.put((-1*u[1],u[0]))

            if visited[u[0]]==0:
                d[u[0]]=min(d[s[1]],u[1])
                visited[u[0]]=1
                parent[u[0]]=s[1]
                Q.put((-1*u[1],u[0]))

    return d[t]

def groupamount(G,s,t):
    n=0
    for u in G:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1
    graph=[ [] for _ in range(n)]
    for u in G:
        graph[u[0]].append((u[1],u[2]))
        graph[u[1]].append((u[0],u[2]))
        
    for line in graph:
        print(line)

    print(Dijksta_with_wild_argument(graph,s,t))

if __name__=="__main__":
    G=[ (0,4,5),(4,3,20),(0,3,8),(0,5,10),(5,2,5),(5,6,7),(6,1,4),(2,1,9),(3,2,20),(4,1,11)]
    groupamount(G,0,1)