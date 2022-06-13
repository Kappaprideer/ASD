import queue

# Reprezentacja grafu [[(2,5), (4,6)]]

# DIJKSTRA 
def w(u,v):
    return None

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

# -------------------------------------------

# Algorytm Kruskala znajdywania MST
# Struktura zbiorów rozłącznych jest dana 

# Reprezentacja grafu [ (5,1,2), (7,2,3), ...] zbiór krawędzi, pierwszy element to waga

class Node:
    def __init__(self,value):
        self.parent=self
        self.value=value
        self.rank = 0 

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 
    if x.rank>y.rank:
        y.parent =x 
    else:
        x.parent=y 
        if x.rank == y.rank:
            y.rank+=1



def kruskal(G):
    G=sorted(G, key=lambda x: x[0])
    E = len(G)
    v=0
    for i in range(E):
        if G[i][2]>v:
            v=G[i][2]
    D = [None for _ in range(v)]
    for u in range(v):
        D[u]=Node(u)
    MST = [] 
    for e in range(len(G)):
        if find(D[[G[e][1]]]) != find(D[G[e][2]]):
            union(D[G[e][1]], D[G[e][2]])
            MST.append(D[e])
    return MST
    
# --------------------------------------------
# Szukanie ścieżki hamilltona w DAGU 
# Posortować graf topologicznie i sprawdzić czy kolejne wierzchołki mają między sobą połączenie, jeżeli tak to to jest ta ścieżka
# jeżeli między dwoma kolejnymi wierzchołkami nie ma połączenia to ścieżka hamiltona nie istnieje. 

# --------------------------------------------
# Dobry początek 
# wierzchołek v w grafie skierowanym nazywamy wierzchołek od którego wszystkie inne są osiągalne
# (tzw. źródło)
# znaleźć silnie spójne skłądowe, następnie posortować topologicznie silnie spójne składowe. następnie sprawdzamy czy 
# z pierwszego da się dojść do wszystkich innych 
# ---   ----    ----    ---  ----    ----    ---- 
# Puszczając DFS-a zapamiętujemy ostatni wierzchołek od którego poleciał DFS, i na samym końcu ponownie puszczamy z niego DFS i sprawdzamy 
# czy z niego da się dojsc do wszystkich innych. Jeżeli tak to znaczy że jest on źródłem. 

# -----------------------------------------------
# Znalezienie ścieżki o najmniejszym koszcie w DAGu:
# Posortować topologicznie graf a nastepnei puścić relax idąc po kolei w posortowanym grafie 

# -----------------------------------------------
# Ścieżka o minimalnym iloczynie 
# Zastąpić mnożenie przez sumowanie logarytmów a następenie zastosować algorytm Dikstry 

