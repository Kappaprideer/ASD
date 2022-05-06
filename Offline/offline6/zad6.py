from zad6testy import runtests
from queue import Queue
def longer( G, s, t ):
    v=len(G)
    Q=Queue()
    paths=[]
    parents=[None for _ in range(v)] #skąd można przyjść do wierzchołka u
    visited=[0 for _ in range(v)]   #czy wierzchołek został odwiedzony
    d=[-1 for _ in range(v)]        #odległość wierzchołków od wierzchołka s
    visited[s]=1
    parents[s]=0
    d[s]=0
    d[t]=10**10
    Q.put(s)
    while not Q.empty():
        p=Q.get()
        for u in G[p]:
            if u==t:
                if d[p]+1<=d[t]:
                    d[t]=d[p]+1
                    paths.append(p)
                break
            elif visited[u]==0:
                visited[u]=1
                parents[u]=p
                d[u]=d[p]+1
                Q.put(u)
    
    if len(paths)==1:
        return (paths[0],t)
    if len(paths)==0:
        return None
    
    
            


    # return (0,0)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )