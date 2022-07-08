# Ścieżki w Dagu,
# Należy policzyć ile jest możliwych ścieżek od wierzchołka s do t w DAG-u.
# ------------------------------------------------------------------------
# Trochę brut, za kazdym razem jak dojde do wierzchołka t to zwiększam ilość wynik o 1


answer=0

def DFS_visit(G,d,u,t):
    if u==t:
        global answer
        answer+=1
    for s in G[u]:
        DFS_visit(G,d,s,t)

if __name__=="__main__":
    graph=[ (2,1),(2,0),(0,3),(1,3),(1,4),(3,4)]
    s=2
    t=4
    n=0
    for u in graph:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1
    G= [ [] for _ in range(n)]
    for u in graph:
        G[u[0]].append(u[1])
    d=[0 for _ in range(n)]
    DFS_visit(G,d,s,t)
    
    print(answer)