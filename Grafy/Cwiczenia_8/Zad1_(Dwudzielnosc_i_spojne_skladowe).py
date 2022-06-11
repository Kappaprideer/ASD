from collections import deque


def dwudzielnosc(G):
    n=len(G)
    visited=[ 0 for _ in range(n)]
    color=[ 0 for _ in range(n)]
    Q=deque()
    Q.append(0)
    color[0]=1
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==1 and color[u]==color[s]:
                return False
            if visited[u]==0:
                color[u]=3-color[s]
                visited[u]=1
                Q.append(u)
    return True

def DFS_visit(G,visited,s):
    visited[s]=1
    for u in G[s]:
        if visited[u]==0:
            visited[u]=1
            DFS_visit(G,visited,u)

def ilosc_spojnych_skladowych(G):
    n=len(G)
    visited=[0 for _ in range(n)]
    result=0
    for u in range(n):
        if visited[u]==0:
            DFS_visit(G,visited,u)
            result+=1
    return result



if __name__=="__main__":
    G=[
    [5,4,7],
    [3,6],
    [7],
    [1],
    [0],
    [0],
    [1,7],
    [0,2,6]
    ]
    H=[
    [1,3,6],
    [3,0,6],
    [4,7],
    [0,1],
    [2,5,7],
    [4],
    [0,1],
    [4,2]
    ]
    print("Graf jest dwudzielny:", dwudzielnosc(G))
    print("Ilosc spojnych skladowych w grafie:", ilosc_spojnych_skladowych(H))