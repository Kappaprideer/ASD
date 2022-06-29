# Andrzej Zaborniak
# Algorytm sprawdza dla wierzchołka w którm sie znajduje czy nie ma lepszego przelotu szybowcem do dowolnego wierzchołka z grafu. Jeśli taki istnieje
# to zapisuje odległość występującą do danego wierzchołka oraz wrzuca go do kolejki piorytetowej. Lekko zmodyfikowana Dijkstra. Złożoność O(n^2)


from kol3btesty import runtests
from queue import PriorityQueue

def airports( G, A, s, t ):
    n=len(G)
    c=[ 10**10 for _ in range(n)]
    visited=[ 0 for _ in range(n)]
    Q=PriorityQueue()
    Q.put((0,s))   
    c[s]=0

    while not Q.empty():
        u=Q.get()
        s=u[1]
        if c[s]==u[0]:
            if s==t:
                return c[t]
            for j in range(n):
                if c[j]>A[s]+A[j]+c[s]:
                    c[j]=A[s]+A[j]+c[s]
                    Q.put((c[j],j))

            for i, w in G[s]:
                if c[i]>c[s]+w:
                    c[i]=c[s]+w
                    Q.put((c[i],i))
        
    return c[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )