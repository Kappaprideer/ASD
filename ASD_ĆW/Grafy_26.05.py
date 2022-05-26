import queue


def relax(u,v,d,parent, PQ):
    if d[v] > d[u] + w(u,v):
        d[v] = d[u] + w(u,v)
        parent[v]=u
        PQ.put((d[v],v))

def dijkstra(G,s):
    v=len(G)
    d = [ float('inf') for _ in range(v)]
    parent = [ None for _ in range(v)]
    d[s] = 0 
    PQ = queue.PriorityQueue()
    PQ.put((d[s],s))
    while not PQ.empty():
        prior, u = PQ.get()
        for p in G[u]:
            relax(u, p[0], d, parent, PQ)