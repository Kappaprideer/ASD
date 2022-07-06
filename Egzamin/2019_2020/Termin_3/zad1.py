from zad1testy import runtests
from collections import deque

def best_root( L ):
    n = len(L)
    visited=[0 for _ in range(n)]
    d=[0 for _ in range(n)]
    root=None
    maximum=0
    Q=deque()
    Q.append(0)
    visited[0]=1
    while len(Q)>0:
        s=Q.popleft()
        for u in L[s]:
            if visited[u]==0:
                d[u]=d[s]+1
                visited[u]=1
                if d[u]>maximum:
                    maximum=d[u]
                    root=u
                Q.append(u)

    d=[0 for _ in range(n)]
    visited=[0 for _ in range(n)]
    path=[-1 for _ in range(n)]
    maximum=0
    visited[root]=1
    Q.append(root)
    while len(Q)>0:
        s=Q.popleft()
        for u in L[s]:
            if visited[u]==0:
                visited[u]=1
                path[u]=s
                d[u]=d[s]+1
                if d[u]>maximum:
                    maximum=d[u]
                    root=u
                Q.append(u)

    while root!=-1:
        if maximum//2==d[root]:
            return root
        root=path[root]





    return None


runtests( best_root ) 
