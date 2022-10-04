# Złożoność obliczeniowa to O(V+E+t^2) gdzie t jest równe długości najkrótszej ścieżki w grafie (V,E)
# Program przeszukuje graf w szerz startując w wierzchołlku s, następnie dla każdego odwiedzonego wierzchołka zapisuje w nim rodzica z którego przyszedł
# oraz długosć jaką musiał pokonać. Wyjątkiem jest wierzchołek t w którym zapisuje się wszystkich rodziców z których mozna dojść do wierzchołka t pokonując
# minimalną odległość. Jeśli wierzchołek t ma tylko jednego rodzica to wystarczy usunąć krawędź łączącą go z nim, w przeciwnym wypadku jeśli rodziców jest więcej
# usunąć można jedynie wspólną krawędź dla wszytkich ścieżek. Program porównuje dwie ścieżki szukając tej samej krawędzi i w momencie znalezienia sprawdza czy każda 
# ścieżka posiada tą samą krawędź w tym samym miejscu, jeżeli tak to właśnie ją nalezy usunąć, w przeciwnym wypadku program zwraca False.

from zad6testy import runtests
from collections import deque

def longer( G, s, t ):
    v=len(G)
    Q=deque()
    paths=[]
    parents=[None for _ in range(v)]    #skąd można przyjść do wierzchołka u
    visited=[0 for _ in range(v)]       #czy wierzchołek został odwiedzony
    d=[10**10 for _ in range(v)]        #odległość wierzchołków od wierzchołka s
    visited[s]=1
    d[s]=0
    Q.appendleft(s)
    while len(Q)>0:
        p=Q.pop()
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
                Q.appendleft(u)

    if len(paths)==1:
        return (paths[0],t)
    if len(paths)==0:
        return None
    
    one=paths[0]
    two=paths[1]
    how_many=0
    while parents[one] is not None:
        if one==two and parents[one]==parents[two]:
            git=True
            for j in range(2,len(paths)):
                tmp=paths[j]
                for i in range(how_many):
                    tmp=parents[tmp]
                if tmp!=one or parents[tmp]!=parents[one]:
                    git=False
                    break
            if git:
                return one, parents[one]
        one=parents[one]
        two=parents[two]
        how_many+=1

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )