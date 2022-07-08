# Domy i sklepy 
# Mamy mapę miasteczka w którym są domy i sklepy. Na mapie są również drogi (każda długosći 1), które łączą dom z domem lub dom ze sklepem
# Znajdź dla każdego domu odległość do najbliższego sklepu.
# Mapa w postaci listy krawędzi, liczby parzyste to sklepy, nieparzyste reprezentują domy
# -------------------------------------------------------------------
# Rozwiązanie: na samym początku wrzucić wszystkie sklepy do kolejki w BFS oraz przypisywać kolejne domy

from collections import deque

def foo(T):
    n=0
    for u in T:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1
    d=[ 10**10 for _ in range(n)]
    visited= [ 0 for _ in range(n)]
    G= [ [] for _ in range(n)]
    q=deque()
    for u in T:
        G[u[0]].append(u[1])
        G[u[1]].append(u[0])
        if u[0]%2==0:
            q.append(u[0])
            d[u[0]]=0
            visited[u[0]]=1
        if u[1]%2==0:
            q.append(u[1])
            d[u[1]]=0
            visited[u[1]]=0

    while len(q)>0:
        s=q.popleft()
        for u in G[s]:
            if u%2==1 and visited[u]==0:
                d[u]=d[s]+1
                visited[u]=1
                q.append(u)
    
    for i in range(n):
        if i%2==1:
            print("Numer domu:", i, "Dlugosc drogi:", d[i])


if __name__=="__main__":
    # Liczby nieparzyste to domy a parzyste to sklepy 
    mapa=[[1,3],[2,3],[4,3],[7,8],[7,8],[8,5],[5,9],[9,11],[9,10],[5,11],[3,5],[1,7],[3,13],[5,13],[17,13],[17,15],[13,15]]
    foo(mapa)
    